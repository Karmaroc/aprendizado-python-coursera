"""
function isPrime(number n)
    for i from 2 to square root of n rounded down inclusive
        if n mod i is 0
            return false

    return true
"""

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:    
            return False
    return True

# print(isPrime(2))

"""
function isPrime(number n)
        factors = generated array of numbers from 2 to n-1 inclusive
        for i in factors:
            if n mod i is not equal to 0
                remove i from factors

        if factors is not empty
            return false

        return true
"""

def isPrime(n):
    fator = range(2, (n-1))

    for i in fator:
        if n % i != 0:
            fator.remove(i)
    if fator is not []:
        return False

    return True

# print(isPrime(7))
""" 
function isPrime(number n)
    for i from 1 to n inclusive
        if i ≠ 1 and i ≠ n and n mod i equals 0
            return false
            
    return true
"""

def isPrime(n):
    for i in range(2, n):
        if i != 1 and i != n and n % i == 0:
            return False
    
    return True

print(isPrime(121))