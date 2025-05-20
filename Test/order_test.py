import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def test_order_initialization(self):
        customer = Customer("Hannah")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 5.0)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 5.0)

    def test_order_price_immutable(self):
        customer = Customer("Ian")
        coffee = Coffee("Espresso")
        order = Order(customer, coffee, 5.0)
        with self.assertRaises(AttributeError):
            order.price = 6.0

    def test_order_customer_immutable(self):
        customer = Customer("Jack")
        coffee = Coffee("Americano")
        order = Order(customer, coffee, 5.0)
        with self.assertRaises(AttributeError):
            order.customer = Customer("Jill")

    def test_order_coffee_immutable(self):
        customer = Customer("Kate")
        coffee = Coffee("Cappuccino")
        order = Order(customer, coffee, 5.0)
        with self.assertRaises(AttributeError):
            order.coffee = Coffee("Mocha")

if __name__ == '__main__':
    unittest.main()