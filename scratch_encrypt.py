# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 14:04:01 2021

@author: subhankar
"""

import sympy
import math

def generateKey():    
    return sympy.randprime(300, 3000),sympy.randprime(300, 3000)

def generatePair():
    i = 1
    while(True):        
        print("checkpoint 2", (fi*i+1))
        factors = get_factors(fi*i+1)
        print("checkpoint 3", factors)
        i += 1
        if(len(factors)>8):
            break
        
    print("checkpoint 4 final", factors)
    E = factors[int(len(factors) - 2)]
    D = factors[int(len(factors) - 1)]
    print("checkpoint 5 final", E, D)
    if(E<=1 or E>=fi):
        print("failed")
        return [0,0]
    else:
        return E,D

def get_factors(x):
   factors = []
   i = 1
       
   while i <= math.sqrt(x):         
        if (x % i == 0) :
            factors.append(i)
            factors.append(int(x/i))
        if(i%10000==0):
           print(".", end=(" "))
        i = i + 1
   print()
   return factors

generatedPrime = generateKey()
P=generatedPrime[0]
Q=generatedPrime[1]
n = P*Q
fi = (P-1)*(Q-1)

print("checkpoint 1", P, Q, fi, n)

# choose a value for e
# d * e = 1 mod fi => d * 7 = 1 mod 20
l = generatePair()
print("checkpoint 5", l)
e = l[0]
d = l[1]
if((e*d)%fi==1):
    print("checkpoint 6", "successful", e, d)    

public_key = [e,n]
private_key = [d,n]

def RSAencrypt(plain_text):
    plain_text = list(plain_text)
    cipher_text = []
    for i in plain_text:
        cipher_text.append(((i**public_key[0])%public_key[1]).to_bytes(4,'little'))
        # print(cipher_text)
    return cipher_text

def RSAdecrypt(cipher_text):
    cipher_text = int.from_bytes(cipher_text, "little")
    return ((cipher_text**private_key[0])%private_key[1]).to_bytes(1,'little')

def RSAdecrypt2(cipher_text_full):
    enlist = list(cipher_text_full)
    i = 0
    cipher_text_group = []
    while(i<len(enlist)):    
        cipher_text_group.append(bytes(bytearray(enlist[i:i+4])))
        i += 4        
    # print(cipher_text_group)
    
    plain_text = []
    for cipher_text in cipher_text_group:
        cipher_text = int.from_bytes(cipher_text, "little")
        plain_text.append(((cipher_text**private_key[0])%private_key[1]).to_bytes(1,'little'))
    return plain_text