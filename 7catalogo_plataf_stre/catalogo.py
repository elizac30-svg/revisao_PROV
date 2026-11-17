import json


def carregar_catalogo():
    with open("catalogo.json", "r", encoding="utf-8") as arquivo:
        catalogo = json.load(arquivo)

    return catalogo


def mostrar_titulo(titulo):
    if titulo["classificacao"] == 0:
        classificacao = "L"
    else:
        classificacao = titulo["classificacao"]

    print(
        f'{titulo["id"]:2} '
        f'{titulo["titulo"]:<25} '
        f'{titulo["tipo"]:<12} '
        f'{titulo["genero"]:<15} '
        f'{titulo["ano"]} '
        f'{str(classificacao):>3} '
        f'nota {titulo["nota"]:.1f}'
    )


def listar_tudo(catalogo):
    for titulo in catalogo:
        mostrar_titulo(titulo)


def listar_generos(catalogo):
    generos = []

    for titulo in catalogo:
        if titulo["genero"] not in generos:
            generos.append(titulo["genero"])

    return generos


def filtrar_por_genero(catalogo, genero):
    for titulo in catalogo:
        if titulo["genero"].lower() == genero.lower():
            mostrar_titulo(titulo)


def buscar_titulo(catalogo, busca):
    for titulo in catalogo:
        if busca.lower() in titulo["titulo"].lower():
            mostrar_titulo(titulo)


def titulos_por_idade(catalogo, idade):
    for titulo in catalogo:
        if titulo["classificacao"] <= idade:
            mostrar_titulo(titulo)


def mais_bem_avaliados(catalogo, quantidade=5):
    ordenados = sorted(
        catalogo,
        key=lambda t: t["nota"],
        reverse=True
    )

    for titulo in ordenados[:quantidade]:
        mostrar_titulo(titulo)


def estatisticas(catalogo):
    filmes = 0
    series = 0
    soma_notas = 0

    for titulo in catalogo:
        if titulo["tipo"] == "Filme":
            filmes += 1
        elif titulo["tipo"] == "Série":
            series += 1

        soma_notas += titulo["nota"]

    media = soma_notas / len(catalogo)

    generos = listar_generos(catalogo)

    print(f"Títulos: {len(catalogo)} (filmes: {filmes}, séries: {series})")
    print(f"Nota média: {media:.2f}")
    print(f"Gêneros: {', '.join(generos)}")



if __name__ == "__main__":

    catalogo = carregar_catalogo()

    print(f"Catálogo carregado: {len(catalogo)} títulos.")

    while True:

        print("===== CINEFLIX =====")
        print("1 - Listar tudo")
        print("2 - Filtrar por gênero")
        print("3 - Buscar título")
        print("4 - Títulos para a minha idade")
        print("5 - Mais bem avaliados")
        print("6 - Estatísticas")
        print("0 - Sair")

        escolha = input("Escolha: ")

        if escolha == "1":

            listar_tudo(catalogo)

        elif escolha == "2":

            generos = listar_generos(catalogo)

            print(f"Gêneros: {', '.join(generos)}")

            genero = input("Gênero: ")

            filtrar_por_genero(catalogo, genero)

        elif escolha == "3":

            busca = input("Parte do título: ")

            buscar_titulo(catalogo, busca)

        elif escolha == "4":

            idade = int(input("Sua idade: "))

            titulos_por_idade(catalogo, idade)

        elif escolha == "5":

            quantidade = input("Quantos (Enter = 5)? ")

            if quantidade == "":
                quantidade = 5
            else:
                quantidade = int(quantidade)

            mais_bem_avaliados(catalogo, quantidade)

        elif escolha == "6":

            estatisticas(catalogo)

        elif escolha == "0":

            break

        else:
            print("Opção inválida.")
