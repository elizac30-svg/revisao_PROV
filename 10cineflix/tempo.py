def formatar_duracao(minutos):
    horas = minutos // 60
    resto = minutos % 60

    if horas > 0:
        return f"{horas}h{resto:02d}min"
    else:
        return f"{resto}min"
