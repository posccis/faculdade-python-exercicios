



""" --- DECLARAÇÃO DA LISTA QUE RECEBE OS INSTANTES 
---------------------- E --------------------------
     DA VARIAVEL COM A QUATIDADE DE PESSOAS --- """
instantes = []
pessoas = int(input())

""" --- end --- """

""" --- INICIO DO LAÇO 'FOR' QUE RECEBE OS INSTANTES --- """
for i in range(pessoas):

    #Vai testar se o input é um inteiro
    try:
        #Entrada do instante
        inst = int(input())
    except:
        #Caso seja uma string ele encerra o laço
        break
    
    #Adiciona os instantes á lista
    instantes.append(inst)
""" --- end --- """



""" --- INICIO DA FUNÇÃO QUE FAZ O CALCULO PARA DEVOLVER OS SEGUNDOS --- """

#A função recebe a lista com os instantes(quant)
def Segundos(quant):
    #A escada sempre vai ficar ativa pelo menos 10s
    total = 10 

    #Os segundos iniciais em que a escada ficou ativa antes que alguem passasse
    resto = quant[0] 
    for i in range(len(quant)):

        #Os segundos que aumentam sempre que outra pessoa passa no sensor
        diferença = quant[i] - quant[i-1] 
        if diferença < 0:
            diferença = quant[i]

        #Os 10s que aumentam sempre que a escada tem 10 segundos de inatividade
        if diferença > 10: 
            total += 10

        elif diferença <= 10:
            total += diferença
    
    #O resultado ignora os segundos iniciais de inatividade
    return total - resto
""" --- end --- """

#CHAMADA DA FUNÇÃO
print(Segundos(instantes)) 