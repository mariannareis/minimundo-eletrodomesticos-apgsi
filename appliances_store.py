class Product():

    def __init__(self):
        self.warranty = {'date_of_purchase':'17/01/2011',
                         'mark':'Arno',
                         'model':'H3-42X',
                         'serial_number':'123456',
                         }

class Customer():
    def __init__(self, my_id, name, address):
        self.id = my_id
        self.name = name
        self.address = address

