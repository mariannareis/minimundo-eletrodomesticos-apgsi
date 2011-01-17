from should_dsl import should, should_not
import unittest
import specloud

from appliances_store import Product

class TestProduct(unittest.TestCase):
    def test_product_warranty(self):
        product = Product()
        product.warranty.has_key('date_of_purchase') |should| equal_to (True)
        product.warranty.has_key('mark') |should| equal_to (True)
        product.warranty.has_key('model') |should| equal_to (True)
        product.warranty.has_key('serial_number') |should| equal_to (True)

 #git commit -m 'created the basic structure of the Product with de Warranty'

