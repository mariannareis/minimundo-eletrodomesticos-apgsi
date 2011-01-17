class Customer():
    def __init__(self, my_id, name, address):
        self.id = my_id
        self.name = name
        self.address = address

class Product():

    def __init__(self, my_id, mark, model, serial_number):
        self.warranty = {
                         'id':my_id,
                         'mark':mark,
                         'model':model,
                         'serial_number':serial_number,
                         }

