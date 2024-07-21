from datetime import datetime
from regular_order import RegularOrder
from vip_order import VipOrder
from order_item import OrderItem
from customer import Customer, CustomerType
from order import PaymentType
from wine_opener import WineOpener

# Create customers
customer1 = Customer(1, 'John', 'Doe', 'john_doe@email.com', '123 St', CustomerType.REGULAR, None)
customer2 = Customer(2, 'Jane', 'Doe', 'jane_doe@blackpearl.com', '456 St', CustomerType.VIP, 100)

# Create items
item1 = OrderItem(1, 'Laptop', 1000)
item2 = OrderItem(2, 'Mouse', 50)
item3 = OrderItem(3, 'Keyboard', 100)
item4 = OrderItem(4, 'Monitor', 200)
item5 = OrderItem(5, 'Speakers', 150)

# Create orders
order1 = RegularOrder(1, 'order 1', [item1, item2], customer1, PaymentType.CREDIT_CARD, datetime.now().strftime('%Y-%m-%d'))
print('order 1 total price: {}'.format(order1.order_total_price))
print('order 1 delivery address: "{}"'.format(order1.delivery_address))
print('customer 1 favourite items: {}'.format([item.item_name for item in customer1.favorite_items]))

order2 = VipOrder(2, 'order 2', [item3, item4, item5], customer2, PaymentType.CASH, datetime.now().strftime('%Y-%m-%d'))
print('order 2 total price: {}'.format(order2.order_total_price))
print('order 2 delivery address: "{}"'.format(order2.delivery_address))
print('customer 2 favourite items: {}'.format([item.item_name for item in customer2.favorite_items]))
try:
    order3 = VipOrder(3, 'order 3', [item1, item2, item4], customer1, PaymentType.CHECK, datetime.now().strftime('%Y-%m-%d'))
except ValueError as e:
    print('Warning! {msg}'.format(msg=str(e)))
print('customer 1 favourite items: {}'.format([item.item_name for item in customer1.favorite_items]))

# Success Test gifts
print('Testing gifts:')
gift = WineOpener()
print('john Doe gift: {gift}'.format(gift=customer1.customer_gift))
customer1.take_gift(gift)
print('john Doe gift: {gift}'.format(gift=customer1.customer_gift))
customer1.open_gift()
