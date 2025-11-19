#Escreva um programa (função!) que receba uma lista e retorne uma nova lista contendo todos os elementos da primeira lista, menos os duplicados.
lista = [1, 5, 10, 4, 1, 92, 5, 3, 7, 10, 94, 92, 5, 7, 12, 12, 8]

lista_2 = []

for i in lista:
    if i not in lista_2:
        lista_2.append(i)

print(lista_2)