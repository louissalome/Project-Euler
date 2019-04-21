#!/usr/bin/env python
# coding: utf-8

# MY LIBRARY
import numpy as np

def crible(n) :
    L, P = [], []
    for i in range(2,n+1) :
        L.append(i)
    for i in range(2,int(np.sqrt(n))+1) :
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
    if n==1 or n==0:
        return 1
    else :
        return n*fact(n-1)
    
def dichotomy(l, e):
    size = len(l)
    (a, b) = (0, size - 1)
    while b - a > 1:
        m = (a + b) // 2
        if e == l[m]:
            return m
        elif e < l[m]:
            b = m
        else:
            a = m
    if e == l[a]:
        return a
    elif e == l[b]:
        return b
    elif l[a] < e < l[b]:
        return a, b
    elif e < l[a]:
        return (0, -1)
    else:
        return (-1, 0)
    return a, b

def is_in_dichotomy(l,e):
    size = len(l)
    (a, b) = (0, size - 1)
    while b - a > 1:
        m = (a + b) // 2
        if e == l[m]:
            return True
        elif e < l[m]:
            b = m
        else:
            a = m
    if e == l[a]:
        return True
    elif e == l[b]:
        return True
    else:
        return False
    
def tri_bulle(liste) :
    n = len(liste)
    pres_inv = True
    cpt = 0
    while pres_inv :
        # Inv : liste[n-cpt] <= ... <= liste[n-1]
        #   et j < n-cpt => liste[j] <= liste[n-cpt]
        pres_inv = False
        for j in range(n-cpt-1) :
            if liste[j] < liste[j+1] :
                liste[j+1], liste[j] = liste[j], liste[j+1]
                pres_inv = True
        cpt = cpt + 1
    return liste