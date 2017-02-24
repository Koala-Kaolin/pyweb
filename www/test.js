
tests={"action2_fichier_codem_niv1": ["GET", "/codem/{path1}\\.{ext}", [], "\n    @param entetes headers\n    @param lus param\u00e8tres dans l'url ou dans le formule post\n    "], "wshandler": [".*", "/ws/{chat}", [{"pattern": null, "name": "chat", "type": "path"}], "@websocket\n\n    @param headers headers\n    @param params param\u00e8tres dans l'url ou dans le formule post\n    @param chat nom du salon.\n    "], "action_test_unique": ["GET|POST", "/test/unique/{id}", [{"pattern": "[a-zA-Z]{10}", "name": "ptexte", "type": "text"}, {"pattern": null, "name": "htexte", "type": "header"}, {"pattern": ".{10}", "name": "pnum", "default": 1, "type": "number"}, {"pattern": null, "name": "pfile", "default": null, "type": "file"}], "\n    Fonction de test\n    @param headers entetes\n    @param params disctionnaire des param\u00e8tres\n    @param ptexte test\n    @param htexte test\n    @param pnum test\n    @param pfile test\n    "], "defaulthandler": [".*", "/*", [], "\n    @param headers headers\n    @param params param\u00e8tres dans l'url ou dans le formule post\n    "], "action2_fichier_codem_niv2": ["GET", "/codem/{path2}/{path1}\\.{ext}", [], "\n    @param entetes headers\n    @param lus param\u00e8tres dans l'url ou dans le formule post\n    "], "echoparams": [".*", "/echo", [], "\n    @param headers headers\n    @param params param\u00e8tres dans l'url ou dans le formule post\n    "], "action1_global": ["POST", "/poste", [], "\n    @param entetes headers\n    @param lus param\u00e8tres dans l'url ou dans le formule post\n    "], "action1_auth": ["GET", "/auth.do", [], "\n    @param entetes = http.client.HTTPMessage\n    @param lus param\u00e8tres dans l'url ou dans le formule post\n    "], "action1_verif": ["GET", "/verif.do", [], "@Rejet ADMIN\n\n    @param entetes headers\n    @param lus param\u00e8tres dans l'url ou dans le formule post\n    "], "action2_fichier": [".*", "/{path1}\\.{ext}", [], "\n    @param entetes headers\n    @param lus param\u00e8tres dans l'url ou dans le formule post\n    "]};