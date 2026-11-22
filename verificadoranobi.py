# Tarefa 4 - Aula 08
# Verificador de Ano Bissexto

print("==== Verificardo de Ano Bissexto ====")
ano = int(input("Informe o ano no formato XXXX: "))

def eh_bissexto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

resultado = eh_bissexto(ano)

if resultado:
    print(f"O ano {ano} É bissexto")
else:
    print(f"O ano {ano} NÂO é bissexto")