#Suponha que eu lhe dê uma lista salva em uma variável: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Escreva uma linha de código Python que receba essa lista ae crie uma nova lista contendo apenas os elementos pares da lista original.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []
for i in a:
    if i % 2 == 0:
        i = b.append(i)

print(b)