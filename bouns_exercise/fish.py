from overrides import override

from animal import Animal
from pet import Pet


class Fish(Animal, Pet):
    FISH_LEGS_NUMBER = 0
    GENERIC_FISH_NAME = 'Fish'

    def __init__(self):
        super().__init__(Fish.FISH_LEGS_NUMBER)
        self.__name = Fish.GENERIC_FISH_NAME

    @override
    def get_name(self):
        return self.__name

    @override
    def set_name(self, name: str):
        self.__name = name

    @override
    def play(self):
        print('{name} the fish is playing'.format(name=self.__name))

    @override
    def walk(self):
        print('{name} the fish is swimming'.format(name=self.__name))

    @override
    def eat(self):
        print('{name} the fish is eating'.format(name=self.__name))
