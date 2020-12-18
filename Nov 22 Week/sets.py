#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 12:32:48 2020

@author: jwoo
"""

#Sets are lists without duplicates
s1 = {131, 2, 23, 4}

#You can convert from lists to sets
#Converting a list to a set is an easy way of removing duplicates
L1 = list(s1)
L = [4, 2, 4, 5, 6]
set(L)

#Initializing a set
s2 = set()

#a.intersection(b) returns a set containing elements in both 
#a and b.
a = {1, 2, 3}
a.intersection({1,3})

#Freezes a set from being mutable. An application of this
#is that a frozen set can be used as a key in a dictionary. Recall that
#dictionary keys must be immutable.
b = frozenset(a)

#Returns a set containing all elements from both a and b. Like usual, 
#duplicates are removed.
a.union(b)

#Adds an element to the set. Requires the element to iterable
a.update([5])

#Removes an element from the set.
a.remove(5)

#Gets the value that corresponds to k. If k is not in the dictionary,
#we are returned the default value (42 in this case).
k = 3
d.get(k, 4)

def manual_get(d, k, default):
    if k in d:
        return d[k]
    else:
        return default
    
    
#Updating values in a dictionary. Updating will replace the original
#value for the same key
d = {1:2, 3:4}
to_add = {5:6, 3:5}
d.update(to_add)

to_add = {1:3}
d.update(to_add)
    
def manual_update(d, to_add):
    for k, v in to_add.items():
        d[k] = v