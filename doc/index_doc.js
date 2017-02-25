var docs = {};
docs.mapper = {"mapper": {"type": "module", "members": {"SocketReader": {"herit": ["object"], "type": "class", "members": {"__init__": {"type": "function", "parameters": [{"name": "self", "doc": null, "annotation": "SocketReader"}, {"name": "sock", "doc": "#socket \u00e0 lire en tant que tableau", "annotation": "socket"}], "return": null, "name": "__init__", "doc": "\n        @param sock socket \u00e0 lire en tant que tableau\n        "}}, "name": "SocketReader", "doc": "\n    La socket devient une liste.\n    Stocke toutes les donn\u00e9es lues.\n    @warn A ne pas utiliser dans la d\u00e9claration d'une boucle.\n\n    reader = SocketReader(socket)\n    #lecture de 5 octets\n    print (reader[:5])\n    "}}, "name": "mapper", "doc": "\nModule outil pour transformer la lecture d'une socket en lecture de tableau.\n"}};
docs.tools = {"tools": {"type": "module", "members": {"tobytes": {"type": "function", "parameters": [{"name": "v", "doc": "#valeur \u00e0 convertir"}, {"name": "enc", "value": "utf-8", "doc": "#encodage pour les cha\u00eenes de caract\u00e8res"}], "return": null, "name": "tobytes", "doc": "\n    Convertit None, une cha\u00eene, un dictionnaire en binaire\n    @param v valeur \u00e0 convertir\n    @param enc encodage pour les cha\u00eenes de caract\u00e8res\n    @return binaire\n    "}, "read_cookie": {"type": "function", "parameters": [{"name": "headers", "doc": "#ent\u00eates de la requ\u00eate"}], "return": null, "name": "read_cookie", "doc": "\n    Lit un cookie\n    @param headers ent\u00eates de la requ\u00eate\n    @return {name, value} ou None\n    "}, "write_cookie": {"type": "function", "parameters": [{"name": "nam", "doc": "#nom du cookie"}, {"name": "val", "doc": "#valeur du cookoie"}, {"name": "hs", "value": "{}", "doc": "#dictionnaire des ent\u00eates \u00e0 enrichir"}, {"name": "secured", "value": "False", "doc": "#pour contraindre l'utilisation via https"}, {"name": "seconds", "value": "None", "doc": "#d\u00e9lai d\"expiration en secondes"}], "return": null, "name": "write_cookie", "doc": "\n    Ecrit un cookie\n    @param nam nom du cookie\n    @param val valeur du cookoie\n    @param hs dictionnaire des ent\u00eates \u00e0 enrichir\n    @param secured pour contraindre l'utilisation via https\n    @param seconds d\u00e9lai d''expiration en secondes\n    "}, "json": {"type": "module", "name": "json"}, "answer": {"type": "function", "parameters": [{"name": "code", "value": "200", "doc": "#code HTTP"}, {"name": "headers", "value": "{}", "doc": "#ent\u00eates de la r\u00e9ponse"}, {"name": "mime", "value": "None", "doc": "#pour le format de la r\u00e9ponse"}, {"name": "charset", "value": "utf-8", "doc": "#encodage de la r\u00e9ponse"}, {"name": "body", "value": "", "doc": "#corps de la r\u00e9ponse en binaire"}, {"name": "callback", "value": "None", "doc": "#traitement post \u00e9mission HTTP callback(socket, callbackCtx)", "annotation": "fonction"}, {"name": "callbackCtx", "value": "None", "doc": "#contexte"}], "return": null, "name": "answer", "doc": "\n    Construit une r\u00e9ponse HTTP\n    @param code code HTTP\n    @param headers ent\u00eates de la r\u00e9ponse\n    @param mime pour le format de la r\u00e9ponse\n    @param charset encodage de la r\u00e9ponse\n    @param body corps de la r\u00e9ponse en binaire\n    @param callback traitement post \u00e9mission HTTP callback(socket, callbackCtx)\n    @param callbackCtx contexte\n    @return [code, headers, content, callback, callbackCtx]\n    "}, "readfile": {"type": "function", "parameters": [{"name": "path", "doc": "#chemin du fichier"}], "return": null, "name": "readfile", "doc": "\n    Lit le contenu d'un fichier texte\n    @param path chemin du fichier\n    @return contenu du fichier texte\n    "}}, "name": "tools", "doc": "\nOutils\n"}};
docs.gui = {"gui": {"type": "module", "members": {"App": {"herit": ["object"], "type": "class", "members": {"cmd_purge": {"type": "function", "parameters": [{"name": "self", "doc": null}], "return": null, "name": "cmd_purge", "doc": "\n        Remise \u00e0 z\u00e9ro de la zone de texte\n        "}, "cmd_start": {"type": "function", "parameters": [{"name": "self", "doc": null}], "return": null, "name": "cmd_start", "doc": "\n        D\u00e9marrage du serveur\n        "}, "__init__": {"type": "function", "parameters": [{"name": "self", "doc": null}, {"name": "stacksize", "value": "1000", "doc": "#taille max. de la stacktrace"}], "return": null, "name": "__init__", "doc": "\n        Constructeur\n        @param stacksize taille max. de la stacktrace\n        "}, "cmd_stop": {"type": "function", "parameters": [{"name": "self", "doc": null}], "return": null, "name": "cmd_stop", "doc": "\n        Arr\u00eat du serveur\n        "}}, "name": "App", "doc": "\n    Application tkinter de Pyweb\n    "}, "builtins": {"type": "module", "name": "builtins"}, "_tkinter": {"type": "module", "name": "_tkinter"}, "tkinter.scrolledtext": {"type": "module", "name": "tkinter.scrolledtext"}, "tkinter": {"type": "module", "name": "tkinter"}, "web": {"type": "module", "name": "web"}, "start": {"type": "function", "parameters": [{"name": "secured", "value": "False", "doc": "#si https sinon http"}, {"name": "port", "value": "8080", "doc": "#port"}, {"name": "test", "value": "False", "doc": "#si test \u00e0 g\u00e9n\u00e9rer"}, {"name": "chemin_js", "value": "www/test.js", "doc": "#chemin du fichier js de test"}], "return": null, "name": "start", "doc": "\n    @param secured si https sinon http\n    @param port port\n    @param test si test \u00e0 g\u00e9n\u00e9rer\n    @param chemin_js chemin du fichier js de test\n    "}, "sys": {"type": "module", "name": "sys"}, "re": {"type": "module", "name": "re"}, "reloader": {"type": "module", "name": "reloader"}, "py3": {"type": "module", "name": "py3"}, "constants": {"type": "module", "name": "constants"}, "threading": {"type": "module", "name": "threading"}, "Buffer": {"herit": ["object"], "type": "class", "members": {"write": {"type": "function", "parameters": [{"name": "self", "doc": null}, {"name": "st", "doc": "#texte \u00e0 ajouter"}], "return": null, "name": "write", "doc": "\n        Ecrit\n        @param st texte \u00e0 ajouter\n        "}, "__init__": {"type": "function", "parameters": [{"name": "self", "doc": null}, {"name": "text", "doc": "#zone de texte"}, {"name": "main", "value": "True", "doc": "#si sortie standard sinon sortie d'erreur"}, {"name": "outfile", "value": "None", "doc": "#fichier de sortie ou None"}, {"name": "stacksize", "value": "1000", "doc": "#taille max. de la stacktrace"}], "return": null, "name": "__init__", "doc": "\n        Constructeur\n        @param text zone de texte\n        @param main si sortie standard sinon sortie d'erreur\n        @param outfile fichier de sortie ou None\n        @param stacksize taille max. de la stacktrace\n        "}, "restore": {"type": "function", "parameters": [{"name": "self", "doc": null}], "return": null, "name": "restore", "doc": "\n        Lib\u00e8re la sortie standard et la sortie d'erreur\n        "}, "reset": {"type": "function", "parameters": [{"name": "self", "doc": null}], "return": null, "name": "reset", "doc": "\n        Nettoie la zone de texte\n        "}}, "name": "Buffer", "doc": "\n    Gestion de la sortie standard et de la sortie d'erreur\n    "}, "importlib": {"type": "module", "name": "importlib"}, "stop": {"type": "function", "parameters": [], "return": null, "name": "stop", "doc": "\n    Arr\u00eat du serveur\n    "}, "main": {"type": "function", "parameters": [], "return": null, "name": "main", "doc": "\n    Main function\n    "}}, "name": "gui", "doc": "\nInterface graphique de pyweb\n"}};
docs.iframe = {"iframe": {"type": "module", "members": {"base64": {"type": "module", "name": "base64"}, "readMessage": {"type": "function", "parameters": [{"name": "sock", "doc": "#la socket \u00e0 lire"}], "return": null, "name": "readMessage", "doc": "\n    Lit un message depuis la socket\n    @param sock la socket \u00e0 lire\n    @return message {data, fin:trame de fin, closed:fermeture, ping}\n    "}, "padd": {"type": "function", "parameters": [{"name": "array", "doc": "#tableau \u00e0 renseigner"}, {"name": "value", "doc": "#valeur \u00e0 additionner"}], "return": null, "name": "padd", "doc": "\n    Additionne la valeur dans le tableau [fort, faible]\n    @param array tableau \u00e0 renseigner\n    @param value valeur \u00e0 additionner\n    @return le tableau\n    "}, "mapper": {"type": "module", "name": "mapper"}, "websocket_headers": {"type": "function", "parameters": [{"name": "headers", "doc": "#ent\u00eates HTTP pour r\u00e9cup\u00e9rer Sec-WebSocket-Key"}], "return": null, "name": "websocket_headers", "doc": "\n    Construit les ent\u00eates pour un accord d'ouverture de la websocket\n    @param headers ent\u00eates HTTP pour r\u00e9cup\u00e9rer Sec-WebSocket-Key\n    @return dictionnaire des ent\u00eates pour une r\u00e9ponse positive\n    "}, "_hashlib": {"type": "module", "name": "_hashlib"}, "writeMessage": {"type": "function", "parameters": [{"name": "sock", "doc": "#la socket"}, {"name": "text", "doc": "#texte \u00e0 transmettre"}, {"name": "mask", "value": "[]", "doc": "#masque"}, {"name": "encoding", "value": "utf-8", "doc": "#encodage"}, {"name": "toClose", "value": "False", "doc": "#fermeture"}, {"name": "toPing", "value": "False", "doc": "#ping"}, {"name": "toPong", "value": "False", "doc": "#pong"}], "return": null, "name": "writeMessage", "doc": "\n    Ecrit un message et l'envoie vers la socket\n    @param sock la socket\n    @param text texte \u00e0 transmettre\n    @param mask masque\n    @param encoding encodage\n    @param toClose fermeture\n    @param toPing ping\n    @param toPong pong\n    "}, "fromMessage": {"type": "function", "parameters": [{"name": "buffer", "doc": "#trame \u00e0 lire (sous la forme d'un tableau)"}], "return": null, "name": "fromMessage", "doc": "\n    D\u00e9code une trame websocket (RFC 6455).\n    @param buffer trame \u00e0 lire (sous la forme d'un tableau)\n    @return message {data, fin:trame de fin, closed:fermeture, ping}\n    "}, "toTextPayload": {"type": "function", "parameters": [{"name": "text", "doc": "#texte \u00e0 envoyer"}, {"name": "mask", "value": "[]", "doc": "#masque"}, {"name": "encoding", "value": "utf-8", "doc": "#encodage"}, {"name": "toClose", "value": "False", "doc": "#\u00e0 fermer"}, {"name": "toPing", "value": "False", "doc": "#ping"}, {"name": "toPong", "value": "False", "doc": "#pong"}], "return": null, "name": "toTextPayload", "doc": "\n    Construit une trame websocket (RFC 6455)\n    @param text texte \u00e0 envoyer\n    @param mask masque\n    @param encoding encodage\n    @param toClose \u00e0 fermer\n    @param toPing ping\n    @param toPong pong\n    @return message binaire\n    "}, "bvalid": {"type": "function", "parameters": [{"name": "val", "doc": "#valeur \u00e0 v\u00e9rifier"}, {"name": "mask", "doc": "#masque binaire"}], "return": null, "name": "bvalid", "doc": "\n    V\u00e9rifie que la valeur correspond au masque\n    @param val valeur \u00e0 v\u00e9rifier\n    @param mask masque binaire\n    @return \u00e9galit\u00e9\n    "}, "depad": {"type": "function", "parameters": [{"name": "array", "doc": "#tableau \u00e0 lire"}], "return": null, "name": "depad", "doc": "\n    R\u00e9cup\u00e8re la valeur depuis un tableau [fort, faible]\n    @param array tableau \u00e0 lire\n    @return le nombre calcul\u00e9\n    "}}, "name": "iframe", "doc": "\nGestion des trames Websockets (RFC 6455)\n\nM\u00e9thodes \u00e0 utiliser:\n    websocket_headers\n    readMessage\n    writeMessage\n"}};
docs.py3 = {"py3": {"type": "module", "members": {"json": {"type": "module", "name": "json"}, "os": {"type": "module", "name": "os"}, "web": {"type": "module", "name": "web"}, "MyHttpHandler": {"herit": ["http.server.SimpleHTTPRequestHandler", "http.server.BaseHTTPRequestHandler", "socketserver.StreamRequestHandler", "socketserver.BaseRequestHandler", "object"], "type": "class", "members": {"do_GET": {"type": "function", "parameters": [{"name": "self", "doc": null}], "return": null, "name": "do_GET", "doc": "Redirig\u00e9 vers execute"}, "execute": {"type": "function", "parameters": [{"name": "self", "doc": null}, {"name": "method", "doc": "#GET, POST, PUT ou DELETE"}], "return": null, "name": "execute", "doc": "\n        @param method GET, POST, PUT ou DELETE\n        "}, "send": {"type": "function", "parameters": [{"name": "self", "doc": null}, {"name": "codehsbody", "doc": "#r\u00e9ponse sous la forme d'une liste"}], "return": null, "name": "send", "doc": "\n        @param codehsbody r\u00e9ponse sous la forme d'une liste\n            [code_http, dictionnaire_entetes, contenu_binaire,\n                None/fonction_postemission, None/contexte_postemission]\n            avec fonction_postemission(socket_client, contexte_postem)\n        "}, "socketserver": {"type": "module", "name": "socketserver"}, "do_PUT": {"type": "function", "parameters": [{"name": "self", "doc": null}], "return": null, "name": "do_PUT", "doc": "Redirig\u00e9 vers execute"}, "do_POST": {"type": "function", "parameters": [{"name": "self", "doc": null}], "return": null, "name": "do_POST", "doc": "Redirig\u00e9 vers execute"}, "http.client": {"type": "module", "name": "http.client"}, "__init__": {"type": "function", "parameters": [{"name": "self", "doc": null}, {"name": "socket", "doc": "#socket ouverte pour le client ayant \u00e9mis la requ\u00eate"}, {"name": "client_address", "doc": "#adresse du client (IP et port)"}, {"name": "server", "doc": "#serveur multi-threaded"}], "return": null, "name": "__init__", "doc": "\n        @param socket socket ouverte pour le client ayant \u00e9mis la requ\u00eate\n        @param client_address adresse du client (IP et port)\n        @param server serveur multi-threaded\n        "}, "http.server": {"type": "module", "name": "http.server"}, "do_DELETE": {"type": "function", "parameters": [{"name": "self", "doc": null}], "return": null, "name": "do_DELETE", "doc": "Redirig\u00e9 vers execute"}}, "name": "MyHttpHandler", "doc": "\n    R\u00e9ceptionneur des requ\u00eates\n    "}, "ThreadedServer": {"herit": ["socketserver.ThreadingMixIn", "socketserver.TCPServer", "socketserver.BaseServer", "object"], "type": "class", "members": {"setcore": {"type": "function", "parameters": [{"name": "self", "doc": null}, {"name": "core", "doc": "#dictionnaire des actions"}], "return": null, "name": "setcore", "doc": "\n        Positionne le dictionnaire des actions\n        @param core dictionnaire des actions\n        "}, "socketserver": {"type": "module", "name": "socketserver"}, "find": {"type": "function", "parameters": [{"name": "self", "doc": null}, {"name": "method", "doc": "#m\u00e9thode de la requ\u00eate HTTP"}, {"name": "uri", "doc": "#URL de la requ\u00eate HTTP"}], "return": null, "name": "find", "doc": "\n        Recherche l'action (callback) pour r\u00e9pondre \u00e0 la requ\u00eate\n        @use self.core dictionnaire des actions\n        @param method m\u00e9thode de la requ\u00eate HTTP\n        @param uri URL de la requ\u00eate HTTP\n        @return action\n        "}, "socket": {"type": "module", "name": "socket"}}, "name": "ThreadedServer", "doc": "Serveur multi-threaded"}, "socketserver": {"type": "module", "name": "socketserver"}, "re": {"type": "module", "name": "re"}, "base64": {"type": "module", "name": "base64"}, "run": {"type": "function", "parameters": [{"name": "core", "value": "<web.Core object at 0xb708baec>", "doc": "#dictionnaire des actions"}, {"name": "server_class", "value": "<class 'py3.ThreadedServer'>", "doc": "#serveur", "annotation": "classe"}, {"name": "handler_class", "value": "<class 'py3.MyHttpHandler'>", "doc": "#r\u00e9ceptionneur des requ\u00eates", "annotation": "classe"}, {"name": "port", "value": "8000", "doc": "#port s\u00e9curi\u00e9 ou non"}, {"name": "secured", "value": "False", "doc": "#s\u00e9curis\u00e9", "annotation": "boolean"}, {"name": "certfile", "value": "run/certificate.crt", "doc": "#certificat (n\u00e9cesssaire si secured == True)"}, {"name": "keyfile", "value": "run/privateKey.key", "doc": "#cl\u00e9 priv\u00e9e (n\u00e9cesssaire si secured == True)"}], "return": {"name": "return", "annotation": "blocking", "doc": null}, "name": "run", "doc": "\n    Lancement du serveur\n    @param core dictionnaire des actions\n    @param server_class serveur\n    @param handler_class r\u00e9ceptionneur des requ\u00eates\n    @param port port s\u00e9curi\u00e9 ou non\n    @param secured s\u00e9curis\u00e9\n    @param certfile certificat (n\u00e9cesssaire si secured == True)\n    @param keyfile cl\u00e9 priv\u00e9e (n\u00e9cesssaire si secured == True)\n    "}, "ssl": {"type": "module", "name": "ssl"}, "threading": {"type": "module", "name": "threading"}, "finish": {"type": "function", "parameters": [], "return": null, "name": "finish", "doc": "\n    Arret du serveur\n    "}, "iframe": {"type": "module", "name": "iframe"}, "http": {"type": "module", "name": "http"}, "sys": {"type": "module", "name": "sys"}, "urllib": {"type": "module", "name": "urllib"}}, "name": "py3", "doc": "\nServeur HTTP\n"}};
docs.web = {"web": {"type": "module", "members": {"HttpConverter": {"herit": ["object"], "type": "class", "members": {"encode": {"type": "function", "parameters": [{"name": "self", "doc": null}, {"name": "data", "doc": "#donn\u00e9e \u00e0 encoder"}], "return": null, "name": "encode", "doc": "\n        @param data donn\u00e9e \u00e0 encoder\n        @return r\u00e9sultat de l'encodage\n        "}, "decode": {"type": "function", "parameters": [{"name": "self", "doc": null}, {"name": "data", "doc": "#donn\u00e9e \u00e0 d\u00e9coder"}], "return": null, "name": "decode", "doc": "\n        @param data donn\u00e9e \u00e0 d\u00e9coder\n        @return r\u00e9sultat du d\u00e9codage\n        "}, "__init__": {"type": "function", "parameters": [{"name": "self", "doc": null}, {"name": "nam", "doc": "#nom du codec"}, {"name": "params", "doc": "#liste des param\u00e8tres requis"}, {"name": "fin", "doc": "#fonction de conversion en entr\u00e9e"}, {"name": "fout", "doc": "#fonction de conversion en sortie"}], "return": null, "name": "__init__", "doc": "\n        @param nam nom du codec\n        @param params liste des param\u00e8tres requis\n        @param fin fonction de conversion en entr\u00e9e\n        @param fout fonction de conversion en sortie\n        "}, "missing": {"type": "function", "parameters": [{"name": "self", "doc": null}, {"name": "liste", "doc": "#parm\u00e8tres re\u00e7ues"}], "return": null, "name": "missing", "doc": "\n        Calcule la liste des param\u00e8tres manquants\n        @param liste parm\u00e8tres re\u00e7ues\n        @return liste des param\u00e8tres requis et non re\u00e7us\n        "}}, "name": "HttpConverter", "doc": "\n    Traite les conversions en entr\u00e9e et en sortie\n    "}, "noCodec": {"type": "object", "name": "noCodec", "class": "web.HttpConverter"}, "Core": {"herit": ["object"], "type": "class", "members": {"declare": {"type": "function", "parameters": [{"name": "self", "doc": null}, {"name": "action_name", "doc": "#nom de la fonction"}, {"name": "method", "doc": "#\"GET\", \"POST\", \"PUT\", \"DELETE\""}, {"name": "expr", "doc": "#expression r\u00e9guli\u00e8re pour d\u00e9tection des param\u00e8tres"}, {"name": "pars", "doc": "#nom des param\u00e8tres"}, {"name": "act", "doc": "#fonction \u00e0 appeler"}, {"name": "uri", "doc": "#mod\u00e8le d'URI"}, {"name": "test", "doc": "#informations pour la g\u00e9n\u00e9ration de tests"}, {"name": "doc", "doc": "#documentation de la fonction"}], "return": null, "name": "declare", "doc": "\n        Ajoute une action\n            @param action_name nom de la fonction\n            @param method ''GET'', ''POST'', ''PUT'', ''DELETE''\n            @param expr expression r\u00e9guli\u00e8re pour d\u00e9tection des param\u00e8tres\n            @param pars nom des param\u00e8tres\n            @param act  fonction \u00e0 appeler\n            @param uri  mod\u00e8le d'URI\n            @param test informations pour la g\u00e9n\u00e9ration de tests\n            @param doc documentation de la fonction\n        "}, "get_parameters": {"type": "function", "parameters": [{"name": "self", "doc": null}, {"name": "_action", "doc": "#action"}, {"name": "converter", "doc": "#ne sert \u00e0 rien"}], "return": null, "name": "get_parameters", "doc": "\n        [{name, type, pattern, default?}*]\n        @param _action action\n        @param converter ne sert \u00e0 rien\n        @return liste des param\u00e8tres sans les 2 premiers\n        "}, "reset": {"type": "function", "parameters": [{"name": "self", "doc": null}], "return": null, "name": "reset", "doc": "\n        R\u00e9initialise l'objet.\n        Evite les conflits de d\u00e9claration.\n        "}, "control_parameter": {"type": "function", "parameters": [{"name": "self", "doc": null}, {"name": "nam", "doc": "#nom du param\u00e8tre"}, {"name": "typ", "doc": "#type"}, {"name": "patt", "doc": "#pattern"}, {"name": "val", "doc": "#valeur \u00e0 tester"}], "return": null, "name": "control_parameter", "doc": "\n        Controle la valeur d'un param\u00e8tre en fonction de son pattern\n        et de son type num\u00e9rique (number)\n        @param nam nom du param\u00e8tre\n        @param typ type\n        @param patt pattern\n        @param val valeur \u00e0 tester\n        "}, "__init__": {"type": "function", "parameters": [{"name": "self", "doc": null}], "return": null, "name": "__init__", "doc": "\n        Utilise une liste pour g\u00e9rer l'ordre de d\u00e9claration des actions\n        "}, "http": {"type": "function", "parameters": [{"name": "self", "doc": null}, {"name": "method", "doc": "#GET, PUT, DELETE, POST, .*"}, {"name": "uri", "doc": "#URL avec des patterns (/chemin/{fichier}\\.{extension})"}, {"name": "test", "value": "[]", "doc": "#liste d'informations pour la g\u00e9n\u00e9ration des tests"}, {"name": "converter", "value": "<web.HttpConverter object at 0xb6bb434c>", "doc": "#ne sert \u00e0 rien"}], "return": null, "name": "http", "doc": "\n        Annotation de d\u00e9claration d'une action dans le core\n        @param method GET, PUT, DELETE, POST, .*\n        @param uri URL avec des patterns (/chemin/{fichier}\\.{extension})\n        @param test liste d'informations pour la g\u00e9n\u00e9ration des tests\n        @param converter ne sert \u00e0 rien\n        @return action\n        "}, "prepare_test": {"type": "function", "parameters": [{"name": "self", "doc": null}, {"name": "test", "value": "False", "doc": "#si les tests doivent \u00eatre g\u00e9n\u00e9r\u00e9s"}, {"name": "chemin_js", "value": "www/test.js", "doc": "#chemin de g\u00e9n\u00e9ration du test"}], "return": null, "name": "prepare_test", "doc": "\n        Initialise le fichier javsacript de description des test\n        pour les actions d\u00e9clar\u00e9es\n        @param test si les tests doivent \u00eatre g\u00e9n\u00e9r\u00e9s\n        @param chemin_js chemin de g\u00e9n\u00e9ration du test\n        "}, "find": {"type": "function", "parameters": [{"name": "self", "doc": null}, {"name": "method", "doc": "#m\u00e9thode de la requ\u00eate HTTP"}, {"name": "uri", "doc": "#URL de la req\u00eate"}], "return": null, "name": "find", "doc": "\n        Cherche et retourne la premi\u00e8re action compatible avec la requ\u00eate\n        @param method m\u00e9thode de la requ\u00eate HTTP\n        @param uri URL de la req\u00eate\n        @return (action, dictionnaire des param\u00e8tres de l'URL)\n        "}, "get_infotest": {"type": "function", "parameters": [{"name": "self", "doc": null}], "return": null, "name": "get_infotest", "doc": "\n        Fournit les informations pou l'\u00e9tablissement de tests\n        "}}, "name": "Core", "doc": "\n    Dictionnaire des actions\n    "}, "json": {"type": "module", "name": "json"}, "core": {"type": "object", "name": "core", "class": "web.Core"}, "inspect": {"type": "module", "name": "inspect"}, "jsonCodec": {"type": "object", "name": "jsonCodec", "class": "web.HttpConverter"}, "doc": {"type": "module", "name": "doc"}, "re": {"type": "module", "name": "re"}, "websocket": {"type": "function", "parameters": [{"name": "callback", "doc": "#fonction de r\u00e9ception de l'\u00e9v\u00e9nement"}], "return": null, "name": "websocket", "doc": "\n    Annotation de d\u00e9claration d'un gestionnaire d'\u00e9v\u00e9nements de websocket.\n    callback(contexte, donn\u00e9es)\n        ouverture : donn\u00e9es = True\n        fermeture : donn\u00e9es = False\n        message : donn\u00e9es = str\n        contexte : fourni en tant que retour de l'action\n            (si None pas d'appel \u00e0 la callbac)\n    @param callback fonction de r\u00e9ception de l'\u00e9v\u00e9nement\n    @return gestionnaire de websocket\n    "}, "instanciate_core": {"type": "function", "parameters": [], "return": null, "name": "instanciate_core", "doc": "\n    @return instance de Core\n    "}, "iframe": {"type": "module", "name": "iframe"}}, "name": "web", "doc": "\nModule de gestion des actions et des websockets\n"}};
docs.reloader = {"reloader": {"type": "module", "members": {"time": {"type": "module", "name": "time"}, "threading": {"type": "module", "name": "threading"}, "os": {"type": "module", "name": "os"}, "Surveillant": {"herit": ["threading.Thread", "object"], "type": "class", "members": {"verifie": {"type": "function", "parameters": [{"name": "self", "doc": null}], "return": null, "name": "verifie", "doc": "\n        V\u00e9rifie et charge le modules python modifi\u00e9s dans le r\u00e9pertoire courant\n        "}, "lit": {"type": "function", "parameters": [{"name": "self", "doc": null}], "return": null, "name": "lit", "doc": "\n        Permet de lire les lignes de la sortie standard.\n        Sortie d\u00e8s la premi\u00e8re ligne vide re\u00e7ue.\n        "}, "run": {"type": "function", "parameters": [{"name": "self", "doc": null}], "return": null, "name": "run", "doc": "\n        Usage indirect par la fonction start\n        "}, "__init__": {"type": "function", "parameters": [{"name": "self", "doc": null}, {"name": "laps", "value": "1", "doc": "#temps d'attente en secondes entre chaque v\u00e9rification"}], "return": null, "name": "__init__", "doc": "\n        @param laps temps d'attente en secondes entre chaque v\u00e9rification\n        "}, "threading": {"type": "module", "name": "threading"}}, "name": "Surveillant", "doc": "\n    Thread pour le rechargement des modules python du r\u00e9pertoire courant\n    "}, "importlib": {"type": "module", "name": "importlib"}, "sys": {"type": "module", "name": "sys"}}, "name": "reloader", "doc": "Module permettant de recherger les modules pythons modifi\u00e9s\ndans le r\u00e9pertoire courant\n"}};
docs.doc = {"doc": {"type": "module", "members": {"esc": {"type": "function", "parameters": [{"name": "st", "doc": "#cha\u00eene \u00e0 \u00e9chapper", "annotation": "string"}], "return": null, "name": "esc", "doc": "\n    Remplace les guillements par 2 apostrophes\n    @param st cha\u00eene \u00e0 \u00e9chapper\n    @return cha\u00eene \u00e9chapp\u00e9e\n    "}, "docfunction": {"type": "function", "parameters": [{"name": "nam", "doc": "#nom de la fonction", "annotation": "string"}, {"name": "obj", "doc": "#objet fonction", "annotation": "fonction"}], "return": null, "name": "docfunction", "doc": "\n    Retourne la documentation de la fonction.\n    Les param\u00e8tres sont r\u00e9cup\u00e9r\u00e9s directement\n    depuis la fonction ou __arguments__.\n    {type, name, return, parameters, doc}\n    @use getargs\n    @use protect\n    @param nam nom de la fonction\n    @param obj objet fonction\n    @return la documentation d'une fonction\n    "}, "json": {"type": "module", "name": "json"}, "protect": {"type": "function", "parameters": [{"name": "act", "doc": "#fonction encapsulant", "annotation": "fonction"}, {"name": "_action", "doc": "#fonction encapsulant", "annotation": "fonction"}, {"name": "docannot", "value": "", "doc": "#documentation \u00e0 retenir de la fonction d'encapsulation", "annotation": "string"}], "return": null, "name": "protect", "doc": "\n    Permet de pr\u00e9server les informations n\u00e9cessaires\n    \u00e0 la documentation dans le cas d'un d\u00e9corateur.\n    Stocke les param\u00e8tres dans __arguments__\n    @param act fonction encapsulant\n    @param _action fonction encapsulant\n    @param docannot documentation \u00e0 retenir de la fonction d'encapsulation\n    @return None\n\ndef decorateur(parametres_decorateur):\n    def encapsulateur(fonction):\n        def substitu (*args, **argv):\n            return fonction (*args, **argv)\n        doc = ''''\n        if f.__doc__ is not None:\n            doc = f.__doc__\n        docannot = ''@InfoDecorateur %s'' % (parametres_decorateur)\n        protect(substitu, fonction, docannot)\n        return substitu\n    return encapsulateur\n    "}, "os": {"type": "module", "name": "os"}, "inspect": {"type": "module", "name": "inspect"}, "getargs": {"type": "function", "parameters": [{"name": "_action", "doc": "#fonction", "annotation": "fonction"}], "return": null, "name": "getargs", "doc": "\n    Construit la liste des infos sur le retour et les param\u00e8tres\n    {name, annotation, doc}\n    @use getparamdoc\n    @use inspect.getfullargspec\n    @param _action fonction\n    @return liste des infos sur les param\u00e8tres et le type retour\n    (premier \u00e9l\u00e9ment de la liste)\n    "}, "getparamdoc": {"type": "function", "parameters": [{"name": "doc", "doc": "#documentation de la fonction", "annotation": "string"}, {"name": "p", "doc": "#nom du param\u00e8tre", "annotation": "string"}, {"name": "typ", "value": "param", "doc": "#\"param\" ou \"return\"", "annotation": "string"}], "return": null, "name": "getparamdoc", "doc": "\n    Retourne les informations sur un param\u00e8tre ou le retour d'une fonction\n    @param doc documentation de la fonction\n    @param p nom du param\u00e8tre\n    @param typ ''param'' ou ''return''\n    @return chaine concat\u00e9n\u00e9e\n    "}, "parcours": {"type": "function", "parameters": [{"name": "arbo", "value": "{}", "doc": "#objet conteneur", "annotation": "map"}, {"name": "cmod", "value": "None", "doc": "#module racine utilis\u00e9 pour \u00e9carter les objets import\u00e9s", "annotation": "module"}, {"name": "nam", "value": "None", "doc": "#nom r\u00e9cup\u00e9r\u00e9 depuis le conteneur", "annotation": "string"}, {"name": "obj", "value": "None", "doc": "#objet dont la documentation sera associ\u00e9e \u00e0 arbo[nam]", "annotation": "object"}], "return": null, "name": "parcours", "doc": "\n    Calcule le dictionnaire de documentation du module fourni en tant que obj\n    @use inspect\n    @use docfunction\n    @param arbo objet conteneur\n    @param cmod module racine utilis\u00e9 pour \u00e9carter les objets import\u00e9s\n    @param nam nom r\u00e9cup\u00e9r\u00e9 depuis le conteneur\n    @param obj objet dont la documentation sera associ\u00e9e \u00e0 arbo[nam]\n    @return documentation sous la forme d'un dictionnaire\n    "}}, "name": "doc", "doc": "G\u00e9n\u00e8re la documentation des modules python pr\u00e9sents\ndans le r\u00e9pertoire courant et contruit un fichier doc/index_doc.js.\n\nRepose sur les modules\n@module inspect\n@module os\n@module json\n"}};
docs.clihttp = {"clihttp": {"type": "module", "members": {"test_http": {"type": "function", "parameters": [{"name": "secured", "doc": "#s\u00e9curis\u00e9"}, {"name": "trusted", "value": "False", "doc": "#de confiance"}], "return": null, "name": "test_http", "doc": "\n    M\u00e9thode de test\n    @param secured s\u00e9curis\u00e9\n    @param trusted de confiance\n    "}, "base64": {"type": "module", "name": "base64"}, "ssl": {"type": "module", "name": "ssl"}, "test_ws": {"type": "function", "parameters": [{"name": "secured", "doc": "#s\u00e9curis\u00e9"}, {"name": "trusted", "value": "False", "doc": "#de confiance"}], "return": null, "name": "test_ws", "doc": "\n    M\u00e9thode de test\n    @param secured s\u00e9curis\u00e9\n    @param trusted de confiance\n    "}, "_hashlib": {"type": "module", "name": "_hashlib"}, "getmask": {"type": "function", "parameters": [], "return": null, "name": "getmask", "doc": "\n    G\u00e9n\u00e8re une liste al\u00e9atoire de 4 octets\n    "}, "getconnection": {"type": "function", "parameters": [{"name": "secured", "value": "False", "doc": "#vrai si https"}, {"name": "host", "value": "localhost", "doc": "#hote"}, {"name": "port", "value": "8080", "doc": "#port"}, {"name": "trusted", "value": "False", "doc": "#si le certificat SSL n'est pas connu par une autorit\u00e9"}], "return": null, "name": "getconnection", "doc": "\n    Fournit une connexion s\u00e9curis\u00e9e ou non\n    @param secured vrai si https\n    @param host hote\n    @param port port\n    @param trusted si le certificat SSL n'est pas connu par une autorit\u00e9\n    "}, "test_http2": {"type": "function", "parameters": [{"name": "secured", "doc": "#s\u00e9curis\u00e9"}, {"name": "trusted", "value": "False", "doc": "#de confiance"}], "return": null, "name": "test_http2", "doc": "\n    M\u00e9thode de test\n    @param secured s\u00e9curis\u00e9\n    @param trusted de confiance\n    "}, "iframe": {"type": "module", "name": "iframe"}, "http": {"type": "module", "name": "http"}, "random": {"type": "module", "name": "random"}}, "name": "clihttp", "doc": "\nClient pour les tests\n"}};
