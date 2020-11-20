L = [1, 20, 1, 0, 0, 50]

#counting sort/bucket sort

#we want to find how many of each item there are in a list
#0: 2
#1: 2
#20: 1
#50: 1

L = [0, 0, 1, 1, 20, 50]

def counting_sort(L):
    '''return a sorted version of the list of non-negative integers L
    '''                           #n = len(L)
    max_L = max(L)                #k1 * n
    counts = [0] * (max_L + 1)    #k2 * (max(L) + 1)
    for e in L:                   #k3 * n
        counts[e] += 1

    res = []
    for elem in len(counts):
        if counts[elem] > 0:
            res.extend([elem] * counts[elem])       #all of this takes a specific amount of time. Although there is a comparison operator, it's time
    return res                                      #does not change based on the input.
                                  #k4 * max(L)
 #total time complexity

 #(k1 + k3)*n + (k2 + k4)*max(L) + k2       --> now simplify by removing coefficient k.
 #O(len(L)) + max(L)

