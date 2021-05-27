#A variaveis LINHA, COLUNA E a area para ser comparada
L, C, M, N = input().split()
L = int(L)
C = int(C)
M = int(M)
N = int(N)
#Variaveis para serem usadas como contadores
c = -1
i = 0
valor = 0
#A fazenda entregue pelo usuario
matriz = [list(int(x) for x in input().split()) for i in range(int(L))]
#Formção da tabela auxiliar. Um pouco custoso, mas foi o melhor metodo que encontrei.
tabela=[]
listo = []
for k in range(L):
    listo=[]
    for h in range(L):
       listo.append(0)
    tabela.append(listo)
    

""" ---- Função que adiciona os valores a tabela auxiliar ---- """
def FormaAux(matriz, tabela):
    global L, C, M, N, c, i
    c+=1
#Conferindo se não vai passar da quantidade de colunas
#C-1 porque o list index começa em 0
    if c <= C-1:
        if c == 0 and i==0 :
            tabela[0][0]= matriz[0][0]
            FormaAux(matriz, tabela)
        elif tabela[i-1][c-1] == 0:
            matriz[i][c] = int(matriz[i][c])
            tabela[i][c]= tabela[i][c-1] + matriz[i][c]
            FormaAux(matriz, tabela)
        elif i > 0 and c == 0:
            matriz[i][c] = int(matriz[i][c])
            tabela[i][c] = matriz[i][c] + tabela[i-1][c]
            FormaAux(matriz, tabela)
        elif tabela[i][c-1] !=0 and tabela[i-1][c] !=0 and tabela[i-1][c-1] != 0 :
            matriz[i][c] = int(matriz[i][c])
            tabela[i][c]= matriz[i][c]+tabela[i][c-1]+tabela[i-1][c]-tabela[i-1][c-1]
            FormaAux(matriz, tabela)
        else:
            pass
#Conferindo se não vai passar da quantidade de linhas
    if i < L-1:
        
        c = -1
        i +=1
        FormaAux(matriz, tabela)
    else:
        pass
    return 0
""" ---- Função que devolve a maior quantidade de cajus possiveis dentro daquela area ---- """
def Varredura(matriz, tabela):
    global i, valor, M, N
    if i < len(tabela):
#For para cada coluna dentro de cada linha
        for w in range(len(tabela)):
            if i == 0 and w == 0:
                
                calculo = tabela[i][w]
#Comparação para ver se é o maior valor
                if calculo > valor:
                   valor = calculo

            elif w > 0 and i == 0:
                
                calculo = tabela[i][w] - tabela[i][w-1]
                if calculo > valor:
                   valor = calculo
            elif i > 0 and w == 0:
                
                calculo = tabela[i][w] - tabela[i-M][w]
                if calculo > valor:
                   valor = calculo
            elif w > 0 and i > 0:
                
                calculo = tabela[i][w] - tabela[i][w-N] - tabela[i-M][w] + tabela[i-M][w-N]
                if calculo > valor:
                   valor = calculo
        i+=1
        Varredura(matriz, tabela)
    else:
#Devolvendo o maior valor
        return print(valor)
#A chamada dessa função
FormaAux(matriz, tabela)
i=0
#Chamada da função que devolve o maior valor
Varredura(matriz, tabela)


