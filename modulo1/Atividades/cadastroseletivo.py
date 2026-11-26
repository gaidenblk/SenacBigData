# Tarefa 2 - Aula 06
# Cadastro de candidatos com lista e dicionario
# Coleta de dados de usuarios maiores de 18 anos considerando o ano atual 2026

print("Cadastro de Usuários Maiores de 18 anos...\n")

qtdcadastrada = 0
candidatos_validos = []

while qtdcadastrada < 5:
    candidato = {}
    idade = 2026 - int(input("Informe o Ano do seu Nascimento no formato XXXX: "))

    if idade > 17:
        candidato["nome"] = input("Informe seu  primeiro nome: ")
        candidato["idade"] = idade
        candidato["telefone"] = input("Informe seu Telefone com DDD: ")

        print(f"Cadastro Efetuado com Sucesso!", idade, candidato["nome"], candidato["telefone"])
        candidatos_validos.append(candidato)
        qtdcadastrada += 1
        print(f"Quantidade cadastrada até agora: {qtdcadastrada}\n")
    else:
        print("Você não tem idade para permissão do cadastro!")
        print(f"Quantidade cadastrada até agora: {qtdcadastrada}\n")

print("Processo de cadastro finalizado!")
print("Lista de candidatos aprovados:")
print(candidatos_validos)