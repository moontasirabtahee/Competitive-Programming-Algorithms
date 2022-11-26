# Created by Moontasir Abtahee at 11/26/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps heres


import time
def fibo(n):

    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)

from functools import lru_cache

@lru_cache(maxsize=None)
def fiboCache(n):
    if n<=1:
        return n
    return fiboCache(n-1)+fiboCache(n-2)

st = time.time()
print(fibo(100))
end = time.time()
print(f"Without Cache time:{end-st}")
st = time.time()
print(fiboCache(100))
end = time.time()
print(f"With Cache time:{end-st}")