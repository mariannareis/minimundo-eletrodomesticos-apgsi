import sys
sys.path.append("/home/mari/eispatterns")
sys.path.append("/home/mari/mewe")

import unittest
from should_dsl import should, should_not
from domain.node.person import Person
from domain.supportive.association_error import AssociationError
from store.models import CustomerDecorator

class customerSpec(unittest.TestCase):

    def setUp(self):
        #  self.a_customer_decorator = CustomerDecorator('Marianna', 'Casa de Marianna')
        self.customer_decorator = CustomerDecorator.objects.create(name="Exemplo8", address="Casa9")
        #test doubles won't work given type checking rules, using classic
        self.a_person = Person()

    def it_decorates_a_person(self):
        #should work
        self.customer_decorator.decorate(self.a_person)
        self.customer_decorator.decorated |should| be(self.a_person)
        self.customer_decorator.decorated |should| have(1).decorators
        #should fail
        non_person = 'I am not a person'
        (self.customer_decorator.decorate, non_person) |should| throw(AssociationError)

