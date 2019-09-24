"""
    Exemplo de Algoritmo Genético desenvolvido por:
    Tiago Bezerra Brito Ramos
    22/09/19
"""
import random as r
import math

cidades = []
with open('/home/tiago/Desktop/cidades.txt', 'r') as city:
    count = 0
    for cid in city:
        aux = cid.strip().split(';')
        x = aux[0]
        y = aux[1]
        cidades.append((int(x[:-2]), int(y[:-2])))


tam_individuo = 3
tam_populacao = 6


def individuo():
    count = 0
    l = []
    while count < tam_individuo:
        elem = r.randint(1, tam_individuo)
        if elem not in l:
            l.append(elem)
            count += 1
    l.append(l[0])
    return l


def populacao():
    ind = []
    for i in range(tam_populacao):
        ind.append(individuo())
    return ind


def fitness(populacao):
    print(populacao)
    calc_fitness = []
    for elem in populacao:
        soma = 0
        x = []
        y = []
        for i in range(tam_individuo):
            a, b = cidades[elem[i]]
            x.append(a)
            y.append(b)

        for i in range(tam_individuo):
            if i < tam_individuo:
                calculo = math.sqrt(math.pow((x[i+1]-x[i]), 2) + math.pow((y[i+1]-y[i]), 2))
                soma += calculo
        calc_fitness.append(soma)
    return calc_fitness



pop = populacao()
print(fitness(pop))


# def selecao(populacao):
#     return
