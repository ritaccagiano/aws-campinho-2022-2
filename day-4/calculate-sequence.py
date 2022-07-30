preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktreaed" \
"lqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

print("The sequence of human preproinsulin: ")
print(preproInsulin)

insulin = bInsulin + aInsulin
print("The sequence of human insulin: " + insulin)

bInsulinPrint = "The sequence of chain B of human insulin: " + bInsulin
print(bInsulinPrint)

print("The sequence of chain A of human insulin: " + aInsulin)


# lista de aminoacidos e pesos
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19, 'G': 75.07, 
        'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21, 'N': 132.12,
        'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12, 'V': 117.15,
        'W': 204.23, 'Y': 181.19}


# contagem do numero de cada aminoacido
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']})

print(aaCountInsulin)

# calcular e somar o total dos valores dos pesos
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']}.values())

print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))

# calcular percentual de erro
# peso molecular padrao
molecularWeightInsulinActual = 5807.63 #float

print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))

