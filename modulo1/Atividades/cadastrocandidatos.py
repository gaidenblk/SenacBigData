# Tarefa 2 - Aula 05
# Cadastro de candidatos
# Coleta de dados de usuarios maiores de 18 anos considerando o ano atual 2026

print("Cadastro de Usuários Maiores de 18 anos...\n")

qtdcadastrada = 0

while qtdcadastrada < 12:
    idade = 2026 - int(input("Informe o Ano do seu Nascimento no formato XXXX: "))

    if idade > 17:
        nome = input("Informe seu  primeiro nome: ")
        telefone = input("Informe seu Telefone com DDD: ")

        print(f"Cadastro Efetuado com Sucesso!", idade, nome, telefone)
        qtdcadastrada += 1
        print(f"Quantidade cadastrada até agora: {qtdcadastrada}\n")
    else:
        print("Você não tem idade para permissão do cadastro!")
        print(f"Quantidade cadastrada até agora: {qtdcadastrada}\n")
    