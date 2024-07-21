from enum import Enum
from typing import Optional, List
from gift import Gift
from order_item import OrderItem


class CustomerType(Enum):
    REGULAR = 'Regular'
    VIP = 'VIP'


class Customer:
    customers_ids = []

    def __init__(self, customer_id, first_name, last_name, email, delivery_address, customer_type, customer_discount):
        if customer_id not in Customer.customers_ids:
            self.__id = customer_id
            self.__first_name = first_name
            self.__last_name = last_name
            self.__email = email
            self.__delivery_address = delivery_address
            self.__customer_type = customer_type
            self.__customer_discount = customer_discount
            self.__favorite_items = []
            self.__customer_gift = None
            Customer.customers_ids.append(self.__id)
        else:
            raise ValueError('Customer id {id} already exists in the database'.format(id=customer_id))

    @property
    def id(self):
        return self.__id

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def email(self):
        return self.__email

    @property
    def delivery_address(self):
        return self.__delivery_address

    @property
    def customer_type(self):
        return self.__customer_type

    @property
    def customer_discount(self):
        return self.__customer_discount

    @property
    def favorite_items(self):
        return self.__favorite_items

    @property
    def customer_gift(self):
        return self.__customer_gift

    def add_to_favorites(self, items):
        self.__favorite_items += [item for item in items if item.item_name not in [item.item_name for item in self.__favorite_items]]

    def remove_from_favorites(self, items):
        self.__favorite_items = [item for item in self.__favorite_items if item.item_name not in [item.name for item in items]]

    def take_gift(self, gift):
        self.__customer_gift = gift

    def open_gift(self):
        if self.__customer_gift:
            self.__customer_gift.open_gift()
