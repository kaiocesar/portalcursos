import jinja2
import os

_base = os.path.dirname(__file__)
_base = os.path.join(_base, 'web')
_jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader([_base]),
    trim_blocks=True,
    autoescape=True)


def render(template_name, values={}):
    template = _jinja_environment.get_template(template_name)
    return template.render(values)

