import banco_streaming
import tempo


def mostrar_catalogo(conn):
    titulos = banco_streaming.listar_catalogo(conn)

    print("\n===== CATÁLOGO =====")

    for item in titulos:
        print(f"ID: {item[0]} | {item[1]} | {item[2]} | "
              f"{item[3]} | {item[4]} | {tempo.formatar_duracao(item[5])}")


def registrar(conn, perfil):
    try:
        titulo_id = int(input("Id do título: "))
        minutos = int(input("Quantos minutos você assistiu? "))

        if minutos <= 0:
            print("Digite uma quantidade de minutos válida.")
            return

        if banco_streaming.registrar_visualizacao(
            conn, perfil, titulo_id, minutos
        ):
            print("Registrado!")
        else:
            print("Esse id de título não existe.")

    except ValueError:
        print("Digite números válidos.")


def mostrar_historico(conn, perfil):
    registros = banco_streaming.historico(conn, perfil)

    print(f"\n===== HISTÓRICO DE {perfil} =====")

    if len(registros) == 0:
        print("Nenhuma visualização registrada.")
    else:
        for data, titulo, minutos in registros:
            print(f"{data} | {titulo} | {tempo.formatar_duracao(minutos)}")

    total = banco_streaming.total_historico(conn, perfil)
    print(f"Tempo total assistido: {tempo.formatar_duracao(total)}")


def mostrar_mais_assistidos(conn):
    registros = banco_streaming.mais_assistidos(conn)

    print("\n===== MAIS ASSISTIDOS =====")

    if len(registros) == 0:
        print("Ainda não existem visualizações.")
    else:
        for titulo, total in registros:
            print(f"{titulo}: {total} visualização(ões)")


def mostrar_tempo_perfil(conn):
    registros = banco_streaming.tempo_por_perfil(conn)

    print("\n===== TEMPO POR PERFIL =====")

    if len(registros) == 0:
        print("Ainda não existem visualizações.")
    else:
        for perfil, minutos in registros:
            print(f"{perfil}: {tempo.formatar_duracao(minutos)}")


def menu():
    conn = banco_streaming.conectar()

    perfil = input("Nome do perfil: ").strip()

    while perfil == "":
        perfil = input("Digite um nome de perfil: ").strip()

    while True:
        print(f"\n===== CINEFLIX ({perfil}) =====")
        print("1 - Ver catálogo")
        print("2 - Registrar que assisti")
        print("3 - Meu histórico")
        print("4 - Mais assistidos")
        print("5 - Tempo assistido por perfil")
        print("6 - Exportar relatório JSON")
        print("7 - Trocar de perfil")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            mostrar_catalogo(conn)

        elif opcao == "2":
            registrar(conn, perfil)

        elif opcao == "3":
            mostrar_historico(conn, perfil)

        elif opcao == "4":
            mostrar_mais_assistidos(conn)

        elif opcao == "5":
            mostrar_tempo_perfil(conn)

        elif opcao == "6":
            print(banco_streaming.exportar_relatorio(conn))

        elif opcao == "7":
            perfil = input("Novo nome do perfil: ").strip()

            while perfil == "":
                perfil = input("Digite um nome de perfil: ").strip()

        elif opcao == "0":
            conn.close()
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
