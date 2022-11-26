# Created by Moontasir Abtahee at 11/26/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here

from random import randint
from sys import stdin

def readint():
    return int(stdin.readline())

def readArray(typ):
    return list(map(typ,stdin.readline().split()))

def multiplyMatrix(M,V):
    return [sum(M[i][j]*V[j])for j in range(len(M)) for i in range(len(M))]

def readMatrix(n):
    M = []
    for i in range(n):
        row = readArray(int)
        assert len(row) == n
        M.append(row)

    return M
def randomVector(n):
    return [randint(0,1000000) for i in range(n)]
#
# a probabilistic
# solution exists in O(n2), which consists in randomly choosing a vector x and testing
# whether A(Bx) = Cx. This is the Freivalds test (1979). What is the probability that
# the algorithm outputs equality even if AB != C?

def freivalds(A,B,C):
    return multiplyMatrix(A,multiplyMatrix(B,randomVector(len(A)))) == multiplyMatrix(C,randomVector(len(A)))

counter = readint()
A = readMatrix(counter)
B = readMatrix(counter)
C = readMatrix(counter)

print(freivalds(A,B,C))