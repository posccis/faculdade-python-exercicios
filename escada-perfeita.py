"""---INPUTS E DECLARAÇÃO DE VARIAVEIS---"""
#Quantidade de colunas
qnt = int(input())
#Quantidade de blocos em cada coluna
blocos = [int(x) for x in input().split()]
#Variavel com a soma dos blocos
som_b = 0
#Laço for fazendo a soma
for j in blocos:
    som_b += j
#Variavel com a quatidade de movimentos
moves = 0
#Valor esperado da escada perfeita
esp = qnt * (qnt+1)/2
#Resto da subtração da soma das colunas do valor esperado
val = som_b - esp
#Contador pois o loop for começa em 0 e não 1
cont = 0


"""---PROCESSO PRINCIPAL DO CODIGO---"""
#Teste para saber se pode se tornar uma escada perfeita
if val % len(blocos) == 0:
#Valor da base
    base = val / len(blocos)
#For que devolve a quantidade de blocos que precisam ser movidos

    for i in range(qnt):
        cont+=1
        
        if blocos[i] > cont + base:
            moves += blocos[i] - cont - base
           
        else:
            pass
    print(moves)
else:
    print('-1')
