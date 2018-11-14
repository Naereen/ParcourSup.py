#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" Candidat, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs : Lilian Besson, Bastien Trotobas et al, (C) 2018.
- Adresse : https://github.com/Naereen/ParcourSup.py
- Licence : MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas et al"
__version__ = "0.2"


class Candidat(object):
    """ Objet minuscule pour numéroter un candidat."""
    last_G_CN_COD = 1
    def __init__(self):
        self.G_CN_COD = self.last_G_CN_COD
        self.last_G_CN_COD += 1

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.G_CN_COD})"
