# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from zen import router

def form(_write_tmpl):
    path=router.to_path(salvar)
    dct={'salvar_curso'}
    _write_tmpl('/templates/curso_form.html',dct)


def salvar():
    pass
