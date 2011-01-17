from should_dsl import should, should_not
import unittest
import specloud

from appliances_store import Product, Customer, Purchase

class TestProduct(unittest.TestCase):

    def test_add_a_product(self):
        product = Product(1, "Arno", "MD-001", "SN-3122")
        product.warranty['id']|should| equal_to (1)
        product.warranty['mark'] |should| equal_to ("Arno")
        product.warranty['model'] |should| equal_to ("MD-001")
        product.warranty['serial_number'] |should| equal_to ("SN-3122")

class TestCustomer(unittest.TestCase):
    def test_add_a_costumer(self):
        customer = Customer(1, "Paula", "Casa Da Paula")
        customer.id |should| equal_to (1)
        customer.name |should| equal_to ("Paula")
        customer.address |should| equal_to ("Casa Da Paula")

class TestPurchase(unittest.TestCase):
    def test_making_a_purchase(self):
        purchase = Purchase(1, 1, "17/01/2011") #id, customer, date_of_purchase
        purchase.id |should| equal_to (1)
        purchase.customer |should| equal_to(1)
        purchase.date |should| equal_to ("17/01/2011")

