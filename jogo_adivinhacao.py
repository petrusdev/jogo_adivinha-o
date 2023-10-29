# Usando WHILE
from random import randint
from time import sleep

jogador = str(input('Informe seu nome:')).strip()
while True:
  # Variaveis
  tentativas = 3  #Limitador
  tentativas_atual = 1  #Contador
  numero_aleatorio = randint(0, 10)

  # Desenvolvimento.
  print('')
  print('=' * 14)
  print('--- Seja Bem Vindo {} ---'.format(jogador))
  print('Tente advinhar o número que estou pensando. entre 0 e 10')
  print('=' * 14)

  while tentativas_atual <= tentativas:
    chute = int(input('Qual número estou pensando? '))
    print('Estamos analisanddo...')
    sleep(2)
    if chute == numero_aleatorio:
      print('Você acertou !')
      break
    elif chute < numero_aleatorio:
      print('Você errou, o número que eu pensei era maior')
    else:
      print('Você errou, o número que eu pensei era menor')
    tentativas_atual += 1

  if tentativas_atual > tentativas:
    print('')
    print('Game Over, eu pensei no número {}'.format(numero_aleatorio))
    print('')

  jogar_novamente = input(
      'Digite 1 para jogar novamente, ou qualquer tecla para sair.')
  if jogar_novamente != '1':
    break
print('Obrigado por jogar comigo, até a proxima')