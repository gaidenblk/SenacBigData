# Tarefa 1 - Criação de sistema de Boletim classificatório

# Primeiro coletamos os dados das notas e 
# armazenamos em variáveis para serem processadas posteriormente

nota1 = 6.5
nota2 = 7.8
nota3 = 6.8
nota4 = 5.6

# Com os dados das notas armazenados iniciaremos o processamento

media = (nota1 + nota2 + nota3 + nota4) / 4

# Agora vem a análise e apresentação do resultado

if media < 7:
    print(f"Sua média foi de", media, "Sua situação é REPROVADO")
else:
    print(f"Sua média foi de", media, "Sua situação é APROVADO")