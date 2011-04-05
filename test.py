import unittest
from store.models import Customer

class CustomerTestCase(unittest.TestCase):
    def setUp(self):
        self.mari = Customer.objects.create(name="marianna", address="casa de mari")
        self.ruhan = Customer.objects.create(name="ruhan", address="casa de ruhan")

    def testSpeaking(self):
        self.assertEquals(self.mari.address, 'casa de mari')
        self.assertEquals(self.ruhan.name, 'ruhan')

