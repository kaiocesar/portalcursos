# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest
from base import GAETestCase
from web.curso import rest
from web.curso.rest import Curso

class RestTests(GAETestCase):
    def test_salvar(self):
        rest.salvar("Python para newbies", around(189.10))                                                                                                                                                                                                                              
        lista=Curso.query().fetch()
        self.assertEquals(1, len(lista))
        curso=lista[0]
        self.assertEquals("Python para newbies", curso.nome)
        self.assertEquals("189.10", curso.preco)

    def test_listar(self):
        curso=[Curso("Python para newbies","189.10"),
               Curso("Python para Hackers","399,70")]
