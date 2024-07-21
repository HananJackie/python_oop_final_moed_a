from customer import CustomerType
from order import Order


class VipOrder(Order):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def calculate_total_price(self):
        if self.order_customer.customer_type != CustomerType.VIP:
            raise ValueError("Only VIP customers can place VIP orders.")
        super().calculate_total_price()
        if self.order_customer.customer_discount is not None:
            self.order_total_price -= min(self.order_total_price, self.order_customer.customer_discount)