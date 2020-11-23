L = [12,10,2,10,2]

def sum_list(L):
    '''Return the sum of the list of integers L
    Define the sum of the empty list to be 0
    '''
    if len(L) == 0:
        return 0

    return L[0] + sum_list(L[1:])

#TIME COMPLEXITY
#time complexity is based on how many times we call sum_list(). We call
#sum_list() L + 1 times. Each call excluding calls to sum_list
#takes the same amount of time. That's why calling sum_list
#is the runtime complexity.
#We are also assuming slicing L[1:] takes a constant amount of time.

#Runtime complexity: O(len(L))

#sum_list([])

#sum_list([2])

#sum_list([10, 2])

#sum_list([2, 10, 2])

#sum_list([10, 2, 10, 2])

#sum_list([12, 10, 2, 10, 2])

def sum_list2(L):
    '''Type of summing a list by splitting the list in half repeatedly.
    Eventually, the list will be of length 1 and in that case, we return the
    value of that position.
    '''
    if len(L) == 0:
        return 0
    elif len(L) == 1:
        return L[0]

    mid = len(L)//2

    return sum_list2(L[:mid]) + sum_list2(L[mid:])

#sum_list([12])     sum_list([10])

#sum_list([12, 10])     sum_list([2, 10])         sum_list([2,1])    sum_list([2, 3, 4])

#sum_list([12, 10, 2, 10])                 sum_list([2, 1, 2, 3, 4])

#sum_list([12, 10, 2, 10, 2, 1, 2, 3,4])

#TIME COMPLEXITY
#In determining the time complexity of sum_list2(), we must determine which 
#processes take up a relative amount of time vs constant amount of time
    
def f(L):
    '''Slices a list L at the midpoint
    '''
    mid = len(L) // 2
    f(L[:mid])

def g(L, start, end):
    '''Determines the midpoint of 2 points: start and end
    '''
    mid = (start + end) // 2
    g(L, 0, mid)
    
#as the above functions prove, determining the midpoint takes a constant amount
#of time while slicing takes more time for a larger list.
    
#L = [1,2,3,4,5,6]
    
#                    sum_list2([2])  sum_list2([3])       sum_list2([5])   sum_list2([6]) 
#       sum_list2([1])   sum_list2([2,3])   sum_list2([4])  sum_list2([5,6])
#           sum_list2([1,2,3])               sum_list2([4,5,6])
#                       sum_list2([1,2,3,4,5,6,])

#how many calls to sum_list2 are there in total?
#let n = number of calls

#       [1]  [1]  [1]  [1]  [1]  [1]  [1]  [1]              #n calls since each list is of length 1
#       .....................................               #and we started with a list of length n
#       [n/4]   [n/4]       [n/4]  [n/4]                    #4 calls  
#           [n/2]               [n/2]                       #2 calls
#                     [n]                                   #1 call

# 1 + 2 + 3 + 4 + ... + n
#notice that this can be related to the sum of a geometric series: 1 + r^1 + r^2 + ... + r^k = (1-r^(k+1))/(1-r)

# 1 + 2 + 4 + ... + n
# 1 + 2 + 4 + .. + 2^(log2(n))        this is true since 2^level = number of entries per level. Thus, log2(n) gives you the number of levels and 2^(log2(n)) gives you the number of items per level

# = (1-2^(log2(n)+1))/(1-2) = 2^(log2(n)+1)-1 = 2*2^log2(n)-1 = 2n-1
# Complexity: O(n) where n = len(L)
