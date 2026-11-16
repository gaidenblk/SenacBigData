# Tarefa 1 - Aula 04
# Cálculo de lâmpadas

pwlampadas = int(input("Informe a potência da lâmpada: "))
largura = int(input("Informe a largura do cômodo: "))
comprimento = int(input("Informe o comprimento do cômodo: "))

area = largura * comprimento

resultado = round((area * 3) / pwlampadas)

print(f"A quantidade de lâmpadas necessária é: ",resultado)