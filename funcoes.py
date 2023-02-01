#funções.py

#uma função deve ter um objetivo único de ser pequena

#você pode pensar em uma função como sendo um verbo!

#exemplo: funções de um carro
# o nome da função deve estar em formato camelCase, com parenteses:
#rodasNaRodovia()
#precisamos incluir a palavra def (define função) antes do nome

#aqui apenas definimos as funções
def rodar():
    print('rodando...')

def acelerar():
    print('acelerando...')
# o parentêses sever para receber um parâmetro
def abastecer(litros):
    preco = 5.5
    total = litros * preco
    print('abastecendo...', litros, 'litros po R$', total)

#uma função basicamente é uma rotina específica
#nada a ver com o carro    
def contador():
    for x in range(10):
        print(x)



#depois de definir, podemos chamar (ou não)
abastecer(50)
acelerar()
rodar()
contador()
