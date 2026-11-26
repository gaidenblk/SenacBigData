# Tarefa 1 - Aula 05

# Calculo de média para Vários Alunos
# Faremos uma repetição para 10 alunos

for i in range(10):
        print(f"Informe as notas do {i + 1}º aluno")
        nota1 = float(input("Digite a nota do primeiro Bimestre: "))
        nota2 = float(input("Digite a nota do segundo Bimestre: "))
        nota3 = float(input("Digite a nota do terceiro Bimestre: "))
        nota4 = float(input("Digite a nota do quarto Bimestre: "))
        print("------------------------------------------\n")

        # Com os dados das notas armazenados iniciaremos o processamento

        media = (nota1 + nota2 + nota3 + nota4) / 4

        # Agora vem a análise e apresentação do resultado

        if media >= 5 and media <= 7:
            print(f"Sua média foi de {media} Sua situação é RECUPERAÇÃO")
        elif media < 5:
            print(f"Sua média foi de {media} Sua situação é REPROVADO")
        else:
            print(f"Sua média foi de {media} Sua situação é APROVADO")

        print("==========================================\n")