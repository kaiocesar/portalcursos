# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from google.appengine.ext import ndb
from mock import Mock
from base import GAETestCase
from web.curso import rest
from web.curso.rest import Curso


class RestTests(GAETestCase):
    def test_salvar(self):
        rest.salvar('Curso 2 de Angular.JS','155.90')
        lista = Curso.query().fetch()
        self.assertEqual(1, len(lista))
        curso = lista[0]
        self.assertEqual('Curso 2 de Angular.JS', curso.nome)
        self.assertEqual(155.90, curso.preco)

    def test_listar(self):
        cursos = [Curso(nome='Curso de Python para quem sabe python',preco=179.49),
                  Curso(nome='Angular.JS para que e fron-end Ninja',preco=899.34)]

        ndb.put_multi(cursos)
        resp = Mock()
        rest.listar(resp)
        resp.write.assert_called_once_with('[{"preco": 899.34, "id": "2", "nome": "Angular.JS para que e fron-end Ninja"}, {"preco": 179.49, "id": "1", "nome": "Curso de Python para quem sabe python"}]')