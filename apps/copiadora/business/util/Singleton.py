class Singleton(object):
    """
        Singleton decorator.
    """
    def __init__(self, decorated):
        self.__decorated = decorated

    def get_instance(self):
        """
        Get the instance-object of the decorated class.

        :return: the instance of the decorated class
        """
        try:
            return self.__instance
        except AttributeError, ae:
            self.__instance = self.__decorated()
            return self.__instance

    def __call__(self, *args, **kwargs):
        """
        Singleton forbids the call access to the decorated class.
        So, to get an instances, you have to use the 'get_instance' method.

        :param args:
        :param kwargs:
        :return:
        """
        raise TypeError("Singleton access forbbiden: must use method 'get_instance'.")

    def __instancecheck__(self, inst):
        """
        Check if the object 'inst' is an instance of the decorated class.

        :param inst:
        :return:
        """
        return isinstance(inst, self.__decorated)