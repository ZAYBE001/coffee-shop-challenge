class Customer:
    def __init__(self, name):
        self._name = None
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        return self._orders

    def coffees(self):
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee")
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee")
        customers = {order.customer for order in coffee.orders()}
        if not customers:
            return None
        return max(customers, key=lambda customer: sum(order.price for order in customer.orders if order.coffee == coffee))


class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string with at least 3 characters.")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders

    def customers(self):
        return list({order.customer for order in self._orders})

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        return sum(order.price for order in self._orders) / len(self._orders)