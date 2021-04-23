"""---FUNÇÃO QUE DESCOBRE A PEÇA---"""
def peça(n, lista):
    a = 0
    b = 0
    #A soma que tem que dar juntando todas as peças
    for i in range(n + 1):
        a += i
    #A soma que da com as epças que se tem
    for j in lista:
        v = int(j)
        b += v
    #A peça/valor que tá faltando
    return a - b

"""---INPUT---"""
def entrada():
    #Quantidade de inputs
    qunt = int(input())
    if qunt >= 2 and qunt <= 1000:
        #Todos as peças sendo colocadas em uma lista
        lis_v = [qunt for qunt in input().split()]
        #A lista sendo entregue a função
        print(peça(qunt, lis_v))
    else:
        pass
#Chamada da função
entrada()