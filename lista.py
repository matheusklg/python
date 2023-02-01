#cria uma lista de strings
listaFrutas = ['banana', 'laranjas', 'uva' ]

#cria uma lista de números
listaNumeros = [5, 10, 20, 30, 40, 222, 1001]

#cria uma lista mista
listaMista = ['texto', 3.14, 1, 2, 3, 'mil', 'Brasil', 999]

#imprime o primeiro item da lista
print(listaFrutas[0])

#imprime o segundo item da lista
print(listaFrutas[1])

#imprime o terceiro item da lista
#f5 para rodar!
print(listaFrutas[2])               

#imprime o último item
print(listaFrutas[-1])

print(listaMista[0])

print(listaMista[1])

print(listaMista[2])

print(listaMista[3])

print(listaMista[4])

print(listaMista[5])

print(listaMista[6])

print(listaMista[7])

print('imprimindo a lista completa com for')

for item in listaMista:
    print(item)
    
#remove um item da lista
listaMista.remove('Brasil')
print(listaMista)

#remove o últmo item da lista
ultimo = listaMista.pop()
print('Removeu com pop:', ultimo)
print(listaMista)
print('lista de frutas:', listaFrutas)
#junta um item no final da lista
listaFrutas.append('kiwi')
listaFrutas.append('abacaxi')
print('lista de frutas:', listaFrutas)

#ordenar em ordem alfabética
listaFrutas.sort()
print('\nordena em ordem alfabética:', listaFrutas)
#inverte a odrem
listaFrutas.reverse()
print('\nondem reversa:', listaFrutas)

listaCategorias = ['vw', 'ford', 'fiat', 'gm', 'bmw']
listaMarcasCarros = ['vw', 'fiat', 'ferrari', 'mercades', 'audi']
#quero imprimir somente as marcas de carro que fazem parte da minha listaCategorias
for marca in listaMarcasCarros:
    #verifica se marca está dentro da listaCaegorias
    if marca in listaCategorias:
        print(marca)    #vm fiat

#lista composta por sbulistas
listaValores = [1, 2, [3, 4, 5], 6, [7, 8, 9,]]
print(listaValores)
print(listaValores[0])
print(listaValores[1])
print(listaValores[2])
print(listaValores[3])
print(listaValores[4])
print('\nImprimindo a lista com o for')
for numeros in listaValores:
    print(numeros)
#imprimindo o valor 4 e 9 da lista de valores
print(listaValores[2][1]) #4
print(listaValores[4][2]) #9

#[5, 10, 20, 30, 40, 222, 1001]
print('\nlista de números:', listaNumeros)

#fazendo uma seleção de lista de números
#imprime da posição 0 até a 3, pois 4 é exclusivo (exclui)
print(listaNumeros[0:4])

#imprime entre 1 e 5
print(listaNumeros[1:6])

#imprime da posição 2 até o penúltimo, pois -1 éo último (exclui)
print(listaNumeros[2:-1])

#imprime da posição 2 até o final!
print(listaNumeros[2:])

#imprime do início até a posição 3
print(listaNumeros[:4])

#imprime a lista toda
print(listaNumeros[:])
#ou
print(listaNumeros)


#coia = identico listaNumeros[:]
a = listaNumeros.copy()

#para contar o númeor de itens da lista
print('Tamanho da lista:', len(listaNumeros))  #7 = 0..6

#apaga todos os itens da lista
listaFrutas.clear()
print(listaFrutas) #[]


#juntar listas
lista1 = [0, 1, 2]
lista2 = [3, 4, 5]
todas = lista1 + lista2
print(todas)

#copia o conteúdo da lista, dentro da própia lista
print(todas * 2)


#lista de notas
notas = [7.2, 5.4, 3.3, 8.1, 9.0, 9.0]

#contando as notas
print('Quantida de notas:', len(notas))
#contadno quantas notas 9 existem na lista
print('Qunatidade de 9.0:', notas.count(9.0))

#calculando a nota mínima
print('Nota mínima:', min(notas))


#calculando a nota máxima
print ('Nota máxima:', max(notas))

#calculando a média das notas
print('Média das notas:', sum(notas) / len(notas))

#lista de compras
listaCompras = ['leite', 'ovos', 'manteiga', 'pão', 'queijo', 'mortadela']

#quero saber se existe pão na lista de compras
print('pão' in listaCompras) #True

#não existe 'carne' na lista de compras
print('carne' not in listaCompras) #True

#em qual posição da lista está o pão?
print("Posição de 'pão' na lista:", listaCompras.index('pão'))


#troca 'pão' por 'pão francês'
posicao = listaCompras.index('pão')
listaCompras[posicao] = 'pão francês'
print(listaCompras)

print('\npercorrendo a lista de compras com for')
for x in listaCompras:
    print(x)
    

print('\nprecorrendo a lista com list comprehension')
print([x for x in listaCompras])

#imprimind as notas vezes 2
print([x * 2 for x in notas])


#similar, porém menos eficiente
for x in notas:
    print(x * 2)





#===== tupla =====

#uso parenteses para definir uma tupla
tuplaNumeros = (10, 20, 30, 700, 1001)

#ou não usa nada!
tuplaFrutas = 'banana', 'laranja', 'uva'
print(tuplaFrutas[0])
print(tuplaFrutas[1])
print(tuplaFrutas[2])


# ====> tupla é similar a uma lista, porém IMUTÁVEL

#além de lista e trupla temos:
#conjunto e dicionário

















    









































    
        
    


