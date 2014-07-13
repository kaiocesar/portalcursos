# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from zen import router
from web.curso.rest import Curso


def index(_handler):
    _handler.redirect('/curso/rest/listar_html')

def add(_write_tmpl):
    url = router.to_path(salvar)
    dct = {'salvar_url':url}
    _write_tmpl('/templates/cursos/add.html', dct)


def salvar(_handler, nome, preco):
    preco = float(preco)
    curso = Curso(nome=nome, preco=preco)
    curso.put()
    path = router.to_path(index)
    _handler.redirect(path)
