# importar modulo de expressao regular
import re

# abrir e ler o arquivo txt
with open('day-3/preproinsulin-seq.txt') as f:
    insulinFile = f.read()

# mostrar os dados lidos no arquivo
print('--- DADO ORIGINAL ---')
print(insulinFile)


# funcao para limpar os dados
def clean_text(string):
    
    # regex remover os numeros
    string = re.sub(r"\d+", "", string)
    
    #string = string.replace("61", "")
    #string = string.replace("1", "")
    
    # regex remover espacos em branco
    string = re.sub(r"\s", "", string)
    
    # remover espacos em branco
    #string = string.replace(" ", "")
    # remover quebra de linha
    #string = string.replace("\n", "")
    
    # remover ORIGIN
    string = string.replace("ORIGIN", "")
    # remover //
    string = string.replace("//", "")
    
    # retornar string
    return string
    


# dado limpo
cleanInsulin = clean_text(insulinFile)

# mostrar dado limpo
print('--- DADO LIMPO ---')
print(cleanInsulin)


# contagem de caracteres
print('----- CONTAGEM DE CARACTERES -------')
print('Quantidade de caracteres: {}'.format(len(cleanInsulin)))

# dado limpo
stringInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# dividir a string
print('------ DADOS CLASSIFICADOS -----')
print(f'LS: { stringInsulin[0:24] }')
print('Quantidade de caracteres LS: {}'.format(len(stringInsulin[0:24])))

print(f'B: { stringInsulin[24:54] }')
print('Quantidade de caracteres B: {}'.format(len(stringInsulin[24:54])))

print(f'C: { stringInsulin[54:89] }')
print('Quantidade de caracteres C: {}'.format(len(stringInsulin[54:89])))

print(f'A: { stringInsulin[89:110] }')
print('Quantidade de caracteres A: {}'.format(len(stringInsulin[89:110])))
