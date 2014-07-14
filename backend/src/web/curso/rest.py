# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from google.appengine.ext import ndb

class Curso(ndb.Model):
    nome = ndb.StringProperty()
    preco = ndb.FloatProperty()

def salvar(nome, preco):
    preco = float(preco)
    curso = Curso(nome=nome, preco=preco)
    curso.put()

def to_dict(c):
        dct = c.to_dict()
        dct['id'] = str(c.key.id())
        return dct

def listar(_resp):
    query = Curso.query().order(-Curso.preco)
    cursos = [to_dict(c) for c in query.fetch()]
    cursos = json.dumps(cursos)
    _resp.write(cursos)

def listar_html(_write_tmpl):
    query = Curso.query().order(Curso.preco)
    cursos = [to_dict(c) for c in query.fetch()]
    _write_tmpl("templates/cursos/listagem.html", {'cursos':cursos})


def editar(nome, preco):
    pass