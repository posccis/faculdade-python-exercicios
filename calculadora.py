
""" FUNÇÃO PARA MULTIPLICAR (multiply function) """
def Mult(value_a, value_b):
    print(value_a, value_b)
    resultado = 0
    for j in range(value_b):
        for i in range(value_a):
            resultado += 1
            print(resultado)
        
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

ope, valor_a, valor_b = input("bota: ").split()


print(Exp(int(valor_a), int(valor_b)))