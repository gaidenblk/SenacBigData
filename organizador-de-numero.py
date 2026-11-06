# Tarefa 3 - Organizador numérico

# Ao receber três números independente da ordem, o sistema os organiza e mostra em ordem crescente

n1 = int(input("Insira o primeiro número: ")) # Sem validação, considerando que receberemos um número de fato
n2 = int(input("Insira o segundo número: ")) # Sem validação, considerando que receberemos um número de fato
n3 = int(input("Insira o terceiro número: ")) # Sem validação, considerando que receberemos um número de fato

if n1 > n2:
    if n1 > n3:
        if n3 > n2:
            print(n3)
            print(n2)
            print(n1)