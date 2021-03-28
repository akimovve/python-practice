class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.__surname = surname
        self.__age = age

    def get_info(self):
        return 'Name: {} {}\nAge: {}'.format(str(self.name),
                                             str(self.__surname),
                                             str(self.__age))
