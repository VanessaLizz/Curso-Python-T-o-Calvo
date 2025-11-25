vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def contar_vogais(texto):
    count = 0
    for letra in texto:
        if letra in vogais:
            count += 1
    print(f"O número de vogais é {count}")
    return count

contar_vogais("O rato roeu a roupa do rei de Roma")