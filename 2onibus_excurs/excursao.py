'''Questão 2 - Ônibus da excursão

#laços #decisão
Arquivo(s): excursao.py

A escola vai fazer uma excursão. Cada ônibus tem 44 lugares e custa R$ 1.800,00. Vai um
professor para cada 15 alunos (arredondando para cima: 16 alunos precisam de 2 professores), e
os professores também ocupam lugar no ônibus.

O programa deve:

1. Perguntar quantas turmas vão participar (número inteiro maior que zero).
2. Com um laço for, pedir o nome e o número de inscritos de cada turma (inteiro, 0 ou mais).
3. Mostrar: total de alunos, professores acompanhantes, total de pessoas, ônibus necessários,
lugares que sobram, custo total, valor que cada aluno paga e a turma com mais inscritos.

Dica: Para dividir arredondando para cima sem usar math: (a + b - 1) // b. Por exemplo, (95 +
14) // 15 dá 7 professores. O valor por aluno é o custo total dividido só pelos alunos (os professores
não pagam).'''

def controlar_excursao():

    onibus = []
    turmas = []

    max_lugares = 44
    valor_viagem = 1800.0

    
    while True:
        try:
            qtd_turmas = int(input("Quantas turmas vão participar? ").strip())
            if qtd_turmas <= 0:
                print("[Número inválido! O número deve ser maior que 0.]")
            else:
                break
        except ValueError:
            print("[Entrada inválida! Digite um número inteiro.]")

    
    for i in range(qtd_turmas):
        while True: 
            nome = input("Digite o nome da turma: ").strip()

            if not nome:
                print("O nome não pode estar vazio.") 
                continue
            else:
                break 
            
        while True:
            try: 
                inscritos = int(input("Digite o número de inscritos da turma: ").strip())

                if inscritos < 0: 
                    print("[Número inválido! O número deve ser 0 ou mais.]")
                else: 
                    break
            except ValueError:
                print("[Entrada inválida! Digite um número inteiro.]")

        
        turmas.append(nome)
        onibus.append(inscritos)

    
    total_alunos = sum(onibus)
    maior_alunos = max(onibus)
    turma_maior = turmas[onibus.index(maior_alunos)]

    professores = (total_alunos + 14) // 15
    total_pessoas = total_alunos + professores

    num_onibus = (total_pessoas + 43) // 44
    rest_lugares = (num_onibus * max_lugares) - total_pessoas
    custo_total = num_onibus * valor_viagem

    if total_alunos > 0:
        total_pagamento_por_aluno = custo_total / total_alunos
    else:
        total_pagamento_por_aluno = 0.0

    print("--RESUMO DA EXCURSÃO--")
    
    print(f"Total de alunos: {total_alunos}")
    print(f"Professores: {professores}")
    print(f"Total de pessoas: {total_pessoas}")
    print(f"Ônibus necessários: {num_onibus}")
    print(f"Lugares que sobram: {rest_lugares}")
    print(f"Custo total: R$ {custo_total:.2f}")
    print(f"Valor por aluno: R$ {total_pagamento_por_aluno:.2f}")
    print(f"Turma com mais inscritos: {turma_maior}")

controlar_excursao()