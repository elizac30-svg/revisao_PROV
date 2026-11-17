import utilidades
import random
import datetime

print(utilidades.linha("="))
print("SORTEIO DE BRINDES - FEIRA DE CIÊNCIAS")
print(utilidades.linha("="))

participantes = []

print("Digite os nomes dos participantes (Enter vazio para terminar).")

while True:
    nome = utilidades.ler_texto(
        f"Participante {len(participantes) + 1}: ",
        vazio=True
    )

    if nome == "":
        break

    if nome.lower() in [p.lower() for p in participantes]:
        print(f"{nome} já está na lista.")
    else:
        participantes.append(nome)

quantidade = utilidades.ler_inteiro(
    f"Quantos brindes (1 a {len(participantes)})? ",
    1,
    len(participantes)
)

brindes = []

for i in range(1, quantidade + 1):
    brinde = utilidades.ler_texto(f"Brinde {i}: ")
    brindes.append(brinde)

ganhadores = random.sample(participantes, quantidade)

data = datetime.datetime.now().strftime("%d/%m/%Y às %H:%M")

print(utilidades.linha("-"))
print(f"Sorteio realizado em {data}")
print(f"{len(participantes)} participantes, {quantidade} brindes")
print(utilidades.linha("-"))

for i in range(quantidade):
    print(f"{brindes[i]} -> {ganhadores[i]}")
