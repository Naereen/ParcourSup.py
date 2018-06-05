#!/usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" AlgoOrdreAppelEntree, pour https://github.com/Naereen/ParcourSup.py.

- Auteurs: Lilian Besson, Bastien Trotobas and contributors, (C) 2018.
- Adresse: https://github.com/Naereen/ParcourSup.py
- Licence: MIT License (http://lbesson.mit-license.org).
"""
__author__ = "Lilian Besson, Bastien Trotobas and contributors"
__version__ = "0.0.1"

from lxml import etree
from os import path
import json

class AlgoOrdreAppel(object):

    def __init__(self, groupesClassements):
        self.groupesClassements = groupesClassements
        self.ordresAppel = dict()

    def calculeOrdresAppels(self):
        for ga in self.groupesClassements:
            self.ordresAppel[ga.C_GP_COD] = ga.calculeOrdreAppels()
