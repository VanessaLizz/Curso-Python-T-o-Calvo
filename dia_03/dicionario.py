#Crie um dicionário que irá armazenar informações de um contato, incluindo o nome, o telefone e o email. Peça ao usuário para fornecer esses dados, solicitando que ele insira o nome do contato, o número de telefone e o endereço de email. Após coletar todas as informações necessárias, exiba o conteúdo do dicionário, mostrando todas as informações do contato inserido pelo usuário.

nome = input("Digite o seu nome: ")
telefone = input("Digite o seu telefone: ")
email = input("Digite o seu email: ")

informacoes_usuario = {
    "nome": nome,
    "telefone": telefone,
    "email": email
}


print(informacoes_usuario)