# importando modulos
import csv
import copy

# criando dicionario de dados modelo

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# repeticao para leitura dos dados
for chave, valor in myVehicle.items():
    print("{} : {}".format(chave,valor))
    
# criar lista de inventario vazia
myInventoryList = []

# ler arquivo csv
with open('day-2/car_fleet.csv') as csvFile:
    
    # ler o arquivo e separar os dados
    csvReader = csv.reader(csvFile, delimiter=',')
    
    # variavel de controle
    lineCount = 0
    
    # repeticao
    for row in csvReader:
        # recuparar o nome das colunas
        if lineCount == 0:
            
            # interpolacao de expressoes
            print(f'Os nomes das colunas sao: {", ".join(row)}')
            
            # incrementar variavel de controle +1
            lineCount += 1
        
        else:
            
            # mostrar os valores das linhas
            print(
                f'vin: {row[0]}\n'
                f'make: {row[1]}\n'
                f'model: {row[2]}\n'
                f'year: {row[3]}\n'
                f'range: {row[4]}\n'
                f'topSpeed: {row[5]}\n'
                f'zeroSixty: {row[6]}\n' 
                f'mileage: {row[7]}\n'
            )
            
            # criar copia dos dados lidos
            currentVehicle = copy.deepcopy(myVehicle)
            
            # acessar as posicoes da lista e atribuir
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]
            
            # adicionar dados na lista vazia
            myInventoryList.append(currentVehicle)
            
            # incrementar
            lineCount += 1
        
    # mostrar quantidade de linhas processadas
    print(f'Foram processadas {lineCount} linhas.')
    
    # mostrar meu inventario
    print("------ meu inventario ------")
    
    #print(myInventoryList)
    
    # repeticao
    for myCarProperties in myInventoryList:
        # retornar dicionario
        #print(myCarProperties)
        
        # tupla de dados: chave, valor
        for chave, valor in myCarProperties.items():
            print("{} : {}".format(chave, valor))
            print("----------------")