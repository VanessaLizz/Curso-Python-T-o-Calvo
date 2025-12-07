def maior_numero(a,b,c):
     numero_maior = 0
     if a > b:
         if a > c:
             numero_maior = a
         else:
             numero_maior = c
     else:
          if b > c:
             numero_maior = b
          else:
             numero_maior = c
     return numero_maior

a = float(input("Digite o 1º número: "))
b = float(input("Digite o 2º número: "))
c = float(input("Digite o 3º número: "))

resultado = maior_numero(a, b, c)

print(f"O maior do entre A, B e C é: {resultado}")