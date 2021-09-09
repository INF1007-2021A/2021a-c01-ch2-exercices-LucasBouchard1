#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    nv_mot = ""
    for lettre in mot:
        ord_ = ord(lettre)
        if 96<ord_<123:
            nv_mot += chr(ord_-32)
        else:
            nv_mot += lettre
    return nv_mot



if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)

