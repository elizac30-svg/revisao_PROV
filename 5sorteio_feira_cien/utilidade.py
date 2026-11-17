
def ler_texto(mensagem, vazio=False):
    texto = input(mensagem)

    while texto.strip() == "" and not vazio:
        print("Digite alguma coisa.")
        texto = input(mensagem)

    return texto


def ler_inteiro(mensagem, minimo=None, maximo=None):
    numero = int(input(mensagem))

    while (minimo is not None and numero < minimo) or (maximo is not None and numero > maximo):
        if minimo is not None and numero < minimo:
            print(f"O mínimo é {minimo}.")
        elif maximo is not None and numero > maximo:
            print(f"O máximo é {maximo}.")

        numero = int(input(mensagem))

    return numero


def linha(caractere="-", tamanho=40):
    return caractere * tamanho


if __name__ == "__main__":

    print("=== TESTE DO MÓDULO ===")

    nome = ler_texto("Digite seu nome: ")
    print(nome)

    idade = ler_inteiro("Digite sua idade: ", 1, 120)
    print(idade)

    print(linha("=", 40))
