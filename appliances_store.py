from datetime import date

class Customer():

    all_customers = []

    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
        self.storageCustomers(self)

    @staticmethod
    def storageCustomers(self):
        self.all_customers.append(self)

class Product():

    all_products = []

    def __init__(self, id, mark, model, serial_number):
        self.id = id
        self.mark = mark
        self.model = model
        self.serial_number = serial_number
        self.storageProducts(self)

    @staticmethod
    def storageProducts(self):
        self.all_products.append(self)

class Stock():

    def __init__(self, id, product, quantity):
        self.id = id
        self.product = product
        self.quantity = quantity

    def add_product(self, product):
        self.products.append(product)

   # def remove_product(self, product):
      #  self.product.

class Purchase():

    def __init__(self, my_id, customer, unformatted_date):
        self.id = my_id
        self.customer = customer
        self.date = date(int(unformatted_date[6:10]),int(unformatted_date[3:5]), int(unformatted_date[0:2]))
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def is_my_purchase_in_the_warranty(self):
        warranty_year = self.date.year + 1
        warranty_date = date(warranty_year, self.date.month, self.date.day)
        if date.today() <= warranty_date:
            return True
        else:
            return False

class Exchange():

    def __init__(self, my_id, customer, product_exchanged, problem):
        self.id = my_id
        self.customer = customer
        self.product_exchanged = product_exchanged
        self.problem = problem

    def make_an_exchange(self, purchase):
        return purchase.is_my_purchase_in_the_warranty()
       # if purchase.is_my_purchase_in_the_warranty() is True:
        #    self

