#!/usr/bin/python3


"""
Gestion des trames Websockets (RFC 6455)

Méthodes à utiliser:
    websocket_headers
    readMessage
    writeMessage
"""


from mapper import SocketReader
from base64 import b64encode
from hashlib import sha1


CST_GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
CST_MASK = 128
CST_FIN = 128
MAP_OPCODE_4 = {
    0: "CONT",
    "CONT": 0,
    1: "TEXT",
    "TEXT": 1,
    2: "BIN",
    "BIN": 2,
    8: "CLOSED",
    "CLOSED": 8,
    9: "PING",
    "PING": 9,
    10: "PONG",
    "PONG": 10
}


def websocket_headers(headers):
    """
    Construit les entêtes pour un accord d'ouverture de la websocket
    @param headers entêtes HTTP pour récupérer Sec-WebSocket-Key
    @return dictionnaire des entêtes pour une réponse positive
    """
    rec_key = headers["Sec-WebSocket-Key"]
    key = str(
        b64encode(sha1(bytes(rec_key + CST_GUID, "utf-8")).digest()),
        "utf-8")
    hs = {
        'Upgrade': 'websocket',
        'Connection': 'Upgrade',
        'Sec-WebSocket-Accept': key,
        'Sec-WebSocket-Version-Server': '13',
        'Sec-WebSocket-Extensions': ''}
    return hs


def bvalid(val, mask):
    """
    Vérifie que la valeur correspond au masque
    @param val valeur à vérifier
    @param mask masque binaire
    @return égalité
    """
    return (val & mask) == mask


def padd(array, value):
    """
    Additionne la valeur dans le tableau [fort, faible]
    @param array tableau à renseigner
    @param value valeur à additionner
    @return le tableau
    """
    maxi = len(array)
    for i in range(0, maxi):
        array[maxi - 1 - i] += value % 256
        value = value // 256
    return array


def depad(array):
    """
    Récupère la valeur depuis un tableau [fort, faible]
    @param array tableau à lire
    @return le nombre calculé
    """
    value = 0
    maxi = len(array)
    for i in range(0, maxi):
        value = value * 256 + array[i]
    return value


def toTextPayload(
    text,
    mask=[],
    encoding="utf-8",
    toClose=False,
    toPing=False,
    toPong=False
):
    """
    Construit une trame websocket (RFC 6455)
    @param text texte à envoyer
    @param mask masque
    @param encoding encodage
    @param toClose à fermer
    @param toPing ping
    @param toPong pong
    @return message binaire
    """
    controle = CST_FIN + MAP_OPCODE_4['TEXT']
    if toClose:
        controle += MAP_OPCODE_4['CLOSED']
    if toPing:
        controle += MAP_OPCODE_4['PING']
    if toPong:
        controle += MAP_OPCODE_4['PONG']
    controle = [controle]
    if len(text) > 125 and (toClose or toPing or toPong):
        raise Exception("Message to long for cloasing")
    taille = len(text)
    masque = 0
    if len(mask) == 4:
        masque = CST_MASK
    longueur7 = 0
    ll = []
    if taille < 126:
        longueur7 = masque + taille
    elif taille > 65535:
        longueur7 = masque + 127
        ll = padd([0, 0, 0, 0, 0, 0, 0, 0], taille)
    else:
        longueur7 = masque + 126
        ll = padd([0, 0], taille)
    longueur = [longueur7] + ll
    payload = list(bytes(text, encoding))
    message = None
    if masque == CST_MASK:
        for i in range(0, taille):
            payload[i] = payload[i] ^ mask[i % 4]
        message = controle + longueur + mask + payload
    else:
        message = controle + longueur + payload
    return bytes(message)


def fromMessage(buffer):
    """
    Décode une trame websocket (RFC 6455).
    @param buffer trame à lire (sous la forme d'un tableau)
    @return message {data, fin:trame de fin, closed:fermeture, ping}
    """
    is_fin = bvalid(buffer[0], CST_FIN)
    # is_cont = bvalid(buffer[0], MAP_OPCODE_4["CONT"])
    is_text = bvalid(buffer[0], MAP_OPCODE_4["TEXT"])
    # is_bin = bvalid(buffer[0], MAP_OPCODE_4["BIN"])

    is_clo = bvalid(buffer[0], MAP_OPCODE_4["CLOSED"])
    is_in = bvalid(buffer[0], MAP_OPCODE_4["PING"])
    is_out = bvalid(buffer[0], MAP_OPCODE_4["PONG"])

    is_mask = bvalid(buffer[1], CST_MASK)

    offset = 2
    longu = buffer[1] & 127
    if longu == 126:
        longu = depad(buffer[2:4])
        offset = 4
    elif longu == 127:
        longu = depad(buffer[2:11])
        offset = 11

    mask = []
    if is_mask:
        mask = buffer[offset:offset + 4]
        offset += 4

    payload = buffer[offset:offset + longu]
    if is_mask:
        for i in range(0, longu):
            payload[i] = payload[i] ^ mask[i % 4]

    payload = bytes(payload)
    if is_text:
        payload = str(payload, "utf-8")
    return {
        "data": payload,
        "fin": is_fin,
        "closed": is_clo,
        "ping": is_in
    }


def readMessage(sock):
    """
    Lit un message depuis la socket
    @param sock la socket à lire
    @return message {data, fin:trame de fin, closed:fermeture, ping}
    """
    mapp = SocketReader(sock)
    ret = fromMessage(mapp)
    del mapp
    return ret


def writeMessage(
    sock,
    text,
    mask=[],
    encoding="utf-8",
    toClose=False,
    toPing=False,
    toPong=False
):
    """
    Ecrit un message et l'envoie vers la socket
    @param sock la socket
    @param text texte à transmettre
    @param mask masque
    @param encoding encodage
    @param toClose fermeture
    @param toPing ping
    @param toPong pong
    """
    ret = toTextPayload(
        text,
        mask=mask,
        encoding=encoding,
        toClose=toClose,
        toPing=toPing,
        toPong=toPong)
    sock.send(ret)


if __name__ == "__main__":
    import binascii
    import sys
    text = sys.argv[-1]
    print(binascii.hexlify(toTextPayload(text, mask=[])))
    print(fromMessage(list(toTextPayload(
        text,
        mask=[0x37, 0xfa, 0x21, 0x3d],
        toClose=True))))
