import mysql.connector

conexao = mysql.connector.connect(
  host='localhost',
  user='root',
  password='Root@123',
  database='pokedex'
)

if conexao.is_connected():
  print("BEM VINDO A SUA POKEDEX")
  while True:
    menu = input("""
    ESCOLHA UMA OPÇÃO:
    1 - ADICIONAR POKEMON
    2 - VER TODOS OS SEUS POKEMONS
    3 - EDITAR UM POKEMON
    4 - EXCLUIR UM POKEMON
    0 - SAIR
    """)
    match menu:
      case '1':
        print("CADASTRO DE POKEMONS")
        nome = input("Digite o nome do pokemon que deseja cadastrar: ")
        tipo = input("Digite o tipo do novo pokemon: ")
        abinha = conexao.cursor(dictionary=True)
        abinha.execute(f"""
        INSERT INTO pokemons (nome, tipo) VALUES
            ('{nome}', '{tipo}')
        """)
        conexao.commit() #SEMPRE QUE A ABINHA EXECUTAR UM INSERT OU UPDATE OU DELETE TEM QUE RODAR UM COMMIT PARA CONFIRMAR AS ALTERAÇÕES
        print(f"Pokemon {nome} adicionado com sucesso.")
        abinha.close()
      case '2':
        abinha = conexao.cursor(dictionary=True)
        abinha.execute("SELECT * FROM pokemons")
        lista = abinha.fetchall() #SEMPRE QUE A ABINHA EXECUTAR UM SELECT TEM QUE RODAR UM FETCH SEJA ELE ALL OU ONE PARA GUARDAR O QUE FOI SELECIONADO.
        for element in lista:
          print(f"""
          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
          {element['id']} - {element['nome']} ({element['tipo']})
          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
          """)
        abinha.close()
      case '3':
        abinha = conexao.cursor(dictionary=True)
        abinha.execute("SELECT * FROM pokemons")
        lista = abinha.fetchall()
        for element in lista:
          print(f"{element['id']} - {element['nome']} ({element['tipo']})")
        id_editado = int(input("Digite o número do ID do pokemon que você deseja editar: "))
        pokemons_encontrado = 0
        for element in lista:
          if element['id'] == id_editado:
            pokemons_encontrado += 1
            while True:
              menu_editar = input("""
              ESCOLHA O QUE VOCÊ DESEJA EDITAR:
              1 - NOME
              2 - TIPO
              0 - VOLTAR
              """)
              match menu_editar:
                case '1':
                  novo_nome = input("Digite o novo nome do pokemon: ")
                  abinha.execute(f"UPDATE pokemons SET nome = '{novo_nome}' WHERE id = {id_editado}")
                  conexao.commit()
                  print("Nome do pokemon atualizado com sucesso!")
                case '2':
                  novo_tipo = input("Digite o novo tipo do pokemon: ")
                  abinha.execute(f"UPDATE pokemons SET tipo = '{novo_tipo}' WHERE id = {id_editado}")
                  conexao.commit()
                  print("Tipo do pokemon atualizado com sucesso.")
                case '0':
                  break
                case _:
                  print("Opção inválida")
        if pokemons_encontrado == 0:
          print("Pokemon não encontrado.")
        abinha.close()
      case '4':
        abinha = conexao.cursor(dictionary=True)
        abinha.execute("SELECT * FROM pokemons")
        lista = abinha.fetchall()
        for element in lista:
          print(f"{element['id']} - {element['nome']}")
        id_excluido = int(input("Digite o número do ID do pokemon que você deseja excluir: "))
        pokemons_encontrado = 0
        for element in lista:
          if element['id'] == id_excluido:
            pokemons_encontrado += 1
            abinha.execute(f"DELETE FROM pokemons WHERE id = {id_excluido}")
            conexao.commit()
            print(f"Pokemon {element['nome']} foi excluído com sucesso")
        if pokemons_encontrado == 0:
          print("Pokemon não encontrado.")
        abinha.close()
        
      case '0':
        break
      case _:
        print("Opção inválida")
else:
  print("Erro ao se conectar com o banco.")