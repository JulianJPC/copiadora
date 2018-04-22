import os
from django.conf import settings


class Messages(object):
    def __init__(self, filename):
        """

        :param filename:
        """
        if not os.path.exists(filename):
            # Debe de existir el archivo
            raise IOError("No se puede encontrar el archivo de mensajes {archivo}.".format(archivo=filename))

        # Aca estan los mensajes
        self.__messages = {}

        # Abre el archivo de mensajes, los lee y los carga.
        messages_file = open(filename, "r")
        for line in messages_file.readlines():
            # Se skipea porque es un comentario
            line = line.strip()
            if len(line) == 0:
                continue
            if line[0] == '#':
                continue

            # Cada linea se separa por '='
            results = line.strip().split('=')

            # Si habia mas de 1 '=' entonces los demas son texto
            if len(results) > 2:
                key = str(results[0]).strip()
                value = "".join(['=' + v for v in results[1:]])[1:]
            else:
                # De lo contrario, se puede hacer esto
                key, value = results
                key = str(key).strip()

            # Si la key existe en el mapa, entonces se lanza un error
            if self.__messages.has_key(key):
                raise ValueError("El key '{key}' esta repetido en el archivo {archivo}.".format(
                    key=key,
                    archivo=filename
                ))

            # Se guarda la key y su valor
            self.__messages[key] = str(value).strip()

        # Se cierra el archivo
        messages_file.close()

    def get(self, key):
        """
        Devuelve el valor del mensaje buscado.

        :param key:
        :return:
        """
        return self.__messages.get(key)


# Objeto de mensajes para la capa Business
#MESSAGES_BUSINESS = Messages(settings.FILE_MESSAGES_BUSINESS)

# Objeto de mensajes para la capa de Persistence
#MESSAGES_PERSISTENCE = Messages(settings.FILE_MESSAGES_PERSISTENCE)

# Objeto de mensajes para la capa de Webservices
#MESSAGES_WEBSERVICES = Messages(settings.FILE_MESSAGES_WEBSERVICES)
