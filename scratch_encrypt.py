# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 14:04:01 2021

@author: subhankar
"""

import sympy
import math

class scratch_encrypt:
    def __init__(self, e = -1, d = -1, n = -1, generate_key = True, level = 3):
        if(generate_key):
            generatedPrime = self.generatePrime(level)
            P=generatedPrime[0]
            Q=generatedPrime[1]
            self.n = P*Q
            n = self.n
            self.fi = (P-1)*(Q-1)
            
            print("checkpoint 1", P, Q, self.fi, self.n)
            
            
            l = self.generatePair()
            print("checkpoint 5", l)
            e = l[0]
            d = l[1]
            if((e*d)%self.fi==1):
                print("checkpoint 6", "successful", e, d)        
        
        self.public_key = [e,n]
        self.private_key = [d,n]
        self.expand = 4
        print("Your public and private keys are: ", self.public_key, self.private_key, "Please keep it secure.")
        
        
    def generatePrime(self, level):    
        return sympy.randprime(3*(10**(level-1)), 3*(10**level)),sympy.randprime(3*(10**(level-1)), 3*(10**level))
    
    def generatePair(self):
        i = 1
        while(True):        
            print("checkpoint 2", (self.fi * i + 1))
            factors = self.get_factors(self.fi * i + 1)
            print("checkpoint 3", factors)
            i += 1
            if(len(factors)>8):
                break
            
        print("checkpoint 4 final", factors)
        E = factors[int(len(factors) - 2)]
        D = factors[int(len(factors) - 1)]
        print("checkpoint 5 final", E, D)
        if(E<=1 or E>=self.fi):
            print("failed")
            return [0,0]
        else:
            return E,D
    
    def get_factors(self, x):
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
    
    
    
    def encrypt(self, plain_text):
        if(self.public_key[0] == -1 or self.public_key[1] == -1):
            raise Exception("You need to either generate a key first or provide ur own key to continue")            
        plain_text = list(plain_text)
        cipher_text = []
        for i in plain_text:
            cipher_text.append(((i**self.public_key[0])%self.public_key[1]).to_bytes(self.expand,'little'))
            # print(cipher_text)
        return cipher_text
        
    def decrypt(self, cipher_text_full):
        if(self.private_key[0] == -1 or self.private_key[1] == -1):
            raise Exception("You need to either generate a key first or provide ur own key to continue")
        enlist = list(cipher_text_full)
        i = 0
        cipher_text_group = []
        while(i<len(enlist)):    
            cipher_text_group.append(bytes(bytearray(enlist[i:i+self.expand])))
            i += self.expand        
        # print(cipher_text_group)
        
        plain_text = []
        for cipher_text in cipher_text_group:
            cipher_text = int.from_bytes(cipher_text, "little")
            plain_text.append(((cipher_text**self.private_key[0])%self.private_key[1]).to_bytes(1,'little'))
        return plain_text