# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from zen import router


def index(_resp):
    _resp.write("Hello ZenWarch")

def redirecionar(_handler):
    path = router.to_path(formulario, "Kaio", "cesar")
    _handler.redirect(path)

def formulario(_resp, nome, sobrenome):
    _resp.write("Hello %s %s" % (nome, sobrenome))
