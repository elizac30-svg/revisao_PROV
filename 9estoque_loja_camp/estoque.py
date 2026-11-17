
import banco_estoque


def mostrar_produtos(produtos):
    print("ID Produto Categoria Preço Qtd")

    for produto in produtos:
        id = produto[0]
        nome = produto[1]
        categoria = produto[2]
        preco = produto[3]
        quantidade = produto[4]
        minimo = produto[5]

        if quantidade < minimo:
            aviso = "<- repor"
        else:
            aviso = ""

        print(
            f"{id} {nome} {categoria} "
            f"{preco:.2f} {quantidade} {aviso}"
        )


# PROGRAMA PRINCIPAL
if __name__ == "__main__":

    conn = banco_estoque.conectar()

    while True:

        print("===== ESTOQUE - LOJA DE CAMPING =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar por nome")
        print("4 - Entrada (chegou mercadoria)")
        print("5 - Saída (venda)")
        print("6 - Produtos para repor")
        print("7 - Valor total do estoque")
        print("0 - Sair")

        escolha = input("Escolha: ")

        if escolha == "1":

            nome = input("Nome do produto: ")
            categoria = input("Categoria: ")
            preco = float(input("Preço: R$ ").replace(",", "."))
            quantidade = int(input("Quantidade: "))
            minimo = int(input("Estoque mínimo: "))

            id = banco_estoque.cadastrar(
                conn, nome, categoria, preco, quantidade, minimo
            )

            print(f"Produto cadastrado. ID: {id}")

        elif escolha == "2":

            produtos = banco_estoque.listar(conn)
            mostrar_produtos(produtos)

        elif escolha == "3":

            texto = input("Parte do nome: ")

            produtos = banco_estoque.buscar(conn, texto)
            mostrar_produtos(produtos)

        elif escolha == "4":

            id = int(input("Id do produto: "))
            quantidade = int(input("Quantidade que chegou: "))

            resultado = banco_estoque.entrada(conn, id, quantidade)

            if resultado:
                print("Entrada registrada.")
            else:
                print("Produto não encontrado.")

        elif escolha == "5":

            id = int(input("Id do produto: "))
            quantidade = int(input("Quantidade vendida: "))

            resultado = banco_estoque.saida(conn, id, quantidade)

            print(resultado)

        elif escolha == "6":

            produtos = banco_estoque.estoque_baixo(conn)
            mostrar_produtos(produtos)

        elif escolha == "7":

            total = banco_estoque.valor_total(conn)

            print(f"Valor total em estoque: R$ {total:.2f}")

        elif escolha == "0":

            conn.close()
            break

        else:
            print("Opção inválida.")
