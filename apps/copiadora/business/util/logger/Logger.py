import os

class Logger(object):
    """
        Logger hand-made.

        Esta clase esta pensada para funcionar como logger.
        Para configurar el logger, se necesita un archivo properties
        con la configuracion del mismo.
    """

    # Directorio raiz del usuario
    USER_BASE_DIR = os.path.expanduser("~")

    # Nombre del archivo de configuracion
    CONFIGURATION_FILE = "configuration.xml"

    def __init__(self):
        self.__configurar()

    def __read_properties(self):
        """
        Lee las configuraciones.

        :return:
        """
        props = {}
        f = open(Logger.CONFIGURATION_FILE, "r")
        lines = f.readlines()
        for line in lines:
            prop, val = line.strip().split("=")
            props[prop] = val
        f.close()
        return props

    def __configurar(self):
        """
        Busca la configuracion del Logger.

        :return:
        """
        try:
            if not os.path.exists(Logger.CONFIGURATION_FILE):
                raise IOError("El archivo de configuracion del logger no existe: " + Logger.CONFIGURATION_FILE)

            config = self.__read_properties()



        except Exception, e:
            raise e