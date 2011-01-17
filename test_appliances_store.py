from should_dsl import should, should_not
import unittest
import specloud

from appliances_store import Product, Customer, Purchase

class TestProduct(unittest.TestCase):

    def test_add_a_product(self):
        self.product = Product(1, "Arno", "MD-001", "SN-3122")
        self.product.id |should| equal_to (1)
        self.product.mark |should| equal_to ("Arno")
        self.product.model |should| equal_to ("MD-001")
        self.product.serial_number |should| equal_to ("SN-3122")

class TestCustomer(unittest.TestCase):

    def test_add_a_costumer(self):
        self.customer = Customer(1, "Paula", "Casa Da Paula")
        self.customer.id |should| equal_to (1)
        self.customer.name |should| equal_to ("Paula")
        self.customer.address |should| equal_to ("Casa Da Paula")

class TestPurchase(unittest.TestCase):
    def test_making_a_purchase(self):
        self.purchase = Purchase(1, 1, "17/01/2011") #id, customer, date_of_purchase
        self.purchase.id |should| equal_to (1)
        self.purchase.customer |should| equal_to(1)
        self.purchase.date |should| equal_to ("17/01/2011")
        self.purchase.add_product(1)
        self.purchase.add_product(1)
        self.purchase.products |should| equal_to([1, 1])

    def test_a_purchase_in_the_warranty(self):
        self.purchase = Purchase(1, 1, "17/01/2010") #id, customer, date_of_purchase
        self.purchase.id |should| equal_to (1)
        self.purchase.customer |should| equal_to(1)
        self.purchase.date |should| equal_to ("17/01/2010")
        self.purchase.add_product(1)
        self.purchase.add_product(1)
        self.purchase.products |should| equal_to([1, 1])
        self.purchase.is_my_purchase_in_the_warranty(1) |should| equal_to(True)



#class Exchange():
#    pass


#class ProductStorage():
#    pass

