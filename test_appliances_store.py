from should_dsl import should, should_not
import unittest
import specloud
from datetime import date

from appliances_store import Product, Customer, Purchase, Exchange, Stock

#EH PRECISO CONTABILIZAR E MOVIMENTAR OS PRODUTOS NO ESTOQUE!

class TestProduct(unittest.TestCase):

    def test_add_one_product(self):                                                 #adiciona um produto
        self.product = Product(1, "Arno", "MD-001", "SN-3122")
        self.product.id |should| equal_to (1)
        self.product.mark |should| equal_to ("Arno")
        self.product.model |should| equal_to ("MD-001")
        self.product.serial_number |should| equal_to ("SN-3122")
        self.product.all_products[0].serial_number |should| equal_to ("SN-3122")
        #self.stock = Stock(1)

class TestCustomer(unittest.TestCase):

    def test_add_one_customer(self):                                                #adiciona um cliente
        self.customer = Customer(1, "Paula", "Casa Da Paula")
        self.customer.id |should| equal_to (1)
        self.customer.name |should| equal_to ("Paula")
        self.customer.address |should| equal_to ("Casa Da Paula")
        len(self.customer.all_customers) |should| equal_to (1)

class TestStock(unittest.TestCase):
    def test_make_a_stock(self):
        self.stock = Stock(1, 1, 10) #id, product, quantity_product
        self.stock.id |should| equal_to (1)
        self.stock.product |should| equal_to (1)
        self.stock.quantity |should| equal_to (10)
        #self.stock.add_product_in_stock(1)

    def test_verify_a_product_in_stock(self):
        self.stock = Stock(1, 1, 10)
        self.stock.id |should| equal_to (1)
        self.stock.product |should| equal_to (1)
        self.stock.quantity |should| equal_to (10)
        #self.stock.is_my_product_in_the_stock() |should| equal_to(True)
        #self.purchase.is_my_purchase_in_the_warranty() |should| equal_to(True)
        #self.stock.make_an_product(self.stock) |should| equal_to(True)


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
        #self.purchase.is_my_purchase_in_the_warranty(1) |should| equal_to(True)
        self.exchange = Exchange(1, 1, 1, "Produto nao liga") #id, customer, product_exchanged, problem_of_productself.exchange = Exchange(1, 1, 1, "Produto nao liga") #id, customer, product_exchanged, problem_of_product
        self.exchange.problem |should| equal_to ("Produto nao liga")
        self.exchange.make_an_exchange(self.purchase) |should| equal_to(False)

