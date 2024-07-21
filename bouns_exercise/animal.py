from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, legs_n: int):
        self.__legs_number = legs_n

    def walk(self):
        print('Walking with {legs} legs'.format(legs=self.__legs_number))

    def eat(self):
        pass