# -*- coding: cp1252 -*-
import forca
import adivinhacao

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")


print ("(1) Forca      (2)Adivinhacao")
jogo = int(input("Qual jogo voce quer jogar?"))

if(jogo == 1):
    print("Jogando forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando adivinhacao")
    adivinhacao.jogar()
            
if(__name__ == "__main__"):
     forca.jogar()