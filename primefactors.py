# -*- coding: utf-8 -*-
"""
PrimeFactors 

@Grace Wang

"""

def prime_factorization(num):
    ## Finding all factors of the given number
    factors_list = []
    factor = 2
    while(factor <= num):
        if(num % factor == 0):
            factors_list.append(factor)
        factor = factor + 1
        
    print(factors_list)
    
    ## Finding which of the factors are prime
    prime_factors = []
    for i in factors_list:
        for j in range(2,i):
            if(i % j == 0):
                break
        else:
            prime_factors.append(i)
    
    ## Prints results        
    num = str(num)
    prime_factors = str(prime_factors)
    print("The prime factors of " + num + " are " + prime_factors)
    
    
## Takes user input and calls on the prime factorization function                
while True:
    a = int(input('give me a number greater than 1 or enter 0 to quit: '))
    if (a == 0):
        break
    prime_factorization(a)
                