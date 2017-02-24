#!/usr/bin/python3


"""
Module outil pour transformer la lecture d'une socket en lecture de tableau.
"""


class SocketReader():
    """
    La socket devient une liste.
    Stocke toutes les données lues.
    @warn A ne pas utiliser dans la déclaration d'une boucle.

    reader = SocketReader(socket)
    #lecture de 5 octets
    print (reader[:5])
    """
    def __init__(self: "SocketReader", sock: "socket"):
        """
        @param sock socket à lire en tant que tableau
        """
        self.__sock__ = sock
        self.__nb__ = 0
        self.__blist__ = []

    def __check__(self, pos):
        if self.__nb__ <= pos:
            b = list(self.__sock__.recv(1 + pos-self.__nb__))
            self.__blist__ += b
            self.__nb__ += len(b)

    def __getitem__(self, pos):
        if type(pos) == slice:
            self.__check__(pos.stop - 1)
            return self.__blist__[pos.start: pos.stop]
        else:
            self.__check__(pos)
            return self.__blist__[pos]
