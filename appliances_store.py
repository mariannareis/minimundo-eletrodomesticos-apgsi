class Customer():
    def __init__(self, my_id, name, address):
        self.id = my_id
        self.name = name
        self.address = address

class Product():

    def __init__(self, my_id, date_of_purchase, mark, model, serial_number, customer):
        self.warranty = {
                         'id':my_id,
                         'date_of_purchase':date_of_purchase,
                         'mark':mark,
                         'model':model,
                         'serial_number':serial_number,
                         'initial_customer':customer,
                         }

