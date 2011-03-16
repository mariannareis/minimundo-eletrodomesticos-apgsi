from should_dsl import should, should_not
import unittest
import specloud
from datetime import date

from appliances_store import Storage, Customer, Purchase, Exchange

class TestStorage(unittest.TestCase):

    def test_add_products(self):                                                 #adiciona um produto
        self.storage = Storage()
        self.storage.add_products("Arno", "MD-001", 3)
        self.storage.mark |should| equal_to ("Arno")
        self.storage.model |should| equal_to ("MD-001")
        self.storage.set_products_serials(["SD-2233", "SD-4444", "SD-5566"])
        len(self.storage.products_serials) |should| equal_to (3)
        self.storage.products_by_type[0].products_serials |should| equal_to (['SD-2233', 'SD-4444', 'SD-5566'])
        self.storage.products_by_type[0].mark |should| equal_to ('Arno')

class TestCustomer(unittest.TestCase):

    def test_add_one_customer(self):                                                #adiciona um cliente
        self.customer = Customer(1, "Paula", "Casa Da Paula")
        self.customer.id |should| equal_to (1)
        self.customer.name |should| equal_to ("Paula")
        self.customer.address |should| equal_to ("Casa Da Paula")
        len(self.customer.all_customers) |should| equal_to (1)

class TestPurchase(unittest.TestCase):
    def test_make_a_purchase(self):                                                 #faz uma venda
        self.purchase = Purchase(1, 1, "17/01/2011") #id, customer, date_of_purchase
        self.purchase.id |should| equal_to (1)
        self.purchase.customer |should| equal_to(1)
        self.purchase.date |should| equal_to (date(2011, 1, 17))
        self.purchase.add_product(1)
        self.purchase.add_product(1)
        self.purchase.products |should| equal_to([1, 1])

    def test_verify_a_purchase_in_the_warranty(self):
        self.purchase = Purchase(1, 1, "17/01/2011") #id, customer, date_of_purchase
        self.purchase.id |should| equal_to (1)
        self.purchase.customer |should| equal_to(1)
        self.purchase.date |should| equal_to (date(2011, 1, 17))
        self.purchase.add_product(1)
        self.purchase.add_product(1)
        self.purchase.products |should| equal_to([1, 1])
        self.purchase.is_my_purchase_in_the_warranty() |should| equal_to(True)

    def test_verify_a_purchase_that_is_not_under_warranty(self):
        self.purchase = Purchase(1, 1, "17/01/2005") #id, customer, date_of_purchase
        self.purchase.id |should| equal_to (1)
        self.purchase.customer |should| equal_to(1)
        self.purchase.date |should| equal_to (date(2005, 1, 17))
        self.purchase.add_product(1)
        self.purchase.add_product(1)
        self.purchase.products |should| equal_to([1, 1])
        self.purchase.is_my_purchase_in_the_warranty() |should| equal_to(False)

    def test_make_an_exchange(self):
        self.purchase = Purchase(1, 1, "17/01/2011") #id, customer, date_of_purchase
        self.purchase.id |should| equal_to (1)
        self.purchase.customer |should| equal_to(1)
        self.purchase.date |should| equal_to (date(2011, 1, 17))
        self.purchase.add_product(1)
        self.purchase.add_product(1)
        self.purchase.products |should| equal_to([1, 1])
        #self.purchase.is_my_purchase_in_the_warranty(1) |should| equal_to(True)
        self.exchange = Exchange(1, 1, 1, "Produto nao liga") #id, customer, product_exchanged, problem_of_product
        self.exchange.problem |should| equal_to ("Produto nao liga")
        self.exchange.make_an_exchange(self.purchase) |should| equal_to(True)

    def test_make_an_exchange(self):                                                     #faz troca
        self.purchase = Purchase(1, 1, "17/01/2005") #id, customer, date_of_purchase
        self.purchase.id |should| equal_to (1)
        self.purchase.customer |should| equal_to(1)
        self.purchase.date |should| equal_to (date(2005, 1, 17))
        self.purchase.add_product(1)
        self.purchase.add_product(1)
        self.purchase.products |should| equal_to([1, 1])
        self.exchange = Exchange(1, 1, 1, "Produto nao liga") #id, customer, product_exchanged, problem_of_productself.exchange = Exchange(1, 1, 1, "Produto nao liga") #id, customer, product_exchanged, problem_of_product
        self.exchange.problem |should| equal_to ("Produto nao liga")
        self.exchange.make_an_exchange(self.purchase) |should| equal_to(False)

