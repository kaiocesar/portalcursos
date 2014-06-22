# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest
from google.appengine.ext import ndb
from base import GAETestCase
from web.curso import rest
from web.curso.rest import Curso
from decimal import Decimal
from mock import Mock


class RestTests(GAETestCase):
    def test_salvar(self):
        rest.salvar("Python para newbies", round(189.10,2))
        lista=Curso.query().fetch()
        self.assertEquals(1, len(lista))
        curso=lista[0]
        self.assertEquals("Python para newbies", curso.nome)
        self.assertEquals(189.10, curso.preco)

    def test_listar(self):
        cursos=[Curso(nome="Python para newbies", preco=189.10),
               Curso(nome="Python para Hackers",preco=399.70)]
        ndb.put_multi(cursos)
        resp=Mock()
        resp.listar(resp)
        # resp.assert_called_once_with('[{"preco":189.10, "id":1, "nome": "Python para newbies"}]')
