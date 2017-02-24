#!/usr/bin/python3


"""
Outils
"""


import json


def read_cookie(headers):
    """
    Lit un cookie
    @param headers entêtes de la requête
    @return {name, value} ou None
    """
    if "Cookie" not in headers.keys():
        return None
    cookie = headers["Cookie"]
    idx = cookie.index("=")
    name = cookie[0:idx]
    chain = cookie[idx + 1:]
    if len(chain) > 0 and chain[0] == '"':
        chain = chain[1: -1]
    print(name, chain)
    return {"name": name, "value": chain}


def write_cookie(nam, val, hs={}, secured=False, seconds=None):
    """
    Ecrit un cookie
    @param nam nom du cookie
    @param val valeur du cookoie
    @param hs dictionnaire des entêtes à enrichir
    @param secured pour contraindre l'utilisation via https
    @param seconds délai d"expiration en secondes
    """
    sec = ""
    if secured:
        sec = "; Secure"
    sec2 = ""
    if seconds is not None:
        sec2 = "; Max-Age=%d" % seconds
    hs["Set-Cookie"] = '%s="%s"; HttpOnly%s%s' % (nam, val, sec, sec2)
    return hs


def tobytes(v, enc="utf-8"):
    """
    Convertit None, une chaîne, un dictionnaire en binaire
    @param v valeur à convertir
    @param enc encodage pour les chaînes de caractères
    @return binaire
    """
    if v is None:
        return b""
    typ = type(v)
    if typ == bytes:
        return v
    if typ == str:
        return bytes(v, enc)
    if typ == dict or typ == list:
        return bytes(json.dumps(v), enc)
    return bytes(str(v), enc)


def readfile(path):
    """
    Lit le contenu d'un fichier texte
    @param path chemin du fichier
    @return contenu du fichier texte
    """
    with open(path) as f:
        return f.read()


def answer(
    code=200, headers={}, mime=None, charset="utf-8", body="",
    callback: "fonction"=None, callbackCtx=None
):
    """
    Construit une réponse HTTP
    @param code code HTTP
    @param headers entêtes de la réponse
    @param mime pour le format de la réponse
    @param charset encodage de la réponse
    @param body corps de la réponse en binaire
    @param callback traitement post émission HTTP callback(socket, callbackCtx)
    @param callbackCtx contexte
    @return [code, headers, content, callback, callbackCtx]
    """
    if mime is not None:
        headers["Content-Type"] = mime
    return [code, headers, tobytes(body, charset), callback, callbackCtx]
