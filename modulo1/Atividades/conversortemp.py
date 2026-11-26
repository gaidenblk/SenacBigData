# Tarefa 3 - Aula 08
# Conversor de Temperatura

print("==== Conversor de Temperaturas ====")

pergunta = input("Digite 1 para ir de C° a F° ou 2 para ir de F° a C°: ")

def celsius_para_fahrenheit(temp_c):
    f = (temp_c * 9/5) + 32
    return f

def fahrenheit_para_celsius(temp_f):
    c = (temp_f - 32) * 5/9
    return c

if pergunta == "1":
    temp = float(input("Informe a Temperatura em C°: "))
    conv = celsius_para_fahrenheit(temp)
    print(f"A conversão de {temp}C° é {conv:.2f}F°")
if pergunta == "2":
    temp = float(input("Informe a Temperatura em F°: "))
    conv = fahrenheit_para_celsius(temp)
    print(f"A conversão de {temp}F° é {conv:.2f}C°")
if pergunta != "1" and pergunta != "2":
    print("Nenhuma função selecionada, encerrando...")