from datetime import datetime


def converter_data(texto):
    return datetime.strptime(texto, "%d/%m/%Y").date()


def dias_de_atraso(data_prevista, data_devolucao):
    dias = (data_devolucao - data_prevista).days

    if dias < 0:
        return 0
    else:
        return dias


def valor_multa(dias, por_dia=1.50, maximo=30.00):
    multa = dias * por_dia

    if multa > maximo:
        multa = maximo

    return multa


if __name__ == "__main__":

    print("=== TESTES DO MÓDULO ===")

    data1 = converter_data("05/11/2026")
    data2 = converter_data("10/11/2026")

    print("Data:", data1)
    print("Dias de atraso:", dias_de_atraso(data1, data2))
    print("Multa:", valor_multa(5))
    print("Multa máxima:", valor_multa(40))
    print("Multa personalizada:", valor_multa(5, por_dia=2))
