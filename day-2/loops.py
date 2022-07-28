"""
# importar o modulo random
import random

print("Bem-vindo ao jogos de advinhar numeros")
print("Voce precisa advinhar qual numero e o correto!")

# gerar numero randomico entre 1-10
number = random.randint(1,10)

#print(number)

# variavel de controle
isGuessRight = False

# loop while
while isGuessRight != True:
    guess = input("Advinhe um numero entre 1 e 10: ")
    
    # condicional
    if int(guess) == number:
        print("Voce advinhou o numero {}.".format(guess))
        isGuessRight = True
    else:
        print("Voce digitou {}. Desculpas mas nao eh o numero correto".format(guess))
  
  """
  
# mostrar numeros de 1 a 10
for x in range(1,11):
    print(x)