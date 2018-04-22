from django.conf import settings
from json import JSONEncoder


class WmJsonEncoder(JSONEncoder):
    """

    """
    def default(self, o):
        """

        :param o:
        :return:
        """
        return o.__dict__