
import json
import os
from datetime import datetime


def carregar_shows():
    if os.path.exists("shows.json"):
        with open("shows.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    else:
        return []


def salvar_shows(shows):
    with open("shows.json", "w", encoding="utf-8") as arquivo:
        json.dump(shows, arquivo, ensure_ascii=False, indent=2)


def ordenar_shows(shows):
    return sorted(
        shows,
        key=lambda s: datetime.strptime(s["data"], "%d/%m/%Y")
    )


def listar_shows(shows):
    ordenados = ordenar_shows(shows)

    for i, show in enumerate(ordenados, start=1):
        if show["ingressos"] == 0:
            disponibilidade = "ESGOTADO"
        else:
            disponibilidade = f'{show["ingressos"]} ingressos'

        print(
            f'{i}. {show["data"]} {show["artista"]} '
            f'{show["cidade"]} R$ {show["preco"]:.2f} '
            f'{disponibilidade}'
        )

    return ordenados


def cadastrar_show(shows):
    artista = input("Artista/banda: ")
    cidade = input("Cidade: ")

    while True:
        data = input("Data (dd/mm/aaaa): ")

        try:
            datetime.strptime(data, "%d/%m/%Y")
            break
        except ValueError:
            print("Data inválida. Digite no formato dd/mm/aaaa.")

    preco = float(input("Preço do ingresso: R$ ").replace(",", "."))
    ingressos = int(input("Ingressos disponíveis: "))

    show = {
        "artista": artista,
        "cidade": cidade,
        "data": data,
        "preco": preco,
        "ingressos": ingressos
    }

    shows.append(show)
    salvar_shows(shows)

    print("Show cadastrado e agenda salva.")


def shows_por_cidade(shows):
    cidade = input("Cidade: ")

    for show in ordenar_shows(shows):
        if show["cidade"].lower() == cidade.lower():
            print(
                f'{show["data"]} {show["artista"]} '
                f'{show["cidade"]} R$ {show["preco"]:.2f} '
                f'{show["ingressos"]} ingressos'
            )


def vender_ingressos(shows):
    ordenados = listar_shows(shows)

    if len(ordenados) == 0:
        print("Não há shows cadastrados.")
        return

    numero = int(input("Número do show: "))

    if numero < 1 or numero > len(ordenados):
        print("Número inválido.")
        return

    show = ordenados[numero - 1]

    quantidade = int(input("Quantos ingressos? "))

    if quantidade <= 0:
        print("Quantidade inválida.")
    elif quantidade > show["ingressos"]:
        print(f'Só restam {show["ingressos"]} ingressos.')
    else:
        show["ingressos"] -= quantidade

        total = quantidade * show["preco"]

        print(
            f'Venda: {quantidade} x R$ {show["preco"]:.2f} '
            f'= R$ {total:.2f}'
        )

        salvar_shows(shows)


def remover_show(shows):
    ordenados = listar_shows(shows)

    if len(ordenados) == 0:
        print("Não há shows cadastrados.")
        return

    numero = int(input("Número do show: "))

    if numero < 1 or numero > len(ordenados):
        print("Número inválido.")
        return

    show = ordenados[numero - 1]

    shows.remove(show)
    salvar_shows(shows)

    print(f'Show de {show["artista"]} removido.')


# PROGRAMA PRINCIPAL
if __name__ == "__main__":

    shows = carregar_shows()

    print(f"Agenda carregada: {len(shows)} shows.")

    while True:

        print("===== AGENDA DE SHOWS =====")
        print("1 - Listar shows")
        print("2 - Cadastrar show")
        print("3 - Shows em uma cidade")
        print("4 - Vender ingressos")
        print("5 - Remover show")
        print("0 - Sair")

        escolha = input("Escolha: ")

        if escolha == "1":
            listar_shows(shows)

        elif escolha == "2":
            cadastrar_show(shows)

        elif escolha == "3":
            shows_por_cidade(shows)

        elif escolha == "4":
            vender_ingressos(shows)

        elif escolha == "5":
            remover_show(shows)

        elif escolha == "0":
            break

        else:
            print("Opção inválida.")
