import unittest
from models import Customer

class TestCustomer(unittest.TestCase):
    def test_name_property(self):
        customer = Customer("Alice")
        self.assertEqual(customer.name, "Alice")
        
        with self.assertRaises(ValueError):
            customer.name = "A" * 16
        with self.assertRaises(ValueError):
            customer.name = ""
        with self.assertRaises(ValueError):
            customer.name = 123

    def test_orders(self):
        customer = Customer("Bob")
        self.assertEqual(customer.orders(), [])

    def test_coffees(self):
        customer = Customer("Charlie")
        self.assertEqual(customer.coffees(), [])

    def test_create_order(self):
        customer = Customer("David")
        coffee = Coffee("Espresso")
        order = customer.create_order(coffee, 5.0)
        self.assertIn(order, customer.orders())
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 5.0)

    def test_most_aficionado(self):
        coffee = Coffee("Latte")
        alice = Customer("Alice")
        bob = Customer("Bob")
        alice.create_order(coffee, 5.0)
        alice.create_order(coffee, 5.0)
        bob.create_order(coffee, 3.0)
        self.assertEqual(Customer.most_aficionado(coffee), alice)

if __name__ == '__main__':
    unittest.main()