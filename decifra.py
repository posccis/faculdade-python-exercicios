
#Recebe a lista com as letras de chave
chave = list(input())
#Recebe e tranforma em lista o texto a ser convertido
texto = list(input())
#Cria a lista com cada letra do alfabeto
abc = list("abcdefghijklmnopqrstuvwxyz")
#String que vai ser o texto convertido
string = ""
#Loop que vai pegar cada letra do texto
for c in range(len(texto)):

#Loop que vai receber cada letra e comparar com cada letra da chave
    for j in range(len(chave)):
        if texto[c] == chave[j]:
#Aqui é convertido para o alfabeto
            texto[c] = abc[j]
            break

        else:
            pass
#Transforma a lista em string
for e in texto:
    string += e


print(string)
