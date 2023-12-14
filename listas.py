import math
numero_elementos = int(input("Insira o quantitativo de elementos da lista :"))
lista = [int(input("Insira os elementos :")) for i in range(numero_elementos)]

print("A lista adicionada foi :",lista)
for index, valor in enumerate(lista):
    potencia = math.pow(valor,2)
    print("O elemento de index {} com respectivo valor de {} e sua potencia ao quadrado é é {}.".format(index,valor,int(potencia)))

