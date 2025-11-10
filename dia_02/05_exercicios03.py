numero = input("Entre com um número inteiro para calcular sua raiz quadrada: ")
numero = int(numero)

raiz = numero ** (1/2)
raiz = round(raiz, 4)
print("Raiz quadrada de", numero, "é: ", raiz)