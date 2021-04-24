
#lista recebendo a quantidade de chamadas
listo = []
#lista com as maiores quantidades chamadas
lista_2 = []
#variavel contador
c = 0
#....
"""---FUNÇÃO f(n)---"""
def f_n(n):
    global c
    c +=1
    
    if n%2 != 0 and n != 1:
        n = 3 * n + 1
       
        f_n(n)
    elif n%2 == 0:
        n = n/2
        
        f_n(n)
       
    elif n == 1:
        pass
    #Retornando a quantidade de chamadas que a função fez
    return c
#....
"""---ENTRADA---"""
entrada = int(input())
if entrada >= 1 and entrada <= 100:
    for i in range(entrada):
        #loop recebendo os valores A e B
        value_a, value_b = input().split()
        z = 0
        for j in range(int(value_a), int(value_b)+1): 
            #chamada da função
            listo.append(f_n(j))
            
            c = 0
        #....

        #formção da lista com os maiores valores
        for k in listo:
            if k > z or k == z:
                z = k
        listo = []
        lista_2.append(z)
        z = 0
        #....

"""---SAIDA---"""
for s in range(len(lista_2)):
    print("Caso %i: %i" % (s+1, lista_2[s]) ) 