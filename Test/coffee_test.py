import unittest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):
    def test_name_property(self):
        coffee = Coffee("Cappuccino")
        self.assertEqual(coffee.name, "Cappuccino")
        
        with self.assertRaises(ValueError):
            Coffee("C")
        with self.assertRaises(ValueError):
            Coffee("")

    def test_orders(self):
        coffee = Coffee("Americano")
        self.assertEqual(coffee.orders(), [])

    def test_customers(self):
        coffee = Coffee("Mocha")
        self.assertEqual(coffee.customers(), [])

    def test_num_orders(self):
        coffee = Coffee("Flat White")
        self.assertEqual(coffee.num_orders(), 0)
        customer = Customer("Eve")
        customer.create_order(coffee, 4.5)
        self.assertEqual(coffee.num_orders(), 1)

    def test_average_price(self):
        coffee = Coffee("Macchiato")
        self.assertEqual(coffee.average_price(), 0)
        customer1 = Customer("Frank")
        customer2 = Customer("Grace")
        customer1.create_order(coffee, 3.5)
        customer2.create_order(coffee, 4.5)
        self.assertEqual(coffee.average_price(), 4.0)

if __name__ == '__main__':
    unittest.main()