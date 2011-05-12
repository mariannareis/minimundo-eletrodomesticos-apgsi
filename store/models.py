import sys, os
sys.path.append("/home/mari/eispatterns")

#Para resources => subclasses.
#Para nodes => decorators.
#Para movements => configuracao.

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
class CustomerDecorator(models.Model, Decorator): #decoracao concreta.... tem uma estancia de Person, que sera decorado'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        super(CustomerDecorator, self).save(*args, **kwargs)
        Decorator.__init__(self)

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

#Produto = Resource (WorkItem)
class Product(models.Model):
    product_model = models.ForeignKey(ProductModel)
    serial_number = models.CharField(max_length=100)

#- Estoque(Decorator de No, com 'ponteiros' para as instancias de Produto)
#Note que movimentacoes de estoque sao representadas por um ou mais movements.
#Saida de item do estoque para o cliente => movement entre os nos Estoque e Cliente.
#class Stock(fk_product, in_stock)

#class Sale(fk_product, fk_cliente, data) ---> has_many products, belongs_to product / has_many clientes, belongs_to clientes
#Instancia de Process

#class Exchange(fk_product, fk_cliente, data, defeito_apresentado) ---> has_one product, belongs_to product
#Instancia de Process

