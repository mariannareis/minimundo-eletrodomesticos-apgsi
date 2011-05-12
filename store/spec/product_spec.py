import unittest
import sys
sys.path.append("/home/mari/mewe")

from store.models import ProductModel
from store.models import Product
from should_dsl import should

class productTestCase(unittest.TestCase):

    def setUp(self):
        self.productmodel = ProductModel.objects.get(id=3)
        self.product = Product.objects.create(product_model=self.productmodel, serial_number="019823")

    def it_verify_inclusion_of_a_product(self):
        self.product.product_model.name |should| equal_to('um exemplo')
        self.product.serial_number |should| equal_to("019823")
        self.product.product_model.brand.name |should| equal_to('Dell')
        self.product.unit |should| equal_to('unit')

