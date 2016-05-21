from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse

from jinja2 import Environment


def environment(**options):
    pyjade_extension = ['pyjade.ext.jinja.PyJadeExtension']
    env = Environment(extensions=pyjade_extension, **options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env