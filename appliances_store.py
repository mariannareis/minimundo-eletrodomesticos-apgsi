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

class Storage():

    products_by_type = []         #type are the same mark and model!!!
    products_serials = []

    def add_products(self, mark, model, quantity):
        self.mark = mark
        self.model = model
        for product in (0, quantity):
            self.set_products_serials(self)

        self.storage_products(self)

    def set_products_serials(self, serial_numbers):
         self.products_serials = serial_numbers

    @staticmethod
    def storage_products(self):
        self.products_by_type.append(self)

class Purchase():

    products = []

    def __init__(self, my_id, customer, unformatted_date):
        self.id = my_id
        self.customer = customer
        self.date = date(int(unformatted_date[6:10]),int(unformatted_date[3:5]), int(unformatted_date[0:2]))

    def add_product(self, mark, model, quant):
        for y in range(0, (len(Storage.products_by_type))):
            if (Storage.products_by_type[y].mark == mark):
                for x in range(0, quant):
                    self.products.append(Storage.products_by_type[y].products_serials[quant-1])
                    a = str(Storage.products_by_type[y].products_serials[quant-1])
                    Storage.products_by_type[y].products_serials.remove(a)

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

