#!/usr/bin/python3


"""
Client pour les tests
"""

import http.client
import iframe
import random
import ssl

from base64 import b64encode
from hashlib import sha1


def getmask():
    """
    Génère une liste aléatoire de 4 octets
    """
    ret = [random.randint(0, 255) for i in range(4)]
    return ret


def getconnection(secured=False, host="localhost", port=8080, trusted=False):
    """
    Fournit une connexion sécurisée ou non
    @param secured vrai si https
    @param host hote
    @param port port
    @param trusted si le certificat SSL n'est pas connu par une autorité
    """
    if secured:
        ctx = ssl.create_default_context()
        if trusted:
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
        con = http.client.HTTPSConnection(
            host, port,
            context=ctx)
    else:
        con = http.client.HTTPConnection(
            host, port)
    return con


def test_http(secured, trusted=False):
    """
    Méthode de test
    @param secured sécurisé
    @param trusted de confiance
    """
    con = getconnection(secured, trusted=trusted)
    con.request("GET", "/test.html")
    rep = con.getresponse()
    print(rep.read()[:50], rep.code)
    return rep.code == 200


def test_http2(secured, trusted=False):
    """
    Méthode de test
    @param secured sécurisé
    @param trusted de confiance
    """
    con = getconnection(
        secured, host="www.qwant.com",
        port=443, trusted=trusted)
    con.request("GET", "/?q=python3")
    rep = con.getresponse()
    print(rep.read()[:50], rep.code)
    return rep.code == 200


def test_ws(secured, trusted=False):
    """
    Méthode de test
    @param secured sécurisé
    @param trusted de confiance
    """
    con = getconnection(secured, trusted=trusted)
    key = str(
            b64encode(
                sha1(
                    bytes(
                        "".join([chr(i) for i in getmask()]),
                        "utf-8")).digest()), "utf-8")
    keyrep = "Sec-WebSocket-Accept: %s\r\n" % str(
        b64encode(sha1(bytes(key + iframe.CST_GUID, "utf-8")).digest()),
        "utf-8")
    con.putrequest("GET", "/ws/testA")
    con.putheader("Sec-WebSocket-Version", "13")
    con.putheader("Sec-WebSocket-Key", key)
    con.endheaders()
    con.send(b"")
    s = con.sock
    iframe.writeMessage(s, "message1", mask=getmask())
    rep = []
    while True:
        rep.append(s.recv(1))
        if len(rep) > 10 and rep[-4:] == [b"\r", b"\n", b"\r", b"\n"]:
            rep = str(b"".join(rep), "utf-8")
            if keyrep not in rep:
                raise Exception(
                    "Handshake failure : %s not in %s" % (keyrep, rep))
            break
    count = 0
    while True:
        text = iframe.readMessage(s)
        if text["closed"]:
            print("fin")
            break
        else:
            count += 1
            print(count, text)
            iframe.writeMessage(
                s, "message1", toClose=(count > 1), mask=getmask())
            if count > 1:
                break
    return True


if __name__ == "__main__":
    # test_http2(True, trusted=False)
    test_http(True, trusted=True)
    test_ws(True, trusted=True)
