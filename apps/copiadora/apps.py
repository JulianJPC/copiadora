from __future__ import unicode_literals

import os
import sys
import datetime
from django.apps import AppConfig
from django.conf import settings
from copiadora.business.util.Util import Messages


class CopiadoraConfig(AppConfig):
    # Nombre interno de la aplicacion
    name = 'copy'

    # TODO: hacerlo parametrizado mediante un archivo properties en el resources.
    # Archivo donde va a guardar los logs
    logger_output = os.path.join(os.sep, settings.RESOURCES_DIR, "copiadora", "logger", "copiadora-System-Output.log")

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

    class messages:
        # Mensajes de Business
        business = Messages(os.path.join(settings.RESOURCES_DIR, "copiadora", "messages", "business.properties"))

        # Mensajes de Persistence
        persistence = Messages(os.path.join(settings.RESOURCES_DIR, "copiadora", "messages", "persistence.properties"))

        # Mensajes de Webservices
        webservices = Messages(os.path.join(settings.RESOURCES_DIR, "copiadora", "messages", "webservices.properties"))

class Logger(object):
    """
        Logger interno de la aplicacion.

    """
    def __init__(self, name, loggerfile, app):
        self.filename = name
        self.format = "[{date}] - {level} - {app} - {log}\r\n"
        self.logger_file = loggerfile
        self.app = app

    def error(self, log):
        self.__log('ERROR', log)

    def info(self, log):
        self.__log('INFO', log)

    def warning(self, log):
        self.__log('WARNING', log)

    def __log(self, level, log):
        exc_type, exc_obj, exc_tb = sys.exc_info()

        if os.path.exists(self.logger_file):
            mode = "ab+"
        else:
            mode = "wb"

        with open(self.logger_file, mode) as logfile:
            if exc_type is None or exc_obj is None or exc_tb is None:
                logtext = "{logtext}".format(logtext=log)
            else:
                logtext = "{logtext}\r\nAt: {filename} - {ln} line.".format(logtext=log, ln=exc_tb.tb_lineno, filename=self.filename)
            formatted = self.format.format(
                date=datetime.datetime.now(),
                level=level,
                app=self.app,
                log=logtext
            )
            logfile.write(formatted)

            if settings.DEBUG:
                sys.stdout.write(formatted)
                if level == 'WARNING' or level == 'ERROR':
                    sys.stderr.write(formatted)


class LoggerFactory(object):
    @staticmethod
    def get_logger(name):
        if not name:
            raise ValueError("El logger necesita un nombre de archivo.")
        return Logger(name, CopiadoraConfig.logger_output, CopiadoraConfig.name)
