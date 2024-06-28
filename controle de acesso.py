#Gabriel Martins, Kevyn Cardoso, Vitor dos Santos
#Criando a conta
print("Vamos criar a conta")
print("Digite seu nome de usuario" )
usuario=input()
print("Digite uma senha ")
senha=input()
print("repita a sua senha")
senha=input()
#Logando na conta
print("Entrar na conta")
print("Digite o seu usuário")
usuario=input()
print("digite a sua senha")
senha2=input()
if senha2==senha:
    print("Bem vindo,"+usuario)
else:
    print("senha incorreta")
