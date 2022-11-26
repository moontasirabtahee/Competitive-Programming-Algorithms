# Created by Moontasir Abtahee at 11/26/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
# In Python, heaps are implemented by the module heapq. This module provides a
# function to transform an array A into a heap (heapify(A)), which results in an array
# representing a quasi-perfect tree as described in the preceding section, except that
# the element with index 0 does not remain empty and instead contains the root. The
# module also allows the insertion of a new element (heappush(heap,element)) and
# the extraction of the minimal element (heappop(heap)).

# The reorganisation is done with the operations up(i) and down(i), which are called
# whenever an element with index i is too small with respect to its parent (for up)
# or too large for its children (for down). Hence, up effects a series of exchanges of
# a node with its parents, climbing up the tree until the heap order is respected. The
# action of down is similar, for an exchange between a node and its child with the
# smallest value.
# Finally, the method update permits the value of a heap element to be changed. It
# then calls up or down to preserve the heap order. It is this method that requires the
# introduction of the dictionary rank
import heapq


class OurHeap:

    def __init__(self, items):
        self.heap = [None]  # index 0 will be ignored
        self.rank = {}
        for x in items:
            self.push(x)

def __len__(self):
    return len(self.heap) - 1


def push(self, x):
    assert x not in self.rank
    i = len(self.heap)
    self.heap.append(x)  # add a new leaf
    self.rank[x] = i
    self.up(i)  # maintain heap order


def pop(self):
    root = self.heap[1]
    del self.rank[root]
    x = self.heap.pop()  # remove last leaf
    if self:  # if heap is not empty
        self.heap[1] = x  # move the last leaf
        self.rank[x] = 1  # to the root
        self.down(1)  # maintain heap order
    return root


def up(self, i):
    x = self.heap[i]
    while i > 1 and x < self.heap[i // 2]:
        self.heap[i] = self.heap[i // 2]
        self.rank[self.heap[i // 2]] = i
        i //= 2
        self.heap[i] = x  # insertion index found
        self.rank[x] = i
def down(self, i):
    x = self.heap[i]
    n = len(self.heap)
    while True:
        left = 2 * i  # climb down the tree
        right = left + 1
        if (right < n and self.heap[right] < x and self.heap[right] < self.heap[left]):
            self.heap[i] = self.heap[right]
            self.rank[self.heap[right]] = i  # move right child up
            i = right
        elif left < n and self.heap[left] < x:
            self.heap[i] = self.heap[left]
            self.rank[self.heap[left]] = i  # move left child up
            i = left
        else:
            self.heap[i] = x  # insertion index found
            self.rank[x] = i
            return


def update(self, old, new):
    i = self.rank[old]  # change value at index i
    del self.rank[old]
    self.heap[i] = new
    self.rank[new] = i
    if old < new:  # maintain heap order
        self.down(i)
    else:
        self.up(i)
