# Tarefa 3 - Aula 04
# Calculando o rendimento do Taxista

precocombustivel = 6.15 # Valor em Reais R$
kminicial = float(input("Informe o Km inicial do odômetro: "))
kmfinal = float(input("Informe o Km final do odômetro: "))
combustivelusado = float(input("Informe a quantidade de combustel consumido no dia: "))
totalarrecadado = float(input("Informe a quantia total recebida dos passageiros no dia: "))

totalkmrodado = kmfinal - kminicial
eficienciacombustivel = totalkmrodado / combustivelusado
gastocombustivel = combustivelusado * precocombustivel
lucrototal = round(totalarrecadado - gastocombustivel,2)

print("==============================================")
print(f"Eficiência combustível : {eficienciacombustivel}Km/l")
print(f"Kilometragem rodada no dia: {totalkmrodado}Km")
print(f"Valor gasto com combustível: R${gastocombustivel}")
print(f"Lucro total/dia: R${lucrototal}")
