import sys
sys.path.append("/home/mari/eispatterns")
sys.path.append("/home/mari/minimundo-eletrodomesticos-apgsi")

import unittest
from should_dsl import should, should_not
from domain.node.person import Person
from domain.supportive.association_error import AssociationError
from store.models import Customer
from store.decorators.customer_node_decorator import CustomerDecorator

#from store.decorators.bank_account_decorator import BankAccountDecorator
#from store.resources.loan_request import LoanRequest
#from store.resources.customer import Customer
#from ludibrio import Stub
#from domain.node.machine import Machine

#class CustomerTestCase(unittest.TestCase):
#    def setUp(self):
#        self.a_customer = Customer.objects.create(name="marianna", address="casa de mari")
#        self.ruhan = Customer.objects.create(name="ruhan", address="casa de ruhan")

class CustomerDecoratorSpec(unittest.TestCase):

    def setUp(self):
        self.a_customer = CustomerDecorator('mari','casa de mari')
        #test doubles won't work given type checking rules, using classic
        self.a_person = Person()
        #self.an_purchase = BankAccountDecorator('1234567-8')

    def it_decorates_a_person(self):
        #should work
        self.a_customer.decorate(self.a_person)
        self.a_customer.decorated |should| be(self.a_person)

        #should fail
        non_person = 'I am not a person'
        (self.a_customer.decorate, non_person) |should| throw(AssociationError)

    def test_Verify_inclusion_of_customers(self):
        self.a_customer.name |should| equal_to('mari')
        self.a_customer.address |should| equal_to('casa de mari')

#    def it_creates_a_loan_request(self):
#        self.a_credit_analyst_decorator.decorate(self.a_person)
#        self.a_credit_analyst_decorator.create_loan_request(self.an_account, 10000)
#        self.a_person.input_area |should| contain('1234567-8')

#    def it_analyses_a_loan_request(self):
#        #Stub removed, from now on Node really transfers resources internally
#        self.a_credit_analyst_decorator.decorate(self.a_person)
#        self.an_account.average_credit = 5000
#        #should approve
#        self.a_credit_analyst_decorator.create_loan_request(self.an_account, 10000)
#        self.a_credit_analyst_decorator.analyse(self.an_account.number)
#        self.a_credit_analyst_decorator.decorated.output_area['1234567-8'].approved |should| equal_to(True)
#        #should refuse
#        self.a_credit_analyst_decorator.create_loan_request(self.an_account, 50000)
#        self.a_credit_analyst_decorator.analyse(self.an_account.number)
#        self.a_credit_analyst_decorator.decorated.output_area['1234567-8'].approved |should| equal_to(False)


#    def it_creates_a_purchase(self):
#        loan_request = LoanRequest(self.an_account, 7000, self.a_credit_analyst_decorator)
#        self.a_customer.decorate(self.a_person)
#        self.a_customer.decorated.output_area[self.product] = '123'
#        #creates a machine to be decorated by the account - will need to check its processing_area
#        a_machine = Machine()
#        self.an_purchase.decorate(a_machine)
#        #creates the loan
#        self.a_customer_decorator.purchase("aa")
#        #given that I am using datetime to generate the key, I cannot access the newly
#        #created loan through its key
#        self.a_customer_decorator.decorated.output_area.values() |should| have_at_least(1).product

#    def it_changes_its_loan_limit(self):
#        self.a_credit_analyst_decorator.change_loan_limit(100000)
#        self.a_credit_analyst_decorator.loan_limit |should| be(100000)

