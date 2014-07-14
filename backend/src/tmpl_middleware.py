# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import tmpl


def execute(next_process, handler, dependencies, **kwargs):
    def write_tmpl(template_name, values=None):

        dct = {'_usuario_logado': dependencies.get('_usuario_logado'),
               '_logout_url': dependencies.get('_logout_url'),
               '_login_url': dependencies.get('_login_url')}
        """
            Especificar um nível de filtragem apartir dessas variaveis acima.
        """

        # dct_pages  = {''}

        dct.update(values or {})
        return handler.response.write(tmpl.render(template_name, dct))

    dependencies["_write_tmpl"] = write_tmpl
    dependencies["_render"] = tmpl.render
    next_process(dependencies, **kwargs)
