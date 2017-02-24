#!/usr/bin/python3


"""
Serveur HTTP
"""

import re
import os
import sys
import ssl
import json
import iframe
import threading
import http.server
import socketserver
import urllib.parse
import base64

from web import instanciate_core


httpd = None


class MyHttpHandler (http.server.SimpleHTTPRequestHandler):
    """
    Réceptionneur des requêtes
    """
    def __init__(self, socket, client_address, server):
        """
        @param socket socket ouverte pour le client ayant émis la requête
        @param client_address adresse du client (IP et port)
        @param server serveur multi-threaded
        """
        self.client_socket = socket
        self.server = server
        self.client_address = client_address
        http.server.SimpleHTTPRequestHandler.__init__(
            self, socket, client_address, server)

    def do_DELETE(self):
        """Redirigé vers execute"""
        return self.execute("DELETE")

    def do_PUT(self):
        """Redirigé vers execute"""
        return self.execute("PUT")

    def do_GET(self):
        """Redirigé vers execute"""
        return self.execute("GET")

    def do_POST(self):
        """Redirigé vers execute"""
        return self.execute("POST")

    def execute(self, method):
        """
        @param method GET, POST, PUT ou DELETE
        """
        # récup des paramètres de l'url
        path = self.path
        uri = path
        lus = {"@ip@": self.client_address[0]}
        if "?" in uri:
            query = uri[uri.index("?") + 1:]
            uri = uri[:uri.index("?")]
            lus = urllib.parse.parse_qs(query)
            for k, v in lus.items():
                if type(v) == list:
                    if len(v) == 1:
                        lus[k] = v[0]
                    elif len(v) == 0:
                        lus[k] = None

        # recherche de l'action
        func_pathparams = self.server.find(method, uri)
        if func_pathparams[1] is not None:
            for k, v in func_pathparams[1].items():
                lus[k] = v
        else:
            print("WARNING - missing action for", method, uri)

        # récup du body limité à 9Mo max
        lu = None
        if "Content-Length" in self.headers.keys():
            le = self.headers["Content-Length"]
            if int(le) > 10000000:
                le = 0
            lu = self.rfile.read(int(le))

        cont = ""
        if "Content-Type" in self.headers.keys():
            cont = self.headers["Content-Type"]
        if "application/x-www-form-urlencoded" == cont:
            lu = str(lu, "utf-8")
            lus2 = urllib.parse.parse_qs(lu)
            for k, v in lus2.items():
                lus[k] = v
        elif "multipart/form-data" in cont:
            sep = bytes(cont[cont.index("boundary=")+9:], "utf-8")
            elts = lu.split(sep)[1:-1]
            for elt in elts:
                idx = elt.index(bytes("\r\n\r\n", "utf-8"))
                desc = str(elt[2:idx], "utf-8")
                desc = re.split("[ \t]*(\r\n|;|,|:|=)[ \t]*", desc)
                descr = {}
                for i in range(0, len(desc)//4+1):
                    descr[desc[i*4]] = desc[i*4+2].replace('"', "")
                cont = elt[idx+4:-4]
                obj = None
                if "Content-Type" not in descr.keys():
                    obj = str(cont, "utf-8")
                elif (
                        descr["filename"] is not None and
                        len(descr["filename"])) > 0:
                    obj = {
                        "filename": descr["filename"],
                        "type": descr["Content-Type"],
                        "content": str(base64.b64encode(cont), "utf-8")}
                lus[descr["name"]] = obj
        elif "application/json" == cont:
            lu = str(lu, "utf-8")
            lus["json"] = json.loads(lu)

        # fin de récupération
        print(method, uri, lus)

        # action
        if func_pathparams[0] is not None:
            result = func_pathparams[0](self.headers, lus)
            if result is not None:
                self.send(result)
                return

        mime = "application/json"
        hs = {"Content-Type": (mime+"%s") % ";charset=utf-8"}
        cont = bytes(
            json.dumps({"method": method, "uri": uri, "code": 404}),
            "utf-8")
        self.send([404, hs, cont, None, None])

    def send(self, codehsbody):
        """
        @param codehsbody réponse sous la forme d'une liste
            [code_http, dictionnaire_entetes, contenu_binaire,
                None/fonction_postemission, None/contexte_postemission]
            avec fonction_postemission(socket_client, contexte_postem)
        """
        self.send_response(codehsbody[0])
        for n, v in codehsbody[1].items():
            self.send_header(n, v)
        self.end_headers()
        if len(codehsbody[2]) > 0:
            self.wfile.write(codehsbody[2])
        if codehsbody[3] is not None:
            codehsbody[3](self.client_socket, codehsbody[4])


class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """Serveur multi-threaded"""
    def find(self, method, uri):
        """
        Recherche l'action (callback) pour répondre à la requête
        @use self.core dictionnaire des actions
        @param method méthode de la requête HTTP
        @param uri URL de la requête HTTP
        @return action
        """
        return self.core.find(method, uri)

    def setcore(self, core):
        """
        Positionne le dictionnaire des actions
        @param core dictionnaire des actions
        """
        self.core = core


def run(
    core=instanciate_core(),
    server_class: "classe"=ThreadedServer,
    handler_class: "classe"=MyHttpHandler,
    port=8000,
    secured: "boolean"=False,
    certfile="run/certificate.crt",
    keyfile="run/privateKey.key"
) -> "blocking":
    """
    Lancement du serveur
    @param core dictionnaire des actions
    @param server_class serveur
    @param handler_class réceptionneur des requêtes
    @param port port sécurié ou non
    @param secured sécurisé
    @param certfile certificat (nécesssaire si secured == True)
    @param keyfile clé privée (nécesssaire si secured == True)
    """
    global httpd
    try:
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        httpd.setcore(core)
        if secured:
            try:
                httpd.socket = ssl.wrap_socket(
                    httpd.socket,
                    server_side=True,
                    do_handshake_on_connect=True,
                    certfile=certfile,
                    keyfile=keyfile)
            except Exception as e:
                print(e)
                raise Exception(
                    "openssl req -x509 -sha256 -nodes" +
                    " -days 365 -newkey rsa:2048" +
                    " -keyout run/privateKey.key" +
                    " -out run/certificate.crt")
        print("Server running on port:"+str(port)+" sécurisé:"+str(secured))
        httpd.serve_forever()
    except OSError as e:
        print("!!! Veuillez patienter:", e.strerror, "!!!")
        raise e
    except KeyboardInterrupt:
        finish()


def finish():
    """
    Arret du serveur
    """
    global httpd
    if httpd is not None:
        print("Shutting down server")
        httpd.socket.close()
        httpd.shutdown()
        httpd.server_close()
        print("Server shut down")
        httpd = None
