from datetime import date

class Customer():

    all_customers = []

    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
        self.storage_customers(self)

    @staticmethod
    def storage_customers(self):
        self.all_customers.append(self)

class Storage():

    products_by_type = []         #type are the same mark and model!!!
    products_serials = []

    def __init__(self, mark, model, quantity):
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

    @staticmethod
    def check_disponibility_of_equipments(self):
        result = ""
        for x in range(0, len(Storage.products_by_type)):
            result = result + Storage.products_by_type[x].mark + Storage.products_by_type[x].model + str(len(Storage.products_by_type[x].products_serials))
        return result

class Purchase():

    products = []

    def __init__(self, my_id, customer, unformatted_date):
        self.id = my_id
        self.customer = customer
        self.date = date(int(unformatted_date[6:10]),int(unformatted_date[3:5]), int(unformatted_date[0:2]))

    def sell_product(self, mark, model, quant):

        if (len(Storage.products_by_type)) == 1:
            products_size = 1
        else:
            products_size = len(Storage.products_by_type) - 1

        for y in range(0, products_size):
            if (Storage.products_by_type[y].mark == mark):
                for x in range(0, quant):
                    if len(Storage.products_by_type[y].products_serials) >= 1:
                        self.products.append(Storage.products_by_type[y].products_serials[quant-1])
                        a = str(Storage.products_by_type[y].products_serials[quant-1])
                        Storage.products_by_type[y].products_serials.remove(a)
                    else:
                        return "nao pude adicionar"

    def is_my_purchase_in_the_warranty(self):
        warranty_year = self.date.year + 1
        warranty_date = date(warranty_year, self.date.month, self.date.day)
        if date.today() <= warranty_date:
            return True
        else:
            return False

class Exchange():

    exchanges = []

    def __init__(self, my_serial, customer, product_exchanged, problem):
        self.serial = my_serial
        self.customer = customer
        self.product_exchanged = product_exchanged
        self.problem = problem
        self.date = date.today()
        self.set_exchanges(self)

    @staticmethod
    def set_exchanges(self):
         self.exchanges.append(self)

    def make_an_exchange(self, purchase):
        if purchase.is_my_purchase_in_the_warranty():
            pass    #troca nao foi implementada!!!!!!!!!!!

    @staticmethod
    def verify_problems_with_equipments(self):

        result = ""
        for x in range(0, len(Exchange.exchanges)):
            result = result + str(Exchange.exchanges[x].customer) + str(Exchange.exchanges[x].problem)  + str(Exchange.exchanges[x].date) + str(Exchange.exchanges[x].serial)
        return result

