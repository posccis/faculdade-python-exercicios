#Variaveis de controle
d = 0
c = 0
#Lista que recebe todos os maiores valores
list_2 = []
#Lista que temporaria que recebe todos os valores de cas N
listo = []
#Input da quantidade de casos
entrada = int(input())
#Variavel de controle, vou deixar ai por medo.
p = 0
#Função f(n)
def f_n(n):
    global p
    p += 1
    if n%2 != 0 and n != 1:
        n = 3 * n + 1
       
        f_n(n)

    elif n%2 == 0:
        n = n/2
        
        f_n(n)
   
    elif n == 1:
        pass
    #Retornando a quantidade de chamadas que a função fez
    return p

#Faz o calculo de qual N fez a maior quantidade de chamadas
def ListFin():
    global listo
    
    z=0
    for k in listo:
        
        if k > z or k == z:
             z = k
    
    #Zerando a lista temporaria
    listo=[]
    return z

#Função que chama a função form de acordo com a quantidade de casos que o usuario disser que irá haver
def ent(entrada):
    global d
    if d <= entrada:
        form()
        d += 1
        ent(entrada)

#Função form que inicia todo o processo do codigo   
def form():
    global c, list_2, listo
    #Input que recebe os valores A e B
    value_a, value_b = input().split()
    value_a = int(value_a)
    value_b = int(value_b)
    #Chamada da Função adc
    adc(value_a, value_b)
    
    #Chamada da função ListFin
    return list_2.append(ListFin())
    #Zerando a lista temporaria, também vou deixar aqui por medo.
    listo=[]
    

#Função que define os N da função e retorna a lista com todos os valores de N
def adc(v_a, v_b): 
    global c, listo, p

    
    p=0
    if v_a <= v_b:
        
        v_a +=1
        listo.append(f_n(v_a))
        
        adc(v_a, v_b)
    else:
        
        pass
    return listo
    #Já sabe
    listo=[]

"""__________________________________"""

#Teste das restrições da entrada
if entrada >= 1 and entrada <= 100:
    entrada = entrada -1
    ent(entrada)



d = 0
listo = []
#Saida para o usuario
for s in range(len(list_2)):
    print("Caso %i: %i" % (s+1, list_2[s]) ) 
 
 
        #....
