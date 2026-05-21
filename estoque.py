import sqlite3

conexao = sqlite3.connect("banco_estoque.db")
cursor = conexao.cursor()

while True:
    try:

        cursor.execute("""CREATE TABLE IF NOT EXISTS estoque_loja(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    quantidade INTEGER NOT NULL,
                    preco FLOAT NOT NULL
                    )""")

        def inserir_dados():
            print("--- Inserir Dados ao Estoque ---")
            nome = input("Digite o nome da peça: ")
            quantidade = int(input("Digite a quantidade da peça: "))
            preco = float(input("Digite o preço da peça: "))
            
            cursor.execute("""INSERT INTO estoque_loja
                        (nome, quantidade, preco) VALUES
                        (?, ?, ?)""", (nome, quantidade, preco))
            print("Estoque Atualizado!")
            conexao.commit()

        def visualizar_estoque():
            cursor.execute("""SELECT * FROM estoque_loja""")
            dados_estoque = cursor.fetchall()
            for dados in dados_estoque:
                id, nome, quantidade, preco = dados
                print(f"""Id: {id}
Nome: {nome}
Quantidade: {quantidade}
Preço: R$ {preco}""")
                print()


            conexao.commit()

        def atualizar_dados():
            print("--- Atualizar Dados ---")
            buscar_id = int(input("Digite o ID que deseja buscar: "))
            cursor.execute("""SELECT * FROM estoque_loja WHERE id = ?""", (buscar_id,))
            produto = cursor.fetchone()
            if produto is None:
                print("ID não encontrado...")
                return

            print("Produto ENCONTRADO")
            print()
            print(f"""ID: {produto[0]}
Nome: {produto[1]}
Quantidade: {produto[2]}
Preço: R$ {produto[3]}""")
            print()
            print("-- Escolha a Opção para Atualizar --")
            print("[1] Quantidade\n[2] Preço\n[3] Sair")
            escolha_opçao = int(input("Digite a opção: "))
            if escolha_opçao == 1:
                nova_quantidade = int(input("Digite a Nova Quantidade do Produto: "))
                cursor.execute("""UPDATE estoque_loja SET quantidade = ? WHERE id = ?""", (nova_quantidade, buscar_id))
                print("Quantidade ATUALIZADA!")
            elif escolha_opçao == 2:
                novo_preco = float(input("Digite o Novo Preço do Produto: "))
                cursor.execute("""UPDATE estoque_loja SET preco = ? WHERE id = ?""", (novo_preco, buscar_id))
                print("Preço ATUALIZADO!")
            elif escolha_opçao == 3:
                return "Saindo para o Menu"
            else:
                print("Escolha apenas [1], [2] ou [3]")
                return


            conexao.commit()

        def deletar_dados():
            print("--- Deletar Dados ---")
            buscar_id = int(input("Digite o ID que deseja deletar: "))
            cursor.execute("""SELECT * FROM estoque_loja WHERE id = ?""", (buscar_id,))
            produto = cursor.fetchone()

            if produto is None:
                print("ID não encontrado...")
                return
            print("ID ENCONTRADO")
            print()
            print(f"ID: {produto[0]}")
            print(f"Nome: {produto[1]}")
            print(f"Quantidade: {produto[2]}")
            print(f"Preço: R$ {produto[3]}")
            deletar_opcao = input("Deseja deletar esse produto? (S/N): ").lower()
            if deletar_opcao == "s":
                cursor.execute("DELETE FROM estoque_loja WHERE id = ?", (buscar_id,))
                print("ID DELETADO COM SUCESSO!")
            elif deletar_opcao == "n":
                return "Não Deletado"
            else:
                print("Digite apenas (S)sim ou (N)não")
                return 


            conexao.commit()

        def sair():
            print("Você saiu!")
        ### Menu incial ###
        
        print("-- Sistema de Gerenciamento de Estoque --")
        print()
        print("""[1] Inserir Dados
[2] Visualizar Dados
[3] Atualizar Dados
[4] Deletar Dados
[5] Sair""")
        opcao = int(input("Escolha uma das opções: "))

        if opcao == 1:
            inserir_dados()
        elif opcao == 2:
            visualizar_estoque()
        elif opcao == 3:
            atualizar_dados()
        elif opcao == 4:
            deletar_dados()
        elif opcao == 5:
            sair()
            break
        else:
            print("Digite apenas as opções de [1] a [5]")
    except ValueError:
        print("Digite apenas Números")
        continue