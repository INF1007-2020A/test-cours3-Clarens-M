#!/usr/bin/env python
# -*- coding: utf-8 -*-
nom = str(input("Écrire le nom d'un pays: "))
def capitaliser_pays(nom):
    # TODO completer la fonction
    n = 1
    liste = [nom[i:i+n] for i in range(0, len(nom), n)]
    for i in range(0, len(nom), 1):
        if ord(liste[i]) > 96 and ord(liste[i]) < 123:
             cap = chr(ord(liste[i]) - 32)
             liste[i] = cap
    NOM = ''.join(liste)
    print(NOM)


if __name__ == '__main__':
    pays = [
        'AfghanIstan',
        'albania',
        'algeria',
        'AndorRa',
        'angolA',
        'antigua ANd barbuda',
        'argEntina',
        'Armenia',
        'austrAlia',
        'ausTria',
        'azerBaijaN'
    ]
    for i in range(len(pays)):
        pays[i] = capitaliser_pays(pays[i])

    print(pays)
