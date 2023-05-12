from threading import *         
import time         
import random
import os

valid_options = ['S', 'C' , 'E' ]

player1Attacks = []
player2Attacks = []

def limpaTela():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

def bemVindo():
  print()
  print("----------------------------------")
  print("---- Bem vindo(a) ao RYG-BOSS ----")
  print("----------------------------------")
  print()

def regras():
  print ("----REGRAS DO JOGO:")
  print ()
  print ("1. Cada jogador escolhe uma sequência de 5 ataques.")
  print ("2. Existem 3 tipos de ataque: simples, combo e especial.")
  print ("3. Cada jogador possui apenas 1 ataque especial por partida.")
  print ("4. Cada jogador possui até 2 ataques combo por partida.")
  print ("5. Cada jogador possui até 5 ataques simples por partida. ")
  print()

def comoJogar():
  print ("----COMO JOGAR:")
  print()
  print("1. Cada jogador deve enviar uma sequência de ataques através dos caracteres S, C, E (simples, combo e especial respectivamente)")
  print("2. Cada caracter deve estar separado por um espaço")
  print("         exemplos: ")
  print("                 E S S S C")
  print("                 C S S S E")
  print()

def partidaComecou():
  print()
  print("----------------------------------")
  print("----- PARTIDA EM ANDAMENTO -------")
  print("----------------------------------")
  print()

def vezDoPlayer1():
  print()
  print("----------------------------------")
  print("-------- VEZ DO PLAYER 01 --------")
  print("----------------------------------")
  print()

def vezDoPlayer2():
  print()
  print("----------------------------------")
  print("-------- VEZ DO PLAYER 02 --------")
  print("----------------------------------")
  print()

def relatorioDaPartida():
  print()
  print("----------------------------------")
  print("------ RELATÓRIO DA PARTIDA ------")
  print("----------------------------------")
  print()

def verificaAtaquesInvalidos(playerAttacks):
  runAgain = False
  for attack in playerAttacks:
    if attack in valid_options:
       runAgain = runAgain
    else:
     print(attack + " não é uma opção válida!")
     runAgain = True
  return runAgain

def verificaQuantidadeInvalida(playerAttacks):
  if len(playerAttacks) < 5:
    print("Devem ser selecionados 05 ataques")
    return True
  elif len(playerAttacks) > 5:
    print("Devem ser selecionados 05 ataques")

    return True
  else:
    return False

def verificaLimitePorTipo(playerAttacks, tipo, limite):
  quantidade = 0
  for attack in playerAttacks:
    if attack == tipo:
      quantidade += 1
  
  if quantidade > limite:
    print("Você colocou ", quantidade, " ataques do tipo ", tipo,". O limite é: ", limite)
    return True
  else:
    return False

def attackPower(attack):
  if attack == "E":
    return 35
  elif attack == "C":
    return 25
  else:
    return 20

## ------------------------------------ START
limpaTela()

## ------------- TELA DE REGRAS --------------
bemVindo()
regras()
input("aperte uma enter para continuar")

limpaTela()

## ------------- TELA DE COMO JOGAR --------------
bemVindo()
comoJogar()
input("aperte uma enter para continuar")

limpaTela()

## ------------- TELA DA VEZ DO PLAYER 1 --------------
valid1 = True
while valid1:
  limpaTela()
  vezDoPlayer1()

  #RECEBE OS ATAQUES DO PLAYER 1
  print ("----PLAYER 1: selecione sua sequência de ataques --")
  player1Attacks = input().split()

  quantidadeInvalida = verificaQuantidadeInvalida(player1Attacks)
  ataquesInvalidos = verificaAtaquesInvalidos(player1Attacks)
  limiteAtaqueE = verificaLimitePorTipo(player1Attacks, "E", 1)
  limiteAtaqueC = verificaLimitePorTipo(player1Attacks, "C", 2)
  limiteAtaqueS = verificaLimitePorTipo(player1Attacks, "E", 5)

  if quantidadeInvalida == True or ataquesInvalidos == True or limiteAtaqueE == True or limiteAtaqueC == True or limiteAtaqueS == True:
    valid1 = True
  else:
    valid1 = False

  time.sleep(2)

print()
input("Ataques Válidos!! Aperte uma enter para continuar.")


