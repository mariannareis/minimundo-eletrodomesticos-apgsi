from datetime import date

class Customer():
    def __init__(self, my_id, name, address):
        self.id = my_id
        self.name = name
        self.address = address

class Product():

    def __init__(self, my_id, mark, model, serial_number):
        self.id = my_id
        self.mark = mark
        self.model = model
        self.serial_number = serial_number
#        self.warranty = {
#                         'id':my_id,
#                         'mark':mark,
#                         'model':model,
#                         'serial_number':serial_number,
#                         }

class Purchase():

    def __init__(self, my_id, customer, date):
        self.id = my_id
        self.customer = customer
        self.date = date
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def is_my_purchase_in_the_warranty(self, purchase_id):
        warranty_year = date.today().year - 1
        warranty_date = date(warranty_year, date.today().month, date.today().day)
        if date(2010, 1, 17) <= warranty_date:
            return True
        else:
            return False

