### CONTEXTO 1 (uso do operador AND):

'''
Para que eu possa dirigir, eu preciso ter:
- documento (CNH) em posse;
- maioridade (+18 anos);
- não estar alcoolizado.
'''

pergunta1 = input("Você tem os documentos em mãos?")
pergunta2 = int(input("Qual a sua idade?"))
pergunta3 = input("Você consumiu bebida alcoólica antes de dirigir?")

if pergunta1 == "sim" and pergunta2 >= 18:
    print("Pode dirigir.")
elif pergunta1 == "sim" and  pergunta3 == "sim":
    print("Não pode dirigir.")


### CONTEXTO 2 (uso do operador OR):

'''
Para me deslocar até o SENAC Nova Iguaçu, posso utilizar:
- trem;
- ônibus;
- metrô.
'''

trem = input("Você veio de trem?")
busao = input("Você veio de ônibus?")
metro = input("Você veio de metrô?")

if trem == "sim" or busao == "sim" or metro == "sim":
    print("Bem-vindo(a) ao SENAC!")
else:
    print("Tarifa dinâmica, né? :( )")