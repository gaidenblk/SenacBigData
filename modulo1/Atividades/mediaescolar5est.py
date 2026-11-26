# Tarefa 1 - Aula 06

# Calculo de média para 5 Estudantes
# Faremos uma repetição para 5 alunos
# Depois retornaremos uma lista com os resultados

resultados = {}

for i in range(5):
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
        resultados[f"Aluno {i+1}"] = "RECUPERAÇÃO"
    elif media < 5:
        resultados[f"Aluno {i+1}"] = "REPROVADO"
    else:
        resultados[f"Aluno {i+1}"] = "APROVADO"
print("========================================")
print("Resultados: \n")
print(resultados)