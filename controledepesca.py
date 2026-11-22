# Tarefa 1 - Aula 08
# Controle de Pesca

print("===== Calculo de taxa de multa do pescado =====")
print("Informe o peso em KG dos pescados ou digite 0 para finalizar o calculo")

pesodopescado = float(input("KG do pescado: "))

def calcular_multa(pesodopescado):
    multaacumulada = 0
    while pesodopescado != 0:
        multa = (pesodopescado - 100) *4

        if multa > 0:
            print(f"Multa do dia: R${multa}\n")
            multaacumulada += multa
        else:
            print("Sem multa para esse dia\n")

        pesodopescado = float(input("KG do pescado: "))

    print(f"Total de multa acumulada na semana: R${multaacumulada}")

calcular_multa(pesodopescado)