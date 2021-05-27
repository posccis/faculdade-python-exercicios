def maximo(x, y):
    if x > y:
        return x
    return y


quant, tam = [int(i) for i in input().split()]
comprimento = [0 for _ in range(quant)]
preco = [0 for _ in range(quant)]

for i in range(quant):
    comprimento[i], preco[i] = [int(j) for j in input().split()]

tabela = [[0 for _ in range(tam+1)] for _ in range(quant+1)]

for i in range(1, quant+1):
    for j in range(1, tam+1):
        if comprimento[i-1] > j:
            tabela[i][j] = tabela[i-1][j]
        else:
            tabela[i][j] = maximo( tabela[i-1][j], tabela[i-1][j-comprimento[i-1]] + preco[i-1])
print(tabela[quant][tam])