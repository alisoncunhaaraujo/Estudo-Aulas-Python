# -*- coding: cp1252 -*-
import random



def jogar():
   
    mensagem_de_abertura()
    palavra_secreta = carregamento_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        
        chute = input ("Qual letra? ")
        chute = chute.strip().upper()
       
        if(chute in palavra_secreta):
          index = 0
          for letra in palavra_secreta:
             if(chute == letra):
                   letras_acertadas[index] = letra
             index += 1
        else:
             erros += 1
             
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    

        if(acertou):
           print("Voce acertou")
        else:
          print("Voce errou")
        
        if(enforcou == True):
            print("Fim do jogo")




def inicializa_letras_acertadas(palavra):
   return ["_" for letra in palavra]

def mensagem_de_abertura():
    print("********************************")
    print("***Bem vindo ao jogo de Forca***")
    print("********************************")

def carregamento_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta










if(__name__ == "__main__"):
        jogar()