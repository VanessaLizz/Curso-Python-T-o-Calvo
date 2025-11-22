
lista = [1, 5, 6, 9, 13, 17, 25, 46, 98]
numero = 14

def encontrar_elemento(lista, numero):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim: 
        meio = (inicio + fim) // 2

        if lista[meio] == numero:
            print("Número encontrado")
            return True
        
        elif lista[meio] < numero:
            inicio = meio + 1

        else:
            fim = meio - 1
    
    return False

resultado = encontrar_elemento(lista, numero)
print("O resultado da verificação foi: ", resultado)