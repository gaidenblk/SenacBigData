# Tarefa 2 - Aula 04
# Calcular a quantidade de caixas de azulejos

comprimento = float(input("Informe o Comprimento da Sala: "))
largura = float(input("Informe a Largura da Sala: "))
altura = float(input("Informe a Altura da Sala: "))

areatotal = ((comprimento * altura) + (largura * altura)) *2

resultado = areatotal / 1.5

print(f"A quantidade de caixas necessárias é: ",resultado)