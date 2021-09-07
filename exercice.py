#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    return "".join([chr(ord(x)-32) for x in mot])


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

