# -*- coding: cp1252 -*-
def jogar():
    print("********************************")
    print("***Bem vindo ao jogo de Forca***")
    print("********************************")
    
    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        
        chute = input ("Digite uma letra")

        for letra in palavra_secreta:
             if(chute == letra):
                print(letra)
        
        print("jogando")
 
    if(__name__ == "__main__"):
         jogar()
