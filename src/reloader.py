#!/usr/bin/python3


"""Module permettant de recherger les modules pythons modifiés
dans le répertoire courant
"""

import os.path
import importlib
import threading
import sys
import time

import lab


class Surveillant (threading.Thread):
    """
    Thread pour le rechargement des modules python du répertoire courant
    """
    def __init__(self, laps=1):
        """
        @param laps temps d'attente en secondes entre chaque vérification
        """
        threading.Thread.__init__(self)
        self.heures = {}
        self.laps = laps

    def run(self):
        """
        Usage indirect par la fonction start
        """
        self.isactive = True
        while self.isactive:
            time.sleep(self.laps)
            self.verifie()

    def verifie(self):
        """
        Vérifie et charge le modules python modifiés dans le répertoire courant
        """
        for f in [e for e in os.listdir(".") if e.endswith(".py")]:
            mtim = int(os.path.getmtime(f))
            if f in self.heures.keys():
                if self.heures[f] < mtim:
                    # Chargement si nécessaire
                    if f[:-3] in sys.modules.keys():
                        importlib.reload(__import__(f[:-3]))
                        print(f)
            self.heures[f] = mtim

    def lit(self):
        """
        Permet de lire les lignes de la sortie standard.
        Sortie dès la première ligne vide reçue.
        """
        while self.isactive:
            line = sys.stdin.readline()[:-1]
            if line == "":
                self.isactive = False

if __name__ == "__main__":
    surv = Surveillant()
    surv.start()
    try:
        lab.start(True)
    except:
        surv.isactive = False
