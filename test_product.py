from should_dsl import should, should_not
import unittest
import specloud

from appliances_store import Product, Customer

class TestProduct(unittest.TestCase):
    def test_product_warranty(self):
        product = Product()
        product.warranty.has_key('date_of_purchase') |should| equal_to (True)
        product.warranty.has_key('mark') |should| equal_to (True)
        product.warranty.has_key('model') |should| equal_to (True)
        product.warranty.has_key('serial_number') |should| equal_to (True)


class TestCostumer(unittest.TestCase):
    def test_costumer_data(self):
        customer = Customer(1, "Paula", "Casa Da Paula")
        customer.id |should| equal_to (1)
        customer.name |should| equal_to ("Paula")
        customer.address |should| equal_to ("Casa Da Paula")

