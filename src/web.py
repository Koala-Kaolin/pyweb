#!/usr/bin/python3


"""
Module de gestion des actions et des websockets
"""

import re
import inspect
import json

from doc import protect
from iframe import writeMessage, readMessage, websocket_headers

core = None


class HttpConverter():
    """
    Traite les conversions en entrée et en sortie
    """
    def __init__(self, nam, params, fin, fout):
        """
        @param nam nom du codec
        @param params liste des paramètres requis
        @param fin fonction de conversion en entrée
        @param fout fonction de conversion en sortie
        """
        self.fin = fin
        self.fout = fout
        self.params = params
        self.name = nam

    def decode(self, data):
        """
        @param data donnée à décoder
        @return résultat du décodage
        """
        return self.fin(data)

    def encode(self, data):
        """
        @param data donnée à encoder
        @return résultat de l'encodage
        """
        return self.fout(data)

    def missing(self, liste):
        """
        Calcule la liste des paramètres manquants
        @param liste parmètres reçues
        @return liste des paramètres requis et non reçus
        """
        return [e for e in self.params if e not in liste]


jsonCodec = HttpConverter("jsonCodec", [], json.loads, json.dumps)
noCodec = HttpConverter("noCodec", [], lambda o: o, lambda o: o)


class Core():
    """
    Dictionnaire des actions
    """
    def __init__(self):
        """
        Utilise une liste pour gérer l'ordre de déclaration des actions
        """
        self.reset()

    def reset(self):
        """
        Réinitialise l'objet.
        Evite les conflits de déclaration.
        """
        self.declares = {}
        self.ordonnes = []
        self.registered_action_names = []
        self.infotest = {}

    def find(self, method, uri):
        """
        Cherche et retourne la première action compatible avec la requête
        @param method méthode de la requête HTTP
        @param uri URL de la reqête
        @return (action, dictionnaire des paramètres de l'URL)
        """
        print("vérif", uri)
        for a in self.ordonnes:
            vv = re.match("^" + a + "$", method + "@" + uri)
            if vv is not None:
                b = self.declares[a]
                vv = vv.groups()
                tab = {}
                for i in range(0, len(b[0])):
                    tab[b[0][i]] = vv[i + 1]
                return (b[1], tab)
        return (None, None)

    def declare(self, action_name, method, expr, pars, act, uri, test, doc):
        """
        Ajoute une action
            @param action_name nom de la fonction
            @param method "GET", "POST", "PUT", "DELETE"
            @param expr expression régulière pour détection des paramètres
            @param pars nom des paramètres
            @param act  fonction à appeler
            @param uri  modèle d'URI
            @param test informations pour la génération de tests
            @param doc documentation de la fonction
        """
        if action_name in self.registered_action_names:
            raise Exception("Fonction %s already declared" % action_name)
        self.registered_action_names.append(action_name)
        self.declares["(" + method + ")@" + expr] = [pars, act]
        self.ordonnes.append("(" + method + ")@" + expr)
        self.infotest[action_name] = (method, uri, test, doc)

    def get_infotest(self):
        """
        Fournit les informations pou l'établissement de tests
        """
        return self.infotest

    def get_parameters(self, _action, converter):
        """
        [{name, type, pattern, default?}*]
        @param _action action
        @param converter ne sert à rien
        @return liste des paramètres sans les 2 premiers
        """
        if "__root__" in dir(_action):
            _action = _action.__root__
        moins = list(inspect.getfullargspec(_action).args)
        defaul = _action.__defaults__
        miss = converter.missing(moins)
        if len(miss) > 0:
            raise Exception(
                "Missing parameter for this codec (" +
                converter.name + "): " + str(miss))
        # FIXME rechercher les éléments annotés
        # pour la documentation + vérifier la propagation

        cons = []  # [{"type": "doc", "value": _action.__doc__}]
        if _action.__annotations__ is not None:
            for i in range(2, len(moins)):
                ka = moins[i]
                defa = "UnDefined"
                if defaul is not None:
                    j = i + len(defaul) - len(moins)
                    if j > -1:
                        defa = defaul[j]
                if ka not in _action.__annotations__.keys():
                    raise Exception(
                        "Not annotated parameter %s for %s" % (
                            ka, _action.__name__))
                desca = _action.__annotations__[ka]
                typa = None
                cona = None
                if ' ' in desca:
                    pos = desca.index(' ')
                    typa = desca[0:pos]
                    cona = desca[pos+1:].strip()
                else:
                    typa = desca
                if defa == "UnDefined":
                    cons.append({"name": ka, "type": typa, "pattern": cona})
                else:
                    cons.append({
                        "name": ka, "type": typa, "pattern": cona,
                        "default": defa})
        return cons

    def control_parameter(self, nam, typ, patt, val):
        """
        Controle la valeur d'un paramètre en fonction de son pattern
        et de son type numérique (number)
        @param nam nom du paramètre
        @param typ type
        @param patt pattern
        @param val valeur à tester
        """
        if typ == "number":
            if not str(val).isnumeric:
                raise Exception("%s - Not a numeric value [%s]" % (
                    nam, str(val)))
        if patt is not None:
            if not re.match(patt, str(val)):
                raise Exception("%s - Not a matching value [%s] for [%s]" % (
                    nam, str(val), patt))

    def http(self, method, uri, test=[], converter=noCodec):
        """
        Annotation de déclaration d'une action dans le core
        @param method GET, PUT, DELETE, POST, .*
        @param uri URL avec des patterns (/chemin/{fichier}\.{extension})
        @param test liste d'informations pour la génération des tests
        @param converter ne sert à rien
        @return action
        """
        pars = re.findall("\{([^{}]*)\}", uri)
        expr = re.sub(
            "{[^{}]*}", "([.a-zA-Z0-9-_#]*)",
            uri.replace("*", "[.a-zA-Z0-9-_#]*"))

        def __act(_action):
            cons = self.get_parameters(_action, converter)

            def act(*args, **argv):
                headers = args[0]
                params = args[1]
                args = list(args)
                for con in cons:
                    va = None
                    ka = con["name"]
                    typa = con["type"]
                    pata = None
                    if "default" in con.keys():
                        va = con["default"]
                    if typa != "header":
                        if ka in params.keys():
                            va = params[ka]
                    else:
                        if ka in headers.keys():
                            va = headers[ka]
                    if "pattern" in con.keys():
                        self.control_parameter(ka, typa, con["pattern"], va)
                    args.append(va)
                    print(con, va)
                args = tuple(args)
                print("=========")
                return _action(*args, **argv)

            self.declare(
                _action.__name__, method, expr, pars,
                act, uri, cons, _action.__doc__)
            doc = ""
            if _action.__doc__ is not None:
                doc = _action.__doc__
            docannot = "@http method=%s, uri=%s" % (method, uri)
            protect(act, _action, docannot)
            return act
        return __act

    def prepare_test(self, test=False, chemin_js="www/test.js"):
        """
        Initialise le fichier javsacript de description des test
        pour les actions déclarées
        @param test si les tests doivent être générés
        @param chemin_js chemin de génération du test
        """
        with open(chemin_js, "w") as f:
            f.write("\ntests=")
            if test:
                f.write(json.dumps(core.get_infotest()))
            else:
                f.write(json.dumps({}))
            f.write(";\n")


