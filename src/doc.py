#!/usr/bin/python3


"""Génère la documentation des modules python présents
dans le répertoire courant et contruit un fichier doc/index_doc.js.

Repose sur les modules
@module inspect
@module os
@module json
"""

import inspect
import os
import json

verif_strict = True


def esc(st: "string"):
    """
    Remplace les guillements par 2 apostrophes
    @param st chaîne à échapper
    @return chaîne échappée
    """
    if st is None:
        return None
    return st.replace('"', "''")


def getparamdoc(doc: "string", p: "string", typ: "string" = "param"):
    """
    Retourne les informations sur un paramètre ou le retour d'une fonction
    @param doc documentation de la fonction
    @param p nom du paramètre
    @param typ "param" ou "return"
    @return chaine concaténée
    """
    if doc is None:
        return None
    tab = [
        e.strip()[len(typ) + 1:].strip()
        for e in doc.split("\n") if e.strip().startswith("@"+typ)]
    tab = [
        "#" + e.strip()[len(p) + 1:].strip()
        for e in tab if e.strip().startswith(p + " ")]
    if len(tab) < 1:
        return None
    else:
        return "\n".join(tab)


def getargs(_action: "fonction"):
    """
    Construit la liste des infos sur le retour et les paramètres
    {name, annotation, doc}
    @use getparamdoc
    @use inspect.getfullargspec
    @param _action fonction
    @return liste des infos sur les paramètres et le type retour
    (premier élément de la liste)
    """
    args = list(inspect.getfullargspec(_action).args)
    defaults = _action.__defaults__
    l = []
    if "return" in _action.__annotations__.keys():
        dr = getparamdoc(_action.__doc__, "", "return")
        l.append({
            "name": "return",
            "annotation": _action.__annotations__["return"],
            "doc": dr})
    dd = 0
    if defaults is not None:
        dd = len(args) - len(defaults)
    else:
        dd = -1
    for i in range(0, len(args)):
        dr = getparamdoc(_action.__doc__, args[i])
        arg = {"name": args[i], "doc": dr}
        if dd > -1 and i >= dd:
            arg["value"] = str(defaults[i - dd])
        if args[i] in _action.__annotations__.keys():
            arg["annotation"] = _action.__annotations__[args[i]]
        l.append(arg)
    return l


def protect(act: "fonction", _action: "fonction", docannot: "string" = ""):
    """
    Permet de préserver les informations nécessaires
    à la documentation dans le cas d'un décorateur.
    Stocke les paramètres dans __arguments__
    @param act fonction encapsulant
    @param _action fonction encapsulant
    @param docannot documentation à retenir de la fonction d'encapsulation
    @return None

def decorateur(parametres_decorateur):
    def encapsulateur(fonction):
        def substitu (*args, **argv):
            return fonction (*args, **argv)
        doc = ""
        if f.__doc__ is not None:
            doc = f.__doc__
        docannot = "@InfoDecorateur %s" % (parametres_decorateur)
        protect(substitu, fonction, docannot)
        return substitu
    return encapsulateur
    """
    if "__arguments__" in dir(_action):
        act.__arguments__ = _action.__arguments__
    else:
        act.__arguments__ = getargs(_action)
    doc = ""
    if _action.__doc__ is not None:
        doc = _action.__doc__
    if len(docannot) > 0 and docannot[-1] != '\n':
        docannot += '\n'
    if "__root__" in dir(_action):
        act.__root__ = _action.__root__
    else:
        act.__root__ = _action
    act.__doc__ = docannot + doc
    act.__module__ = _action.__module__
    act.__name__ = _action.__name__
    act.__annotations__ = _action.__annotations__


def docfunction(nam: "string", obj: "fonction"):
    """
    Retourne la documentation de la fonction.
    Les paramètres sont récupérés directement
    depuis la fonction ou __arguments__.
    {type, name, return, parameters, doc}
    @use getargs
    @use protect
    @param nam nom de la fonction
    @param obj objet fonction
    @return la documentation d'une fonction
    """
    if verif_strict and obj.__doc__ is None:
        raise Exception(
            "Missing documentation for function %s for %s"
            % (obj.__name__, obj.__module__))
    args = None
    if "__arguments__" in dir(obj):
        args = obj.__arguments__
    else:
        args = getargs(obj)
    retu = None
    if args is not None and len(args) > 0 and args[0]["name"] == "return":
        retu = args[0]
        args = args[1:]
    for arg in args:
        if verif_strict and arg["doc"] is None and arg["name"] != "self":
            raise Exception(
                "Missing documentation for function %s parameter %s in %s"
                % (obj.__name__, arg["name"], obj.__module__))
    ret = {
        "type": "function",
        "name": nam,
        "return": retu,
        "parameters": args,
        "doc": esc(obj.__doc__)}
    return ret


def parcours(
    arbo: "map" = {},
    cmod: "module" = None,
    nam: "string" = None,
    obj: "object" = None
):
    """
    Calcule le dictionnaire de documentation du module fourni en tant que obj
    @use inspect
    @use docfunction
    @param arbo objet conteneur
    @param cmod module racine utilisé pour écarter les objets importés
    @param nam nom récupéré depuis le conteneur
    @param obj objet dont la documentation sera associée à arbo[nam]
    @return documentation sous la forme d'un dictionnaire
    """
    root = arbo
    mo = inspect.getmodule(obj)
    if cmod != mo:
        if inspect.ismodule(obj):
            if nam is None or nam == "":
                nam = mod.__name__
            arbo[nam] = {"type": "module", "name": nam}
        elif mo is not None:
            arbo[mo.__name__] = {"type": "module", "name": mo.__name__}
        return
    elif nam is None or nam == "":
        nam = mod.__name__
    if inspect.isclass(obj):
        if verif_strict and obj.__doc__ is None:
            raise Exception(
                "Missing documentation for class %s for %s"
                % (obj.__name__, obj.__module__))
        arbo[nam] = {
            "type": "class",
            "name": nam,
            "members": {},
            "doc": esc(obj.__doc__),
            "herit": [
                str(e).replace("<class '", "").replace("'>", "")
                for e in obj.mro()][1:]}
        arbo = arbo[nam]["members"]
    elif inspect.ismodule(obj):
        if verif_strict and obj.__doc__ is None:
            raise Exception(
                "Missing documentation for module %s for %s"
                % (obj.__name__, obj.__module__))
        arbo[nam] = {
            "type": "module",
            "name": nam,
            "members": {},
            "doc": esc(obj.__doc__)}
        arbo = arbo[nam]["members"]
    elif inspect.ismethod(obj) or inspect.isfunction(obj):
        arbo[nam] = docfunction(nam, obj)
        return
    else:
        ty = type(obj)
        if ty in [str, int, float, bool, None]:
            arbo[nam] = {"type": ty, "name": nam, "doc": esc(obj.__doc__)}
            return
    if not inspect.ismodule(obj) and not inspect.isclass(obj):
        arbo[nam] = {
            "type": "object",
            "name": nam,
            "class": str(type(obj)).replace("<class '", "").replace("'>", "")}
        return
    for n, ob in inspect.getmembers(obj):
        if n[0] != "_" or n == "__init__":
            parcours(arbo, cmod, n, ob)
    return root


if __name__ == "__main__":
    mods = [e[:-3] for e in os.listdir("src") if e.endswith(".py")]

    with open("doc/%s_doc.js" % "index", "w") as f:
        f.write("var docs = {};\n")
        for smod in mods:
            mod = __import__(smod)
            arbo = parcours({}, mod, "", mod)
            f.write('docs.%s = %s;\n' % (mod.__name__, json.dumps(arbo)))
