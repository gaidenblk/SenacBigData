# Tarefa 6 - Aula 08
# Simulador de Dado

import random

print("==== Simulador de Batalha ====")

def rolar_dado(lados):
    return random.randint(1, lados)

pergunta = input("Vamos iniciar a rolagem de dados?: (s/n) ").lower()

while pergunta == "s":
    pergunta = input("Rolar para o Ataque (d20)?: ").lower()
    if pergunta == "s":
        print(f"Total de Dano causado: {rolar_dado(20)}\n")

    pergunta = input("Rolar para o Dano (d8)?: ").lower()
    if pergunta == "s":
        print(f"Total de Dano causado: {rolar_dado(8)}\n")

    pergunta = input("Deseja continuar?: (s/n) ").lower()

print("Encerrando aplicação...")