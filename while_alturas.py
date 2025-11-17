#FAÇA UM PROGRAMA QUE RECEBA 4 ALTURAS USANDO UM LAÇO DE REPETIÇÃO E REALIZE A SOMA DESSAS ALTURAS

SOMA = 0
QTDE_ENTRADAS = 4

while QTDE_ENTRADAS > 0:
    altura = float(input("Insira a altura: "))
    SOMA += altura
    QTDE_ENTRADAS -= 1

print("A soma das alturas é: ", SOMA) #soma das alturas
print("A média das alturas é: ", SOMA / 4) #média das alturas, exercício extra
