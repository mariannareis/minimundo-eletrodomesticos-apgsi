from datetime import date

class Customer():
    def __init__(self, my_id, name, address):
        self.id = my_id
        self.name = name
        self.address = address
        StorageCustomers(self)

class StorageCustomers():

    all_customers = []

    def __init__(self, customer):
        self.all_customers.append(customer)

class Product():

    def __init__(self, my_id, mark, model, serial_number):
        self.id = my_id
        self.mark = mark
        self.model = model
        self.serial_number = serial_number
        StorageProducts(self)

class StorageProducts():

    all_products = []

    def __init__(self, product):
        self.all_products.append(product)

class Purchase():

    def __init__(self, my_id, customer, unformatted_date):
        self.id = my_id
        self.customer = customer
        self.date = date(int(unformatted_date[6:10]),int(unformatted_date[3:5]), int(unformatted_date[0:2]))
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def is_my_purchase_in_the_warranty(self, purchase_id):
        warranty_year = self.date.year + 1
        warranty_date = date(warranty_year, self.date.month, self.date.day)
        if date.today() <= warranty_date:
            return True
        else:
            return False

class Exchange():

    def __init__(self, my_id, customer, product_exchanged):
        self.id = my_id
        self.customer = customer
        self.product_exchanged = product_exchanged

