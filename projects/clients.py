class Client:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if not isinstance(age, int):
            print('Неподходящий тип данных')
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not isinstance(name, str):
            print('Неподходящий тип данных')
        self.__name = name

    def get_surname(self):
        return self.__surname

    def set_surname(self, surname):
        if not isinstance(surname, str):
            print('Неподходящий тип данных')
        self.__surname = surname


class ClientProperty:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            print('Неподходящий тип данных')
        self.__name = new_name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, new_surname):
        if not isinstance(new_surname, str):
            print('Неподходящий тип данных')
        self.__surname = new_surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int):
            print('Неподходящий тип данных')
        self.__age = new_age


if __name__ == '__main__':
    client1 = Client('Вова', 'Капустин', 21)
    print(f'Имя клиента: {client1.get_name()}, фамилия: {client1.get_surname()}, возраст: {client1.get_age()}')
    client1.set_name('Никита')
    print('После изменения имени:')
    print(f'Имя клиента: {client1.get_name()}, фамилия: {client1.get_surname()}, возраст: {client1.get_age()}\n')

    client2 = ClientProperty('Леша', 'Салатов', 24)
    print(f'Имя клиента: {client2.name}, фамилия: {client2.surname}, возраст: {client2.age}')
    client2.surname = 'Ложкин'
    print('После изменения фамилии:')
    print(f'Имя клиента: {client2.name}, фамилия: {client2.surname}, возраст: {client2.age}')
