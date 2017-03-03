#!/usr/bin/python3


"""
Sandbox
"""

import os
import json
import random

from doc import protect
from py3 import run
from web import instanciate_core, websocket

from tools import answer, read_cookie, write_cookie, tobytes, readfile


print("lab.py reloaded ...")
os.chdir(os.getcwd())

www_dir = "./www"

core = instanciate_core(reset=True)


def echo(par, pre=True):
    """
    Annotation pour afficher en console le contenu d'un paramètre
    @param par nom du paramètre à afficher
    @param pre si le message doit être afficher en début
    """
    def spam2(f):
        def ff_spam(*args, **argv):
            headers = args[0]
            params = args[1]
            if not pre:
                return f(*args, **argv)
            v = None
            if par in params.keys():
                v = params[par]
                print("@echo", par, "=", v)
            if pre:
                return f(*args, **argv)
        protect(ff_spam, f)
        return ff_spam

    return spam2


def rejet(par):
    """
    Annotation pour rejeter lorsque le paramètre requis n'est pas présent
    @use answer
    @param par nom du paramètre à contrôler
    """
    # FIXME contrôler
    def spam2(f):
        def ff_spam(headers, params):
            return answer(code=403)

            return f(headers, params)

        docannot = "@Rejet %s" % (par)
        protect(ff_spam, f, docannot)
        return ff_spam

    return spam2


def wsecho(ctx, data):
    """
    Gestion des messages reçus par une websocket
    @param ctx contexte
    @param data message
    """
    send = ctx["send"]
    if type(data) == bool:
        if data:
            send("Bienvenue sur " + ctx["salon"])
        else:
            print("Aurevoir")
    else:
        send(ctx["salon"] + ">+ " + data)


@core.http("GET|POST", "/test/unique/{id}")
@echo("pfile")
def action_test_unique(
        headers,
        params,
        ptexte: "text [a-zA-Z]{10}",
        htexte: "header",
        pnum: "number .{10}"=1,
        pfile: "file"=None):
    """
    Fonction de test
    @param headers entetes
    @param params disctionnaire des paramètres
    @param ptexte test
    @param htexte test
    @param pnum test
    @param pfile test
    """
    return answer(200, body="action_test_unique", mime="text/html")


@core.http("GET", "/auth.do")
@echo("Cookie")
# @echo("@ip@")
def action1_auth(entetes, lus) -> 403:
    """
    @param entetes = http.client.HTTPMessage
    @param lus paramètres dans l'url ou dans le formule post
    """
    # print("param_text", lus["param_text"])
    chaine = random.getrandbits(90)
    id_session = str(chaine) + "@@"  # + str(lus["@ip@"])
    hs = write_cookie("session", id_session, seconds=30)
    return answer(code=203, headers=hs, body=read_cookie(entetes))


@core.http("GET", "/verif.do")
@echo("Cookie")
@rejet("ADMIN")
@echo("@ip@")
# FIXME read_cookie
def action1_verif(entetes, lus):
    """
    @param entetes headers
    @param lus paramètres dans l'url ou dans le formule post
    """
    cookie = read_cookie(entetes)
    cook = ""
    if cookie is not None:
        print(cookie["name"], "==", cookie["value"])
        cook = cookie["value"]
    hs = {}
    return answer(code=203, headers=hs, body=cook)


@core.http("POST", "/poste")
@echo("path1")
@echo("trois")
def action1_global(entetes: "entetes p", lus: "lus p") -> "ne retourne rien":
    """
    @param entetes headers
    @param lus paramètres dans l'url ou dans le formule post
    """
    print("actions1.lus", lus)
    # print("actions1.entetes", entetes)
    return answer(code=203, headers={"ent1": "val1"}, body="corps reponse")


@core.http(".*", "/{path1}\.{ext}")
def action2_fichier(entetes, lus):
    """
    @param entetes headers
    @param lus paramètres dans l'url ou dans le formule post
    """
    mimes = {
        "html": "text/html", "md": "text/plain",
        "css": "text/css", "js": "text/javascript"}
    print("MON NOUVEAU", type(entetes), type(lus))
    try:
        if not lus["ext"] in mimes.keys():
            raise Exception("forbidden")
        hs = {"Content-Type": mimes[lus["ext"]]}
        if "file" in lus.keys():
            hs["Content-Disposition"] = (
                "attachment; filename=\"%s\"" % lus["file"])
        bincont = readfile(www_dir + "/" + lus["path1"] + "." + lus["ext"])
        return answer(code=202, headers=hs, body=bincont)
    except Exception as ex:
        print("action2", ex)
        return answer(
            code=404, body=lus["path1"] + "." + lus["ext"],
            mime=mimes["html"])


@core.http("GET", "/codem/{path1}\.{ext}")
def action2_fichier_codem_niv1(entetes, lus):
    """
    @param entetes headers
    @param lus paramètres dans l'url ou dans le formule post
    """
    mimes = {
        "html": "text/html", "css": "text/css",
        "js": "text/javascript", "md": "text/plain"}
    try:
        if not lus["ext"] in mimes.keys():
            raise Exception("forbidden")
        hs = {"Content-Type": mimes[lus["ext"]]}
        if "file" in lus.keys():
            hs["Content-Disposition"] = (
                "attachment; filename=\"%s\"" % lus["file"])
        bincont = readfile(
            www_dir + "/codem/" + lus["path1"] + "." + lus["ext"])
        return answer(code=202, headers=hs, body=bincont)
    except Exception as ex:
        print("action2", ex)
        return answer(
            code=404, body=lus["path1"] + "." + lus["ext"],
            mime=mimes["html"])


@core.http("GET", "/codem/{path2}/{path1}\.{ext}")
def action2_fichier_codem_niv2(entetes: "un"="zapata", lus: "deux"="vide"):
    """
    @param entetes headers
    @param lus paramètres dans l'url ou dans le formule post
    """
    mimes = {
        "html": "text/html", "css": "text/css",
        "js": "text/javascript",  "md": "text/plain"}
    try:
        if not lus["ext"] in mimes.keys():
            raise Exception("forbidden")
        hs = {"Content-Type": mimes[lus["ext"]]}
        if "file" in lus.keys():
            hs["Content-Disposition"] = (
                "attachment; filename=\"%s\"" % lus["file"])
        bincont = readfile(
            www_dir + "/codem/" + lus["path2"] + "/" +
            lus["path1"] + "." + lus["ext"])
        return answer(code=202, headers=hs, body=bincont)
    except Exception as ex:
        print("action2", ex)
        return answer(
            code=404, body=lus["path1"] + "." + lus["ext"],
            mime=mimes["html"])


@core.http(".*", "/ws/{chat}")
@websocket(wsecho)
def wshandler(headers, params, chat: "path"):
    """
    @param headers headers
    @param params paramètres dans l'url ou dans le formule post
    @param chat nom du salon.
    """
    print("chat", chat)
    return {"salon": params["chat"]}


@core.http(".*", "/echo")
def echoparams(headers, params):
    """
    @param headers headers
    @param params paramètres dans l'url ou dans le formule post
    """
    print({"h": str(headers), "p": params})
    return answer(body={"h": str(headers._headers), "pip": params})


@core.http(".*", "/*")
def defaulthandler(headers, params):
    """
    @param headers headers
    @param params paramètres dans l'url ou dans le formule post
    """
    return answer(code=509)


if __name__ == "__main__":
    core.prepare_test(test=False, chemin_js="www/test.js")
    run(secured=False, port=8080, core=core)
