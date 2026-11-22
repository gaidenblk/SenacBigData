# Tarefa 3 - Aula 05
# Sistema de Login com tentativa limitada

user = "usuario"
senha = "senha123"

print("====== Login de Usuário ======")
print("Para acessar, por favor informe nome de usuário e senha")

userinpt = ""
senhainpt = ""
maxtentativas = 3

while userinpt != user and senhainpt != senha:
    if maxtentativas < 1:
        print("Tentativas excedidas! Encerrando Aplicação...")
        exit()
    
    userinpt = input("Nome de usuário: ")
    senhainpt = input("Informe a senha: ")

    if userinpt != user and senhainpt != senha:
        maxtentativas-= 1
        print("Usuário ou senha incorretos!")
        print(f"Você tem mais {maxtentativas} tentativas!\n")

print(f"Bem vindo {user}!")