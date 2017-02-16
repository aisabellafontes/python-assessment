"""
Summing the N series
@aisabellafontes
"""
def math(x):
    atual = 1
    anterior = 0
    soma = 0
    for i in range(1,x+1):
        atual = i**2
        soma += atual - anterior
        anterior = atual
    return soma
    

def summing_series_quickly(n):
    tx = lambda x: (x**2)-(x-1)**2
    sn = 0
    while n > 0:
        sn += tx(n)
        n -=1
    return sn


def summing_series_manual(n):
    tx = lambda x: (x**2)-(x-1)**2
    sn = 0    
    for y in range(n):
       sn += tx(y+1)
    return sn
    
def summing_series_slowly(n):
    tx = lambda x: (x**2)-(x-1)**2
    sn = lambda y: 1 if y == 1 else tx(y) + sn(y-1)
    return sn(n)
    
k = int(raw_input())
while k > 0:
    n = int(raw_input())
    print math(n)
    k -=1
