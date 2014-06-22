# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from zen import router

def index(_handler):
    path=router.to_path(form, "kaio", "bruna")
    _handler.redirect(path)


def form(_resp, nome, sobrenome):
    _resp.write("ola %s %s" %(nome, sobrenome))
