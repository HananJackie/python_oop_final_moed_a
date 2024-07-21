from order import Order


class RegularOrder(Order):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
