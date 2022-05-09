from ast import If


print ("********************************")
print ("Bem vindo ao jogo de adivinhação")
print ("********************************")

numero_secreto = 42

chute_str = input("Digite o numero: ")

print ("Voce digitou" , chute_str)

chute = int(chute_str)

if (numero_secreto == chute):
    print("Voce acertou")
else: 
    if(chute > numero_secreto):
        print("Voce errou, seu chute foi maior que o numero secreto")
    elif(chute < numero_secreto):
        print("Voce acertou, seu chute foi menor que o numero secreto")



print("Fim do jogo")