def instanciate_core(reset=False):
    """
    @param reset indicateur de la remise à zéro des actions
    @return instance de Core
    """
    global core
    if core is None:
        core = Core()
    if reset:
        core.reset()
    return core


def websocket(callback):
    """
    Annotation de déclaration d'un gestionnaire d'événements de websocket.
    callback(contexte, données)
        ouverture : données = True
        fermeture : données = False
        message : données = str
        contexte : fourni en tant que retour de l'action
            (si None pas d'appel à la callbac)
    @param callback fonction de réception de l'événement
    @return gestionnaire de websocket
    """
    def websocket_(f):
        def listener(sock, ctx):
            def send(data):
                writeMessage(sock, str(data), toClose=(data is None))
            ctx["send"] = send
            callback(ctx, True)
            while True:
                text = readMessage(sock)
                if text["closed"]:
                    callback(ctx, False)
                    break
                else:
                    callback(ctx, text["data"])

        def encapsule(*args, **argv):
            headers = args[0]
            params = args[1]
            ctx = f(*args, **argv)
            res = None
            if ctx is not None:
                hs = websocket_headers(headers)
                res = [101, hs, b"", listener, ctx]
            else:
                res = [403, {}, b"", None, None]
            return res
        protect(encapsule, f, "@websocket")
        return encapsule
    return websocket_
