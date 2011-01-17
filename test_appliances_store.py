from should_dsl import should, should_not
import unittest
import specloud

from appliances_store import Product, Customer

class TestPurchase(unittest.TestCase):
    pass

#"17/01/2011",
#product.warranty['date_of_purchase'] |should| equal_to ("17/01/2011")
#product.warranty['initial_customer'] |should| equal_to (1)

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

