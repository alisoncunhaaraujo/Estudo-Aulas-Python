# -*- coding: cp1252 -*-
import forca
import adivinhacao

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")


print ("(1) Forca      (2)Adivinha��o")
jogo = int(input("Qual jogo voc� quer jogar?"))

if(jogo == 1):
    print("Jogando forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando adivinha��o")
    adivinhacao.jogar()
            