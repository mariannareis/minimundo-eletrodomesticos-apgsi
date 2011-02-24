from datetime import date
from appliances_store import *

option = 0
#produtos = []

while option != 7:
    print "Escolha o que deseja fazer: "
    print "1 - Adicionar um produto"
    print "2 - Adicionar um cliente"
    print "3 - Efetuar uma compra"
    print "4 - Verificar se uma compra esta na garantia"
    print "5 - Efetuar uma troca"
    print "6 - Consultar produtos"
    print "7 - Sair"
    option = input()

    if option == 1:
        print "Digite o id do produto: "
        my_id = input()
        print "Digite a marca do produto: "
        mark = raw_input()
        print "Digite o modelo do produto: "
        model = raw_input()
        print " Digite o numero de serie do produto: "
        serial_number = raw_input()
        Product(my_id, mark, model, serial_number)

    if option == 6:
        print StorageProducts.all_products

