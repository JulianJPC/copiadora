from __future__ import unicode_literals

import os
import sys
import datetime
from django.apps import AppConfig
from django.conf import settings


class CopiadoraConfig(AppConfig):
    # Nombre interno de la aplicacion
    name = 'copy'
 
    # Archivos estaticos, como JS, CSS, HTML, etc.
    static_root = os.path.join(os.sep, settings.STATIC_DIR, "copiadora")

    class Cookie:
        # Host del cookie
        host = 'kaiju.desa'

        # Session cookie key
        session_key = 'COPY_PYSID'

    # Mapa de las URL con su path de sistema
    static_dirs = {
        "/": os.path.join(os.sep, static_root, "html", "layout.html"),
        "js": os.path.join(os.sep, static_root, "js"),
        "favicon.ico": os.path.join(os.sep, static_root, "media", "favicon.ico"),
        "fonts": os.path.join(os.sep, static_root, "fonts"),
        "css": os.path.join(os.sep, static_root, "css"),
        "html": os.path.join(os.sep, static_root, "html"),
        "media": os.path.join(os.sep, static_root, "media"),
    }

    # Templates de errores html
    templates_dir = os.path.join(os.sep, settings.RESOURCES_DIR, "copiadora", "templates")