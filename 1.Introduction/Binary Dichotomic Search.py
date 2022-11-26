# Created by Moontasir Abtahee at 11/26/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here

def binarySearch(array,value,low,high):
    array = sorted(array)
    mid = ((low+high//2))
    if array[mid] == value:
        return mid
    elif array[mid] > value:
        return binarySearch(array,value,low,mid-1)
    elif array[mid] < value:
        return binarySearch(array,value,mid+1,high)
    else:
        return -1
array = [i for i in range(10)]
print(array)
mid = ((0+len(array)//2))
print(array[mid])
x = binarySearch(array,9,0,len(array)-1)
print(x)