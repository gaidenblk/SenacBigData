# Tarefa 5 - Aula 04
# Media do aluno com Optativa

n1 = float(input("Informe a primeira nota do Aluno: "))
n2 = float(input("Informe a segunda nota do Aluno: "))
nopt = input("O aluno fez a avaliação Optativa? (s/n): ")
if nopt == "s":
    nopt = float(input("Informe a nota: "))
else:
    nopt = -1

if n1 < n2 and nopt > n1:
    n1 = nopt
elif n2 < n1 and nopt > n2:
    n2 = nopt

notamedia = (n1 + n2) / 2

if notamedia >= 6:
    print(f"O aluno está APROVADO! Média: {notamedia}")
if notamedia >= 3 and notamedia < 6:
    print(f"O aluno está em RECUPERAÇÃO! Média: {notamedia}")
if notamedia < 3:
    print(f"O aluno está REPROVADO! Média: {notamedia}")


