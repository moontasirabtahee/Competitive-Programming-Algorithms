# Created by Moontasir Abtahee at 11/26/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
import sys
# 3
# paris tokyo 9471
# paris new-york 5545
# new-york singapore 15344

#Read a graph Input
from collections import defaultdict
edge = int(sys.stdin.readline())

g = defaultdict(dict)
for i in range(edge):
    u,v,weight = input().split()
    g[u][v] = int(weight)

print(g)
