# Created by Moontasir Abtahee at 11/25/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
squared_dict = dict()
squred_number = [x**2 for x in range(100)]
# print(squred_number)
for index,value in enumerate(squred_number):
    squared_dict[index] = value

for key,value in squared_dict.items():
    print(key,"--->",value)

squred_number.reverse()
print(squred_number)

for _ in range(10):
    print(_)


#Now we will count something
string = "M A MOONTASIR ABTAHEE"
from collections import Counter
x = Counter(string)
print(x)
x =[[[i] for i in range(10)] for _ in range(20)]
print(*x)
