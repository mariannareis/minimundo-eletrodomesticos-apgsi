import unittest
import sys
sys.path.append("/home/mari/mewe")

from store.models import ProductModel
from store.models import Brand
from should_dsl import should

class productModelTestCase(unittest.TestCase):

    def setUp(self):
        self.brand = Brand.objects.get(id=1)
        self.productmodel = ProductModel.objects.create(brand=self.brand, name="MV-33008")

    def it_verify_inclusion_of_a_product_model(self):
        self.productmodel.name |should| equal_to('DL-33006')
        self.productmodel.brand.name |should| equal_to('Dell')

