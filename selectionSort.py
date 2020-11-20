def max_i(L):
    '''Returns the index of the largest element in L
    by indexing each element. If there is more than one
    maximal element, return the index of the leftmost one
    '''
    cur_max = L[0]
    cur_max_i = 0

    for i in range(len(L)):
        if cur_max < L[i]:
            cur_max = L[i]
            cur_max_i = i
    return cur_max_i

def selection_sort(L):
    '''Modify L so that it's sorted in non-decreasing
    order. Non-decreasing means that it is in increasing
    order with duplicates next to each other.
    '''
    for j in range(len(L)):
        ind_of_max = max_i(L[:len(L) - j])
        L[ind_of_max], L[len(L)-j-1] = L[len(L)-j-1], L[ind_of_max]
    #since we are modifying the contents of L, we do not need to
    #return L

print(selection_sort([5,10,2,2,-1,50]))

#worst case complexity

#max_i
#at worst, max_i is repeated n-1 times where n is the length of
#L. In fact max_i is repeated n-1 times always.

#max_i = O(n) where n is len(L)

#selection_sort
#most time-consuming property is max_i

#j = 0: time proportional to n - 1: k*(n - 1)
#j = 1: time proportional to n - 2: k*(n - 2)
#j = 2: time proportional to n - 3: k*(n - 3)
#...
#j = n - 1: constant time

#where n = len(L) and k is the constant of proportionality.
#since len(L) decreases with each iteration, the pattern goes n - 1, n - 2, ...
#n - n. At n - n, k * (n - n) = constant.
#The constant of proportionality is based on max_i where we established
#earlier that max_i has a runtime complexity of O(n) where n = len(L)

#total = k*(n - 1) + k*(n - 2) + ... + 0
#      = k*(1 + 2 + 3 + ... + (n - 1)) = k*n*(n-1)/2 = k*(n^2 - n)/2
#      = O(n^2)     simplify
#notice that for any list, you will have lengths 1, 2, 3, ... , up to (n-1)

