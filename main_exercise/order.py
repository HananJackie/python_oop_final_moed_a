from abc import ABC, abstractmethod
from enum import Enum


class PaymentType(Enum):
    CREDIT_CARD = 'Credit Card'
    CASH = 'Cash'
    CHECK = 'Check'
    OTHER = 'Other'


class Order(ABC):
    orders_ids = []

    @abstractmethod
    def __init__(self, order_id, order_name, order_items, order_customer, payment_type, order_date):
        if order_id not in Order.orders_ids:
            self.__id = order_id
            self.__name = order_name
            self.__delivery_address = order_customer.delivery_address
            self.__order_items = order_items
            self.__order_customer = order_customer
            self.__payment_type = payment_type
            self.__order_date = order_date
            self.__order_total_price = 0
            self.calculate_total_price()
            order_customer.add_to_favorites(order_items)
            Order.orders_ids.append(self.__id)
        else:
            raise ValueError('Order id {id} already exists in the database')

    def calculate_total_price(self):
        self.__order_total_price = sum(item.item_price for item in self.__order_items)

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def delivery_address(self):
        return self.__delivery_address

    @property
    def order_items(self):
        return self.__order_items

    @property
    def order_customer(self):
        return self.__order_customer

    @property
    def order_total_price(self):
        return self.__order_total_price

    @order_total_price.setter
    def order_total_price(self, order_total_price):
        self.__order_total_price = order_total_price

    @property
    def payment_type(self):
        return self.__payment_type

    @property
    def order_date(self):
        return self.__order_date
