# -*- coding: cp1252 -*-
import random



def jogar():
    mensagem_de_abertura()
    palavra_secreta = carregamento_palavra_secreta()
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
    
    
    enforcou = False
    acertou = False
    erros = 0


    while(not enforcou and not acertou):
        
        chute = pede_chute()
       
        if(chute in palavra_secreta):
          marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
             erros += 1
             
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    

        if(acertou):
           imprime_mensagem_vencedor()
        else:
          imprime_mensagem_perdedor()
       



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


def pede_chute():
    chute = input ("Qual letra? ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
          for letra in palavra_secreta:
             if(chute == letra):
                   letras_acertadas[index] = letra
             index += 1


def imprime_mensagem_vencedor():
    print("________/|/|/|\|\")
    print("________(^O.O^)")
    print("________(.(_).)")
    print("________\..--../")
    print("_______/¯¯Y¯¯\.\")
    print("_______|..|.......\.\")
    print("_______|. \_......|\.\")
    print("________\__\.......|..\")
    print("_____(¯¯¯\..\_|/¯¯\_\_______oooooo__")
    print("______)===ººº=====0000=========);;;]")
    print("_____(____/¯¯¯\__/")
    print("_______/../__________\...\")
    print("__.__./._/____________\._.\__")
    print("_(______/____________(_____)")



def imprime_mensagem_perdedor(palavra_secreta):
                print("Você foi enforcado!")
                print("A palavra era {}".format(palavra_secreta))
                print("__________________________________________________")
                print("___________________¶¶¶¶¶¶¶¶¶¶¶¶¶__________________")
                print("______________¶¶¶¶¶¶________¶¶¶¶¶¶¶_______________")
                print("____________¶¶¶¶__________________¶¶¶¶____________")
                print("__________¶¶¶________________________¶¶¶__________")
                print("_________¶¶____________________________¶¶¶________")
                print("_______¶¶¶_______________________________¶¶_______")
                print("______¶¶__________________________________¶¶______")
                print("_____¶¶_____________________________________¶_____")
                print("____¶¶______________________________________¶¶____")
                print("___¶¶_______________________________¶________¶¶___")
                print("___¶¶_____________________________¶¶¶¶¶¶¶_____¶¶__")
                print("___¶¶____________________________¶¶_____¶¶_____¶__")
                print("___¶¶____________________________________¶¶____¶¶_")
                print("___¶¶¶¶__________________________________¶_____¶¶_")
                print("___¶¶¶¶¶¶________________________¶¶¶¶¶¶¶_¶¶_____¶_")
                print("__¶¶_____¶_________________¶¶____¶¶____¶_¶______¶_")
                print("_¶¶______________________________¶______________¶_")
                print("_¶¶___¶¶¶¶¶_____________¶¶_____¶¶¶¶¶¶___________¶_")
                print("__¶¶_¶__¶¶¶¶¶_____¶__¶¶¶____¶¶¶_____¶__¶¶_______¶_")
                print("___¶¶___¶___¶¶¶____¶¶¶____¶¶¶_______¶_¶¶_______¶¶_")
                print("_____¶¶¶¶¶____¶¶¶__¶¶¶¶_¶¶¶_________¶_¶¶_______¶__")
                print("_______¶¶¶_______¶¶¶__¶¶____________¶_¶¶______¶¶__")
                print("_______¶¶_¶______¶¶__¶_¶__________¶¶___¶_____¶¶___")
                print("_______¶¶___¶¶¶¶¶_¶__¶_¶¶¶¶_____¶¶¶____¶¶¶¶¶¶¶¶___")
                print("______¶¶__________¶¶¶¶¶___¶¶¶¶_¶¶____________¶¶___")
                print("______¶________¶_¶¶__¶¶¶¶¶________________¶¶¶¶____")
                print("______¶¶______¶¶¶______¶¶_¶¶____________¶¶¶¶______")
                print("_______¶¶______¶__________¶___________¶¶¶_¶_______")
                print("________¶¶¶_¶¶¶________________¶____¶¶¶___¶_______")
                print("_________¶¶¶__¶¶_____________¶¶¶¶¶¶¶¶_____¶_______")
                print("___________¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶______¶¶______")
                print("___________¶__¶_¶¶_¶¶¶_¶¶¶_¶¶¶____¶_______¶_______")
                print("___________¶¶_¶¶___¶_¶_¶_¶_¶__¶___¶______¶¶_______")
                print("____________¶¶_¶_¶¶¶__¶_¶¶¶_¶_¶__¶_____¶¶¶________")
                print("_____________¶__¶¶_¶__¶_¶_¶_¶¶¶¶¶_____¶¶__________")
                print("______________¶__¶_¶¶_¶_¶¶¶¶¶__¶¶____¶¶___________")
                print("______________¶¶____________________¶_____________")
                print("_______________¶¶__________________¶______________")
                print("_______________¶¶_________________¶_______________")
                print("_______________¶¶________________¶________________")
                print("________________¶_______________¶_________________")
                print("________________¶¶¶____________¶__________________")
                print("_________________¶¶¶¶¶¶¶¶¶__¶¶¶¶__________________")
                print("__________________________¶¶______________________")




if(__name__ == "__main__"):
        jogar()