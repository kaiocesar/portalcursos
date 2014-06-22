# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb

# atalho alt + enteder para importar
class Curso(ndb.Model):
    nome=ndb.StringProperty()
    preco=ndb.FloatProperty()

#http://127.0.0.1:8080/curso/rest/salvar?nome=PythonParaQuemEstudouCSharp&preco=120.90
def salvar(nome, preco):
    preco=float(preco)
    curso=Curso(nome=nome, preco=preco)
    curso.put()

#http://127.0.0.1:8080/curso/rest/listar
def listar(_resp):
    query=Curso.query().order(-Curso.nome)
    # order by asc query=Curso.query().order(-Curso.nome)
    # order by desc query=Curso.query().order(Curso.nome)
    # lista_cursos=query.fetch()

    def to_dict(c):
        dct=c.to_dict()
        dct['id']=str(c.key.id())
        return dct

    lista_cursos= [to_dict(c) for c in query.fetch()]
    jsontxt= Json.dumps(lista_cursos)

    _resp.write(jsontxt)