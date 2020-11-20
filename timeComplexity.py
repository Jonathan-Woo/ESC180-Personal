#Binary search
#Task: given a sorted list L of length n, determine whether the element e
#      is in the list.

#L = [1, 10, 20, 25, 30, 100, 1000]
#e = 22
#is e smaller than teh middle element l?
#if yes, just look in the first half
#if no, just look in the second half

def find_i_binary(L, e):
    low = 0
    high = len(L) - 1

    #currently looking at L[low:(high+1)]

    #keep track of high - low
    #initially: high - low = n - 1
    #2nd iteration: high - low < (n-1)/2
    #3rd iteration high - low < (n-1)/4
    #4th iteration high - low < (n-1)/8
    #...
    #stop when high - low < 2

    #1, 2, 4, 8, ... , n - 1
    #{... log2(n-1) ...}

    while high - low >= 2:
        mid = (low + high)//2
        if L[mid] > e:
            high = mid - 1
        elif L[mid] < e:
            low = mid + 1
        else:
            return mid

    #high - low < 2
    if L[low] == e:
        return low
    elif L[high] == e:
        return high
    return None

#worst-case runtime complexity: 0(log(n))

def find_i(L, e):
    '''Return the index of the element that's equal to e in the list L, or None if e is not in L
    '''

    for i in range(len(L)): #1 operation
        if L[i] == e:       #2 operations
            return i        #1 operation

    return None

#define the worst-case runtime complexity of find_i(L, e) is 0(n)
#where n = len(L)

#Therefore, in the worst case, we perform 2*n + 2 operations

#Approximately, each operation takes t seconds
#Then in the worst case, we take (2*n+2)*t seconds

#Worst case runtime complexity, in operations
#The number of operations that the computer will perform for a given input
#In the worst case, the number of operations will match the length of input n.

#if the runtime is proportional to (2*n+2) we say the runtime is 0(n)
#Intuitively: the runtime is proprtional to the size of the input n

#suppose f(n) is the worst-case runtime for an input size n

###################################################
#big-oh notation

#f(n) is 0(g(n)) if lim           sup f(n)/g(n) < inf
#                   N->inf        n>=N

#g(n) is a function of n that only grows as slowly as n, never faster than n.
#This means that when choosing g(n) you can choose larger g(n) because the ratio of f(n)/g(n) will be less.
#However, we want the lowest possible value g(n) and f(n)/g(n) is a max. (Hence, the limit and SUP).

#2n+1 is 0(n)
#0.5 n is 0(n^2)
#sqrt(1000000*n) is 0(n) (also 0(sqrt(n))

#the worst-case runtime complexity of find_i(L, e) is 0(len(L))
#                                                     0(n) for n = len(L)

#usually we want to give a tight asymptotic bound on teh worst-case-runtime
#meaning f(n) is 0(g(n)), where g(n) grows as slowly as possible.
#Therefore grow as slow as possible to give the worst case scenario.