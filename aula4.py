numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print("Tentativa de {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o numero: ")
    print ("Voce digitou" , chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute >  numero_secreto
    menor   = chute <  numero_secreto

    if(acertou):
        print("Voce acertou")
    else: 
        if(maior):
            print("Voce errou, seu chute foi maior que o numero secreto.")
        elif(menor):
            print("Voce acertou, seu chute foi menor que o numero secreto.")

rodada = rodada + 1

