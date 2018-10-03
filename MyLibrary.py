# MY LIBRARY
import numpy as np

def is_prime(n):
    isprime = True
    limit = int(n**0.5)+1
    i=2
    while isprime and i<limit:
        if n%i==0:
            isprime= False
        i+=1
    return isprime

def crible(n) :
    L, P = [], []
    for i in range(2,n+1) :
        L.append(i)
    for i in range(2,int(n**0.5)+1) :
        for j in range(i,n-2) :
            if (L[j] % i) == 0 :
                L[j] = 0
    for i in range(n-1) :
        if L[i] != 0 :
            P.append(L[i])
    return P

def ordre(n) :
    cpt = 0
    while n >= 1 :
        cpt += 1
        n = n/10
    return cpt    

def int_to_list(n) :
    L = []
    t = ordre(n)
    for i in range(t) :
        x =  int(n / 10**(t-1-i))
        L.append( x )
        n = n - x*10**(t-i-1)
    return L

def list_to_int(L) :
    n = 0
    t = len(L)
    for i in range(t) :
        n += L[i] * 10**(t-i-1)
    return n

def est_palindrome_iteratif(L) :
    t = len(L)
    n = int(t/2)
    test = True
    for i in range(n) :
        if L[i] != L[t-1-i] :
            test = False
    return test

def est_palindrome(L):
    t = len(L)
    def rec(L,length):
        if length <= 1:
            return True
        else :
            if L[0]!=L[-1]:
                return False
            else :
                return rec(L[1:-1],length-2)
    return rec(L,len(L))

def prod_list(L) :
    P = 1
    for i in range(len(L)) :
        P *= L[i]
    return P

def sum_list(L) :
    S = 0
    for i in range(len(L)) :
        S += L[i]
    return S

def fact(n):
    if n==1:
        return 1
    else :
        return n*fact(n-1)