"""
Python em 12 passos serve para o auto-didata curioso conhecer a linguagem em um primeiro contato
e como se estruturam as funções mais básicas.
Esse foi um exemplo de comentário em várias linhas.
"""

#Instalação do Python no computador
print("Passo 1 - Instalação do Python")
print("Acesse python.org e baixe a última versão do python")
print("Instale o executável e utilize o Python Shell")
print("Caso queira utilizar o prompt de comando e não o Python Shell, abra o cmd e digite 'Python'")

# Para imprimir um texto na tela, utiliza-se a função "print()"
print("Passo 2 - Hello World!")

#
print("Aula 3 - Sobre o Python")
a=1
b=2
c=3
d=a+b+c
print(a)
print(b)
print(c)
print(d)

print("Aula 4 - Variáveis")
valorhora=4
dias=30
horastrabalho=8
vencimentomensal=valorhora*dias*horastrabalho
nome="Dagberto"
print(valorhora)
print(dias)
print(horastrabalho)
print(vencimentomensal)
print(nome)
print("Conversão de tipo de variável")
print(valorhora)
floatvalorhora=float(valorhora)
print(floatvalorhora)
testevalor=10.5
print(testevalor)
inttestevalor=int(testevalor)
print(inttestevalor)

print("Aula 5 - Strings")
nome="dagberto rigue"
print("nome")
print(nome[0:7])
print(nome[9:14])
print(nome+nome)
print(nome*3)
print("Verificar se existe r na string")
print("r" in nome)
print("Verificar se existe z na string")
print("z" in nome)

print("Aula 6 - Listas")
lista=[1,2,4,7,"dagberto",2020]
print("Lista:")
print(lista)
lista.append("rigue")
print(lista)
lista.append(3)
print(lista)
print(lista.index("rigue"))
print(lista.count(4))
lista.append(4)
print(lista)
print(lista.count(4))
lista.remove(4)
lista.reverse()
print("Lista2:")
print(lista)
lista2=[9,1,8,2,7,3,6,4,5]
print(lista2)
lista2.sort()
print(lista2)
print("Verificar se existe o número 9 em lista")
print(9 in lista)
print("Verificar se existe o número 9 em lista2")
print(9 in lista2)

print("Aula 7 - Dicionários")
telefones={"dagberto":91919191, "cristina":92929292, "lorena":93939393}
print(telefones)
print("Para adicionar um novo item no meu dicionário:")
telefones["meg"]=94949494
print(telefones)
print("Para remover um novo item no meu dicionário:")
del telefones["meg"]
print(telefones)

print("Aula 8 - Tuplas")
print("Tuplas são como listas imutáveis.")
tuplas=("dagberto","rigue", "python")
print(tuplas)
print(tuplas[0])
print(tuplas[1])
print(tuplas[2])
print(tuplas[0:2])
print(len(tuplas))
print(tuplas+tuplas)
print("Verificar se existe o número 4 na tupla")
print(4 in tuplas)
print("Verificar se existe o nome rigue na tupla")
print("rigue" in tuplas)
print("Lista3:")
lista3=[1,3,5,"python"]
print(lista3)
print("Tuplas2")
tuplas2=tuple(lista3)
print(tuplas2)

print("Aula 9 - If-else")
numero_a=1
if(numero_a==1) :
    print("Número é igual a 1!")
numero_b=2
if(numero_b==1):
    print("Número é igual a 1!")
else:
    print("Número é igual a 2!")
nome="dagberto"
if("z" in nome):
    print("nome tem a letra z")
elif("d" in nome):
    print("nome tem a letra d")
else:
    pass

print("Aula 10 - For Loop")
for x in range(0,5) :
    print("Valor de x é : ", x)


nome="dagberto"
for letra in nome :
    print(letra)

lista_for=[1, 2, 4, 7, "dagberto", "cristina", "lorena"]
for valor in lista_for :
    print(valor)

print("Aula 11 - While Loop")
numero_w=124
while (numero_w>0) :
    print(numero_w)
    numero_w=numero_w-1

print("Aula 12 - Pass, Break, Continue")
print("Break (break no número 7) :")
numeroc=20
while True :
    numeroc=numeroc-1
    print(numeroc)
    if (numeroc==7) :
        break
print("Continue (exclua o número 4):")
numerod=10
while True :
    numerod=numerod-1
    if(numerod==4) :
        continue
    print(numerod)
    if(numerod==2) :
        break
print("Pass (passa a frente sem fazer absolutamente nada, usado quando não sabemos o que vamos programar dentro de um laço :")
for x in range (0,5) :
    pass