## -----------------------RECEBE OS ATAQUES DO PLAYER 2
valid2 = True
while valid2:
  limpaTela()
  vezDoPlayer2()

  print ("----PLAYER 2: selecione sua sequência de ataques --")
  player2Attacks = input().split()

  quantidadeInvalida = verificaQuantidadeInvalida(player2Attacks)
  ataquesInvalidos = verificaAtaquesInvalidos(player2Attacks)
  limiteAtaqueE = verificaLimitePorTipo(player2Attacks, "E", 1)
  limiteAtaqueC = verificaLimitePorTipo(player2Attacks, "C", 2)
  limiteAtaqueS = verificaLimitePorTipo(player2Attacks, "E", 5)

  if quantidadeInvalida == True or ataquesInvalidos == True or limiteAtaqueE == True or limiteAtaqueC == True or limiteAtaqueS == True:
    valid2 = True
  else:
    valid2 = False

  time.sleep(2)

print()
input("Ataques Válidos!! Aperte uma enter para continuar.")

limpaTela()
## ------- CONTROLE DA CONDIÇÃO DE CORRIDA ---------------

obj = Semaphore(1)  

ordemDeAtaquePorRodada = []

## attackOrder é a função de acesso à zona crítica que é a lista de ordem
def defineQuemConsegueAtacar(jogador):
  time.sleep(random.random())
  obj.acquire() 
  for i in range(5):
    if len(ordemDeAtaquePorRodada) < 5:
      ordemDeAtaquePorRodada.append(jogador)
    time.sleep(random.random())
    obj.release() 

## declara as duas threads, cada uma refrente a um player
t1= Thread(target= defineQuemConsegueAtacar, args= ("p1",))
t2= Thread(target= defineQuemConsegueAtacar, args= ("p2",))

## inicia as duas threads, cada uma refrente a um player
t1.start()
t2.start()

## espera as duas threads trminarem para dar continuidade ao código
t1.join()
t2.join()


## ----------- PROCESSAMENTO DO JOGO
danoInfligidoPeloPlayer1 = 0
danoInfligidoPeloPlayer2= 0
pontosDeVidaDoBoss = 100
jogadorQueDeuAtaqueFatal = ""
jogadorQueInfligiuMaisDano = ""

pontosPlayer1 = 0
pontosPlayer2 = 0


relatorioDaPartida()
print("-------- DANO POR RODADA")
print()

for i in range(0,5):
  turn = ordemDeAtaquePorRodada[i]
  if turn == "p1":
    ataque = attackPower(player1Attacks[i])
    pontosDeVidaDoBoss-= ataque
    danoInfligidoPeloPlayer1 += ataque
    print("Round ", i + 1," - player 1 atacou infligindo", ataque, "de dano no Boss. Pontos de vida do Boss após o ataque:", pontosDeVidaDoBoss)
    if pontosDeVidaDoBoss <= 0:
      jogadorQueDeuAtaqueFatal = "p1"
      break
  else:
    ataque = attackPower(player1Attacks[i])
    pontosDeVidaDoBoss-= ataque
    danoInfligidoPeloPlayer2 += ataque
    print("Round ", i + 1," - player 2 atacou infligindo", ataque, "de dano no Boss. Pontos de vida do Boss após o ataque:", pontosDeVidaDoBoss)
    if pontosDeVidaDoBoss <= 0:
      jogadorQueDeuAtaqueFatal = "p2"
      break

print()
print("------- DANO TOTAL")
print("Player 1 infligiu", danoInfligidoPeloPlayer1, " de dano.")
print("Player 2 infligiu", danoInfligidoPeloPlayer2, " de dano.")

if danoInfligidoPeloPlayer1 > danoInfligidoPeloPlayer2:
  jogadorQueInfligiuMaisDano = "p1"
  pontosPlayer1 += 40
  print("Player 1 infligiu mais dano no Boss")
else:
  jogadorQueInfligiuMaisDano = "p2"
  pontosPlayer2 += 40
  print("Player 2 infligiu mais dano no Boss")

if jogadorQueDeuAtaqueFatal == "p1":
  pontosPlayer1 += 30
  print("Player 1 deu o dano fatal no Boss")
else:
  pontosPlayer2 += 30
  print("Player 2 deu o dano fatal no Boss")


pontosPlayer1 += danoInfligidoPeloPlayer1
pontosPlayer2 += danoInfligidoPeloPlayer2

print()
print("------- PONTUAÇÃO")
print("Player 1:", pontosPlayer1)
print("Player 2:", pontosPlayer2)
if pontosPlayer1 > pontosPlayer2:
  print("Player 1 ganhou!")
else:
  print("Player 2 ganhou!")









