from overrides import override
from animal import Animal


class Spider(Animal):
    SPIDER_LEGS_NUMBER = 8

    def __init__(self):
        super().__init__(Spider.SPIDER_LEGS_NUMBER)

    @override
    def eat(self):
        print('Spider is eating')
