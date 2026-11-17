'''*Questão 1 — Mochila de camping*

#laços #decisão
Arquivo(s): mochila.py
A turma vai acampar, e cada mochila pode ter no máximo 15 kg. Faça um programa que ajude a
montar a mochila.
O programa deve:

1. Pedir o nome e o peso (kg) de cada item, repetindo até a pessoa digitar FIM (em maiúsculas
ou minúsculas).
2. Aceitar o peso com vírgula ou ponto (3,2 ou 3.2). Se o peso não for um número, ou for zero
ou negativo, avisar e perguntar de novo.
3. Avisar, no momento em que acontecer, que o peso total passou de 15 kg.
4. No final, mostrar a lista numerada dos itens, a quantidade de itens, o peso total, o peso
médio, o item mais pesado e quanto é preciso tirar (ou quanto ainda cabe) na mochila.
5. Se nenhum item for digitado, mostrar "A mochila está vazia." sem dar erro.

Dica: float(texto.replace(",", ".")) converte "3,2" em 3.2. Para não parar com erro quando a
pessoa digita letras, use try: / except ValueError:. Guarde nomes e pesos em duas listas para
mostrar o resumo no final.'''

def pedir_peso():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
  while True:
    nome = input("Digite o nome do seu item: ")
    while(True):
      peso = float(input("Digite o peso do seu item (em kg): "))
      if peso == 0:
              peso == False
              print("Por favor, digite um número válido para o peso.")
              return
      elif peso < 0:
              print("Por favor, digite um número válido para o peso.")
              return
      elif ValueError:
              print("Por favor, digite um número válido para o peso.")
      elif peso > 15:
              print("[Valor superior a 15kg]")
      else:
           break
      
pedir_peso()
