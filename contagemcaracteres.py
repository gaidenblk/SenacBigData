# Tarefa 5 - Aula 08
# Contagem de Caracteres

print("==== Contagem de Caracteres em Especifico ====")

texto = input("Informe o texto desejado para contagem: ").lower()
carac = input("Informe o caractere procurado: ").lower()

def contar_caractere(texto, carac):
    total_carac = 0
    for i in texto:
        if i == carac:
            total_carac += 1
    return total_carac

caracteres = contar_caractere(texto,carac)

print(f"Total de caracateres encontrados: {caracteres}")