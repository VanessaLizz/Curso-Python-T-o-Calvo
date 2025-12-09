jogador1 = input("Jogador 1, escolha pedra, papel ou tesoura: ").lower()
jogador2 = input("Jogador 2, escolha pedra, papel ou tesoura: ").lower()

def compare(u1, u2):
    if u1 == u2:
        return "Empate!"

    elif u1 == "pedra":
        if u2 == "tesoura":
            return "Pedra ganha!"
        else:
            return "Papel ganha!"

    elif u1 == "tesoura":
        if u2 == "papel":
            return "Tesoura ganha!"
        else:
            return "Pedra ganha!"

    elif u1 == "papel":
        if u2 == "pedra":
            return "Papel ganha!"
        else:
            return "Tesoura ganha!"

    else:
        return "Entrada inválida! Escolha pedra, papel ou tesoura."

print(compare(jogador1, jogador2))
