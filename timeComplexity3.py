import random
import time

def counting_sort(L):
    '''Return sorted version of the list of non-negative integers L
    '''
    max_L = max(L)
    counts = [0] * (max_L + 1)
    for e in L:
        counts[e] += 1

    res = []
    for elem in range(len(counts)):
        count = counts[elem]
        if count > 0:
            res.extend([elem]*count)
        print(elemn,res)

#lines 11-12: add len(L) elements in total (takes time k5*len(L))
#lines 10-11: run max(L) times  (takes time k4*max(L))

#runtime(L) is O(max(L) + len(L))

#L = [5,2,1,2,10,1]

#bozosort

def is_sorted_nondecreaseing(L):
    '''Return True iff L is sorted in non-decreasing order
    '''
    #return L == sorted(L)
    for i in range (len(L)-1):
        if L[i] > L[i+1]:
            return False
    return True

def bozo_sort(L):
    print(time.time())
    while not is_sorted_nondecreaseing(L):
        i,j = random.randint(0,len(L)-1),random.randint(0,len(L)-1)
        L[i],L[j] = L[j],L[i]
    print(time.time())

bozo_sort([10,2,20,25])

#n = len(L)
#n! permutations of all (n! = 1*2*...*n)
#we expect