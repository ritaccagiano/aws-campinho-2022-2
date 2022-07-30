def printCategory(age):
    if age > 18:
        print('Adult')
    elif age > 65:
        print('Senior Citizen')
    else:
        print('Child')


print(printCategory(70))
