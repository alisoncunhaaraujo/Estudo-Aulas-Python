from ast import If


print ("********************************")
print ("Bem vindo ao jogo de adivinhação")
print ("********************************")

numero_secreto = 42

chute_str = input("Digite o numero: ")

print ("Voce digitou" , chute_str)

chute = int(chute_str)

acertou = chute == numero_secreto
maior   = chute >  numero_secreto
menor   = chute <  numero_secreto

if (acertou):
    print("Voce acertou")
else: 
    if  (maior):
        print("Voce errou, seu chute foi maior que o numero secreto")
    elif(menor):
        print("Voce acertou, seu chute foi menor que o numero secreto")



print("Fim do jogo")