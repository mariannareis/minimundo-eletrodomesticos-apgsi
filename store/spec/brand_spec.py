import unittest
import sys
sys.path.append("/home/mari/mewe")

from store.models import Brand
from should_dsl import should

class brandTestCase(unittest.TestCase):

    def setUp(self):
        self.brand = Brand.objects.create(name="Dell")

    def it_verify_inclusion_of_a_brand(self):
        self.brand.name |should| equal_to('Dell')

