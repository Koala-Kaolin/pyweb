#!/usr/bin/python3

"""
Interface graphique de pyweb
"""

import sys
import threading
import importlib

from tkinter import *
from tkinter.scrolledtext import *

from reloader import Surveillant

from py3 import run, finish
from web import instanciate_core


if len(sys.argv) < 2:
    print(
        """Arguments:
        script_directory
        modules_names_to_be_loaded""")

sys.path.append(sys.argv[1:])
core = instanciate_core()


def start(secured=False, port=8080, test=False, chemin_js="www/test.js"):
    """
    @param secured si https sinon http
    @param port port
    @param test si test à générer
    @param chemin_js chemin du fichier js de test
    """
    for modname in sys.argv[2:]:
        __import__(modname)
    core.prepare_test(test=test, chemin_js=chemin_js)
    run(secured=secured, port=port, core=core)


def stop():
    """
    Arrêt du serveur
    """
    finish()


class Buffer:
    """
    Gestion de la sortie standard et de la sortie d'erreur
    """
    def __init__(self, text, main=True, outfile=None, stacksize=1000):
        """
        Constructeur
        @param text zone de texte
        @param main si sortie standard sinon sortie d'erreur
        @param outfile fichier de sortie ou None
        @param stacksize taille max. de la stacktrace
        """
        self.text = text
        self.file = None
        if main:
            self.stdout = sys.stdout
            self.stderr = sys.stderr
            sys.stdout = self
            sys.stderr = Buffer(
                text, main=False, outfile=outfile, stacksize=stacksize)
            if outfile is not None:
                self.file = open("%s.log" % outfile, "w")
        elif outfile is not None:
            self.file = open("%s.err" % outfile, "w")
        sys.tracebacklimit = stacksize
        self.text.tag_config("warn", foreground="red")
        self.main = main

    def write(self, st):
        """
        Ecrit
        @param st texte à ajouter
        """
        if self.main:
            self.text.insert(END, st)
        else:
            self.text.insert(END, st, "warn")
        if self.file is not None:
            self.file.write(st)

    def reset(self):
        """
        Nettoie la zone de texte
        """
        self.text.delete("1.0", END)
        if self.file is not None:
            self.file.flush()
        if self.main and sys.stderr.file is not None:
            sys.stderr.file.flush()

    def restore(self):
        """
        Libère la sortie standard et la sortie d'erreur
        """
        self.file2 = sys.stderr
        sys.stdout = self.stdout
        sys.stderr = self.stderr
        sys.tracebacklimit = 1000
        if self.file is not None:
            self.file.flush()
            self.file.close()
        if self.file2.file is not None:
            self.file2.file.flush()
            self.file2.file.close()


class App:
    """
    Application tkinter de Pyweb
    """
    def __init__(self, stacksize=1000):
        """
        Constructeur
        @param stacksize taille max. de la stacktrace
        """
        self.surv = None
        self.tk = Tk()
        self.tk.title("Pyweb server")
        self.tk.minsize(320, 50)
        self.top = Frame(self.tk)
        self.portl = Label(self.top, text="Port")
        self.portl.pack(side=LEFT, padx=5)
        self.portv = StringVar()
        self.portv.set("8080")
        self.port = Entry(self.top, text=self.portv, width=6)
        self.port.pack(side=LEFT, padx=5)
        self.secuv = IntVar()
        self.secu = Checkbutton(self.top, text="secured", variable=self.secuv)
        self.secu.pack(side=LEFT, padx=5)
        self.testv = IntVar()
        self.test = Checkbutton(self.top, text="test", variable=self.testv)
        self.test.pack(side=LEFT, padx=5)
        self.start = Button(self.top, text="start", command=self.cmd_start)
        self.start.pack(side=LEFT, padx=5)
        self.stop = Button(self.top, text="stop", command=self.cmd_stop)
        self.stop.pack(side=LEFT, padx=5)
        self.stop = Button(self.top, text="purge", command=self.cmd_purge)
        self.stop.pack(side=RIGHT, padx=5)
        self.top.pack(pady=10)
        self.text = ScrolledText(self.tk)
        self.text.pack(expand=1, fill=BOTH, pady=5)
        self.buffer = Buffer(
            self.text, main=True, stacksize=stacksize, outfile="run/pyweb")
        self.tk.geometry('{}x{}'.format(320, 50))
        self.tk.mainloop()
        self.buffer.restore()
        self.cmd_stop()

    def cmd_start(self):
        """
        Démarrage du serveur
        """
        if self.surv is None:
            self.surv = Surveillant()
            self.surv.start()
            try:
                def dem():
                    start(
                        secured=self.secuv.get() == 1,
                        port=int(self.portv.get()),
                        test=self.testv.get(),
                        chemin_js="www/test.js")
                threading.Thread(target=dem).start()
            except Exception as e:
                print("Exception au lancement du serveur", e)
                self.cmd_stop()

    def cmd_stop(self):
        """
        Arrêt du serveur
        """
        if self.surv is not None and self.surv.isactive:
            self.surv.isactive = False
            stop()
            self.surv = None

    def cmd_purge(self):
        """
        Remise à zéro de la zone de texte
        """
        self.buffer.reset()

if __name__ == "__main__":
    App(stacksize=1)
