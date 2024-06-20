#--------------------------#
# Desenvolvido por:
# Filipe Sottili Alves Pereira
#
# Optei por utilizar do Python pela facilidade
# que eu tenho para desenvolver soluções envolvendo algoritmos com ela.
#---------------------------#

# Imports de bibliotecas para o teste dos algoritmos
import cProfile
import random
 
# Suposta carteira do cidadão
walletMoney = [5, 8, 95, 85, 15, 45, 6, 75, 75]

# Para o teste do algoritmo ter uma visibilidade de diferença entre as duas funções e a escolha da mais ideal,
# adicionei utilizando o while, varios numeros na Wallet do cidadão.
while len(walletMoney) != 8000:
    walletMoney.append(random.random()*100)


def getNum(list: list = []) -> str:
    """Função ideal para verificar no menor tempo possível ( O(n) ) se o cidadão pode ter roubado ou não o dinheiro.
    Recebe como parametro a lista com os elementos,depois pega o primeiro e ultimo elemento da lista para comecar a fazer somas
    e descrobrir se existe alguma combinação de numeros que dá 150. E como estár ordenado, de acordo com o resultado, dá para testar
    o próximo valor da direita (inicio) ou esquerda (final da lista) Se passarmos pela lista inteira e não acharmos uma combinação, 
    então retornar que o fulano não roubou"""

    list.sort()
    matchTheft = []
    left = 0
    right = len(list) - 1

    # While para realizar a operação no array
    while left < right:

        #Lógica para passar pelos elementos e fazer as somas até bater com o numero 150
        total = list[left] + list[right]
        if total == 150:
            matchTheft.append([list[left] + list[right]])  
            return f"Fulano pode ter roubado ${matchTheft[0][0]} da vitima" # Combinação encontrada
        elif total < 150:
            left += 1
        else:
            right -= 1

    return "Fulano não roubou 150 da vitima" # Combinação não encontrada


 
def getNum2(list: list = []) -> str:
    """Função que percorre a lista por O(n)2 que tem uma performance totalmente inferior á função de cima.
    Recebe como parametro a lista com os elementos e passa por todos os elementos da lista, após isso, pega
    cada elemento e soma individualmente com todos os elementos da lista, formando pares, e caso o valor do par dê 150, 
    ele retorna se o fulano pode ter roubado."""
    list.sort()
    matchTheft = []
    for i in list:
        for j in list:
            if i + j == 150:    
            # Se a soma der 150, ele coloca a soma no array e retorna 
            # que o fulano pode ter roubado.
                matchTheft.append([i + j])
                return f"Fulano pode ter roubado os ${matchTheft[0][0]} fulampos da nossa vitima!"
            

# Run das duas funções em comparação do tempo de execução de cada 

# //////////////////////////////////////////////////////////////////////////////////// #

# Função ideal, que demora 0.003 segundos para fazer as operações na carteira em 8 mil números.
cProfile.run('getNum(walletMoney)')

#>>> cProfile.run('getNum2(walletMoney)')
#         7 function calls in 0.003 seconds
# 
#   Ordered by: standard name
# 
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.001    0.001    0.003    0.003 <stdin>:2(getNum2)
#        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        1    0.002    0.002    0.002    0.002 {method 'sort' of 'list' objects}


# //////////////////////////////////////////////////////////////////////////////////// #


# Função não ideal, que demora 1.329 segundos para fazer as operações na carteira em 8 mil números.
cProfile.run('getNum2(walletMoney)')

#>>> cProfile.run('getNum(walletMoney)')
#         6 function calls in 1.329 seconds
# 
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    1.329    1.329    1.329    1.329 <stdin>:1(getNum)
#        1    0.000    0.000    1.329    1.329 <string>:1(<module>)
#        1    0.000    0.000    1.329    1.329 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        1    0.001    0.001    0.001    0.001 {method 'sort' of 'list' objects}

 
 

