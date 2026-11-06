# Tarefa 2 - Criação de calculadora

# Nessa tarefa receberemos os inputs do usuário e 
# calcularemos os dois valores distintos em soma, subtração, divisão, multiplicação e módulo 
# Primeiro recebemos os inputs e armazenamos em variáveis para serem processadas

input1 = input("Insira o primeiro número: ")
input2 = input("Insira o segundo número: ")
if input1.replace(".", "", 1).isdecimal() and input2.replace(".", "", 1).isdecimal():
   c_input1 = float(input1)
   c_input2 = float(input2)
else:
    print("=============================================")
    print("Por favor insira um número válido")
    print("Tente novamente!")
    exit() # encerra a execução

# Haja visto que ao receber os inputs eles vêm como string
# e precisamos converter em número para o processamento funcionar
# e também pode haver a necessidade de validação dos dados para que
# tenhamos certeza de que vamos receber um número de fato

# Após validado, processamos e mostramos os valores

soma = c_input1 + c_input2
subtr = c_input1 - c_input2
mult = c_input1 * c_input2
modulo = c_input1 % c_input2

print("=============================================")
print("Resultados \n")
print(f"O resultado da soma de" ,c_input1, "e" ,c_input2, "é:" ,soma)
print(f"O resultado da subtração de" ,c_input1, "e" ,c_input2, "é:" ,subtr)
print(f"O resultado da multiplicação de" ,c_input1, "e" ,c_input2, "é:" ,mult)
print(f"O resultado do módulo de" ,c_input1, "e" ,c_input2, "é:" ,modulo)
