# Tarefa 2 - Aula 08
# Calculadora de IMC

print("==== Calculadora de IMC ====")

peso = float(input("Informe seu peso em KG: "))
altura = float(input("Informe sua altura separando os cm com . : "))

def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

def obter_classificacao(imc):
    if imc < 18.5:
        print("Abaixo do peso")
    if imc >= 18.5 and imc < 24.9:
        print("Peso normal")
    if imc >= 25.0 and imc < 29.9:
        print("Sobrepeso")
    if imc >= 30.0:
        print("Obesidade")

obter_classificacao(calcular_imc(peso,altura))