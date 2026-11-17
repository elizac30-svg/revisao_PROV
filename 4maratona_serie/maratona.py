def formatar_duracao(minutos):
    horas = minutos // 60
    resto = minutos % 60

    if horas > 0:
        return f"{horas}h{resto:02d}min"
    else:
        return f"{resto}min"

HGFTVHG
def tempo_total(duracoes):
    total = 0

    for minutos in duracoes:
        total += minutos

    return total


def dias_para_terminar(total_minutos, minutos_por_dia=120):
    dias = total_minutos // minutos_por_dia

    if total_minutos % minutos_por_dia != 0:
        dias += 1

    return dias


def classificar_maratona(total_minutos):
    if total_minutos < 300:
        return "Leve"
    elif total_minutos <= 900:
        return "Média"
    else:
        return "Intensa"



if __name__ == "__main__":

    print("=== MARATONA DE SÉRIE ===")

    nome = input("Nome da série: ")
    temporadas = int(input("Quantas temporadas? "))

    duracoes = []

    for i in range(1, temporadas + 1):

        episodios = int(input(f"Temporada {i} - número de episódios: "))
        duracao = int(input(f"Temporada {i} - duração média do episódio (min): "))

        total_temporada = episodios * duracao

        duracoes.append(total_temporada)

    total = tempo_total(duracoes)

    print(f"=== {nome.upper()} ===")

    for i in range(len(duracoes)):
        print(f"Temporada {i + 1}: {formatar_duracao(duracoes[i])}")

    print(f"Total: {formatar_duracao(total)} ({classificar_maratona(total)})")

    minutos_dia = int(input("Quantos minutos por dia você pode assistir? "))

    while minutos_dia <= 0:
        print("Digite um valor maior que zero.")
        minutos_dia = int(input("Quantos minutos por dia você pode assistir? "))

    dias = dias_para_terminar(total, minutos_dia)
    dias_padrao = dias_para_terminar(total)

    print(f"Você termina {nome} em {dias} dias.")
    print(f"Com 2 horas por dia (padrão), seriam {dias_padrao} dias.")
