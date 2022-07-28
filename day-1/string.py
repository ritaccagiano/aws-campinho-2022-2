""""
string1 = "Minha"
string2 = "String"
string3 = "eh um numero"

strings = string1 + string2 + string3

print(string1)
print(string2)
print(string3)
print(strings)
"""

# comentario em uma linha

# solicitar ao usuario para digitar o nome
user = input("Qual eh o seu nome?")

# mostrar o nome que o usuario digitou
print("Seu nome eh: " + user) # concatenacao com +
print("Meu nome eh: {}".format(user)) # concatenacao com o .format