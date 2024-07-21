from overrides import override

from animal import Animal
from pet import Pet


class Cat(Animal, Pet):
    CAT_LEGS_NUMBER = 4
    GENERIC_CAT_NAME = 'Cat'

    def __init__(self, name: str = GENERIC_CAT_NAME):
        super().__init__(Cat.CAT_LEGS_NUMBER)
        self.__name = name

    @override
    def get_name(self):
        return self.__name

    @override
    def set_name(self, name: str):
        self.__name = name

    @override
    def play(self):
        print('{name} the cat is playing'.format(name=self.__name))

    @override
    def eat(self):
        print('{name} the cat is eating'.format(name=self.__name))
