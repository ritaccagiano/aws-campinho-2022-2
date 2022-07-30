from datetime import datetime
import pytz

pessoa = input("Qual o nome do aniversariante? ")
dia = input("Qual o dia do aniversario? ")

# pegar o fuso horario do brasil
brasilTz = pytz.timezone("America/Sao_Paulo")

# pega a data e horario de hoje
dateBr = datetime.now(brasilTz)

# condicionais
if dateBr.strftime("%d") == dia:
    print("Feliz Aniversário {}!!!".format(pessoa))
else:
    print("Hoje ainda não é o seu aniversário!")