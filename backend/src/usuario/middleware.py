# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.api import users
from usuario.model import Usuario
import tmpl


def execute(next_process, handler, dependencies, **kwargs):
    usuario_google = users.get_current_user()
    if usuario_google:
        google_id = usuario_google.user_id()
        query = Usuario.query_by_google(google_id)
        usuario_logado = query.get()
        if not usuario_logado:
            usuario_logado = Usuario(nome=usuario_google.nickname(),
                                     email=usuario_google.email(),
                                     google_id=google_id)
            usuario_logado.put()
        logout_url = users.create_logout_url('/')
        dependencies["_usuario_logado"] = usuario_logado
        dependencies["_logout_url"] = logout_url
    else:
        dependencies["_usuario_logado"] = None
        dependencies["_login_url"] = users.create_login_url("/")

    next_process(dependencies, **kwargs)