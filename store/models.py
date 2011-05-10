import sys, os
sys.path.append("/home/mari/eispatterns")

#- Produto(fk_modelo, fk_compra, fk_troca, serial, em_estoque) ---> se houve compra ou troca, em_estoque 'false'
#Produto = Resource (WorkItem??)

#- Estoque(Decorator de No, com 'ponteiros' para as instancias de Produto)
#Note que movimentacoes de estoque sao representadas por um ou mais movements.
#Saida de item do estoque para o cliente => movement entre os nos Estoque e Cliente.

#Para resources => subclasses.
#Para nodes => decorators.
#Para movements => configuracao.

#- Compra(pk_cliente, data)  ---> has_many products
#Instancia de Process

#- Troca(fk_cliente, data, defeito_apresentado) -> ---> has_one product
#Instancia de Process

#-> Compra, Troca
#Sao process, que contem transformations e transportations.

#-> Se o decorator funciona como um wrapper.... Quem 'enveloparia' quem ai?
#Um decorator Cliente envelopa um objeto Person.
#Se o cliente for uma empresa, ele envelopa uma Machine.
#Significa que suas association rules devem ser do tipo decorated |should| be_instance_of(Node)
#Afinal Node inclui Person e Machine.

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "mewe.settings"

from django.db import models
from should_dsl import should
from domain.resource.work_item import WorkItem
from domain.base.decorator import Decorator
from domain.node.person import Person
from domain.supportive.rule import rule
from domain.supportive.association_error import AssociationError

#Decorator de Person
class CustomerDecorator(Decorator):
    def __init__(self, name, address):
        Decorator.__init__(self)
        self.name = name #models.CharField(max_length=100)
        self.address = address #models.CharField(max_length=200)
        self.description = "A Customer"

    def decorate(self, decorated):
        try:
            CustomerDecorator.rule_should_be_person_instance(decorated)
        except:
            raise AssociationError('Person instance expected, instead %s passed' % type(decorated))
        self.decorated = decorated
        self.decorated.decorators[self.__doc__] = self

    @classmethod
    @rule('association')
    def rule_should_be_person_instance(self, decorated):
        ''' Decorated object should be a Person '''
        decorated |should| be_instance_of(Person)

#Subclasse de product (resource)
class Brand(models.Model):
    name = models.CharField(max_length=100)

#Subclasse de product (resource)
class ProductModel(models.Model):
    brand = models.ForeignKey(Brand)
    name = models.CharField(max_length=100)


#class Storage(models.Model, WorkItem):
#    brand = models.CharField(max_length=100)
#    model =  models.CharField(max_length=100)

#    def __init__(self):
#        WorkItem.__init__(self)

#class Product(models.Model, WorkItem):
#    storage = models.ForeignKey(Storage)
#    serial_number = models.CharField(max_length=100)

#    def __init__(self):
#        WorkItem.__init__(self)

