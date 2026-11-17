
def subtotal_item(preco, quantidade=1):
    return preco * quantidade


def aplicar_cupom(total, cupom):
    cupom = cupom.strip().upper()

    if cupom == "PROMO10":
        percentual = 10
    elif cupom == "VOLTAASAULAS":
        percentual = 15
    elif cupom == "BLACK25":
        percentual = 25
    else:
        percentual = 0

    novo_total = total * (1 - percentual / 100)

    return novo_total, percentual


def calcular_frete(total, gratis_acima=200.0, valor=25.0):
    if total >= gratis_acima:
        return 0.0
    else:
        return valor


def valor_parcela(total, parcelas=1):
    if parcelas <= 6:
        return total / parcelas
    else:
        return total * (1 + 0.02 * parcelas) / parcelas


# PROGRAMA PRINCIPAL
if __name__ == "__main__":

    print("=== LOJA VIRTUAL ===")

    carrinho = 0.0

    while True:
        produto = input("Produto (Enter para fechar o carrinho): ")

        if produto == "":
            break

        preco = float(input("Preço: R$ "))

        while preco <= 0:
            print("Digite um valor maior que zero.")
            preco = float(input("Preço: R$ "))

        quantidade = int(input("Quantidade: "))

        while quantidade <= 0:
            print("Digite um valor maior que zero.")
            quantidade = int(input("Quantidade: "))

        item = subtotal_item(preco, quantidade)
        carrinho += item

        print(f"{quantidade} x {produto} = R$ {item:.2f} (carrinho: R$ {carrinho:.2f})")

    cupom = input("Cupom de desconto (Enter se não tiver): ")

    total_desconto, percentual = aplicar_cupom(carrinho, cupom)

    if cupom.strip() != "" and percentual == 0:
        print("Cupom inválido.")

    desconto = carrinho - total_desconto

    frete = calcular_frete(total_desconto)

    parcelas = int(input("Em quantas parcelas (1 a 12)? "))

    while parcelas < 1 or parcelas > 12:
        print("Digite um número entre 1 e 12.")
        parcelas = int(input("Em quantas parcelas (1 a 12)? "))

    total = total_desconto + frete
    parcela = valor_parcela(total, parcelas)

    print("=== NOTA ===")
    print(f"Subtotal: R$ {carrinho:.2f}")
    print(f"Desconto: {percentual}% (R$ {desconto:.2f})")
    print(f"Frete: R$ {frete:.2f}")
    print(f"Total: R$ {total:.2f}")
    print(f"Pagamento: {parcelas} x R$ {parcela:.2f}")
