""""
# recuperar informacao do usuario
userReply = input("Do you need to ship a package? (Enter yes or no) ")

# condicional com if (se)
if userReply == "yes":
    print("Nos podemos enviar o pacote!")
else:
    print("Por favor retorne depois")
"""

userReply = input("Digite stamps, envelope ou copy com quantidade: ")

if userReply == "stamps":
    print("Nos temos stamps")
elif userReply == "envelope":
    print("Nos temos envelope")
elif userReply == "copy":
    copies = input("Quantas copias voce deseja?")
    print("Aqui estao suas {} copias.".format(copies))
else:
    print("Obrigado, volte sempre!")