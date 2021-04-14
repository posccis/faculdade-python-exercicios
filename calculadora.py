""" FUNÇÃO SUCESSOR """
def Suc(valor_a):
    return valor_a + 1


""" FUNÇÃO PARA MULTIPLICAR (multiply function) """
def Mult(value_a, value_b):
    
    resultado = 0
    for j in range(value_b):
        for i in range(value_a):
            resultado += 1
          
        
    return resultado
"""---FIM DA FUNÇÃO (end of the function)---"""

""" FUNÇÃO PARA SOMAR (sum function) """
def Soma(value_a, value_b):
    resultado = value_a
    for j in range(value_b):
        resultado += 1
    return resultado
"""---FIM DA FUNÇÃO (end of the function)---"""

""" FUNÇÃO EXPONENCIAL (exponential function) """
def Exp(value_a, value_b):
    valor_1 = value_a
    if int(value_b) >= 3:
        for j in range(value_b-1):
            valor_1 = Mult(valor_1, value_a)
    else:
        valor_1 += Mult(value_a, value_a)
    return valor_1
"""---FIM DA FUNÇÃO (end of the function)---"""

""" --- ENTRADAS (INPUTS) --- """

ope = "stringo"
results = []

while ope != "":
    try:
        entrada = input().split()
        ope = str(entrada[0])
    except:
        ope = ""
       
    if ope == "Mult":
        valor_a, valor_b = entrada[1], entrada[2]
        results.append(Mult(int(valor_a), int(valor_b)))
    elif ope == "Soma":
        valor_a, valor_b = entrada[1], entrada[2]
        results.append(Soma(int(valor_a), int(valor_b)))
    elif ope == "Suc":

        valor_a = entrada[1]
        results.append(Suc(int(valor_a)))
    elif ope == "Exp":
        valor_a, valor_b = entrada[1], entrada[2]
        results.append(Exp(int(valor_a), int(valor_b)))
    else:
        ope = ""
        
""" --- FIM DAS ENTRADAS (end of the inputs) ---"""

""" SAIDAS (outputs) """

for i in range(len(results)):

    print(results[i])

""" --- FIM DAS SAIDAS --- """


