# Se houver 5 ou mais bananas, imprima "Eu tenho um monte de bananas"
# se houver de 1 a 4 bananas, imprima "Eu tenho uma pequena quantidade de bananas".

#import random

#bananas = random.randint(1,5)
bananas = 6

#if bananas >= 1 & bananas <= 5:
if bananas >= 5: 
    print("Eu tenho um monte de bananas, {}".format(bananas))
    
    
elif bananas >= 1:
#elif bananas >= 1 & bananas <= 5: # redundante
    print("Eu tenho uma pequena quantidade de bananas, {}".format(bananas))

else:
    print("Não tenho bananas")