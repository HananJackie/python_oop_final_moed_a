class OrderItem:
    order_items_ids = []

    def __init__(self, item_id, item_name, item_price):
        if item_id not in OrderItem.order_items_ids:
            self.__id = item_id
            self.__item_name = item_name
            self.__item_price = item_price
            OrderItem.order_items_ids.append(self.__id)
        else:
            raise ValueError('Order item id {id} already exists in the database'.format(id=item_id))

    @property
    def id(self):
        return self.__id

    @property
    def item_name(self):
        return self.__item_name

    @property
    def item_price(self):
        return self.__item_price

