
import multas
from datetime import date

print("=== BALCÃO DE DEVOLUÇÕES ===")

quantidade = 0
com_atraso = 0
total_multas = 0.0

while True:

    titulo = input("Título do livro (Enter para encerrar): ")

    if titulo == "":
        break

    while True:
        texto = input("Data prevista (dd/mm/aaaa): ")

        try:
            data_prevista = multas.converter_data(texto)
            break
        except ValueError:
            print("Data inválida. Use o formato dd/mm/aaaa.")

    while True:
        texto = input("Data da devolução (Enter = hoje): ")

        if texto == "":
            data_devolucao = date.today()
            break

        try:
            data_devolucao = multas.converter_data(texto)
            break
        except ValueError:
            print("Data inválida. Use o formato dd/mm/aaaa.")

    dias = multas.dias_de_atraso(data_prevista, data_devolucao)

    quantidade += 1

    if dias == 0:
        print(f"'{titulo}' devolvido no prazo. Obrigado!")
    else:
        multa = multas.valor_multa(dias)

        com_atraso += 1
        total_multas += multa

        print(f"'{titulo}' com {dias} dia(s) de atraso. Multa: R$ {multa:.2f}")

print("=== FECHAMENTO DO DIA ===")
print(f"Livros devolvidos: {quantidade}")
print(f"Com atraso: {com_atraso}")
print(f"Total em multas: R$ {total_multas:.2f}")
