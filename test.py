#<<<<<<< HEAD
#import unittest
#from store.models import Customer
##from mewe.resources.customer import Customer
#from should_dsl import should, should_not
#from ludibrio import Stub
#from domain.node.person import Person
#from domain.node.machine import Machine
#from domain.supportive.association_error import AssociationError
#=======
##import unittest
##import sys
##sys.path.append("/home/mari/minimundo-eletrodomesticos-apgsi")
##from store.models import Customer
#>>>>>>> 204ee74b2a30d784f41cbfaa4d28143e541d5c30

##class CustomerTestCase(unittest.TestCase):
##    def setUp(self):
##        self.mari = Customer.objects.create(name="marianna", address="casa de mari")
##        self.ruhan = Customer.objects.create(name="ruhan", address="casa de ruhan")

#<<<<<<< HEAD
#    def it_verify_if_the_people_was_added(self):
#        self.assertEquals(self.mari.address, 'casa de mari')
#        self.assertEquals(self.ruhan.name, 'ruhan')
#=======
##    def test_Verify_inclusion_of_customers(self):
##        self.assertEquals(self.mari.address, 'casa de mari')
##        self.assertEquals(self.ruhan.name, 'ruhan')
#>>>>>>> 204ee74b2a30d784f41cbfaa4d28143e541d5c30



#class CreditAnalystDecoratorSpec(unittest.TestCase):

#    def setUp(self):
#        self.a_credit_analyst_decorator = CreditAnalystDecorator('12345-6')
#        #test doubles won't work given type checking rules, using classic
#        self.a_person = Person()
#        self.an_account = BankAccountDecorator('1234567-8')

#    def it_decorates_a_person(self):
#        #should work
#        self.a_credit_analyst_decorator.decorate(self.a_person)
#        self.a_credit_analyst_decorator.decorated |should| be(self.a_person)
#        #should fail
#        non_person = 'I am not a person'
#        (self.a_credit_analyst_decorator.decorate, non_person) |should| throw(AssociationError)

