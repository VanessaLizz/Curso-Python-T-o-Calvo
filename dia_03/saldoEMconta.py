#qtde indefinida

saldo_total = 0

while True:
    saldo = input("Digite o saldo: ")
    if saldo == "":
        break
    saldo_total += float(saldo)

print("O saldo total é: ",saldo_total)