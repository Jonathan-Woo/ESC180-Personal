import math
#1, 1, 2, 3, 5 ...

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

def fib_formula(n):
    phi = (1+math.sqrt(5))/2
    return int(phi**n/math.sqrt(5) + 0.5)


#TIME COMPLEXITY
#fib(n)
#The branches are different in size, that's what makes it difficult.
#1
# ...                      ...1
#   (n-3)(n-2)    (n-3) (n-4)                       4
#      (n-1)        (n-2)                           2
#           n                                       1

#Since we know that the branch on the left is shorter than the branch on the left, 
#we can determine an upper bound on the time complexity.
#We have fewer than 1 + 2 + 4 + 8 + ... + 2^n = (2^(n+1)-1)/(2-1) = 2^(n+1)-1
#O(2^(n+1)) calls

#The left side becomes the lower bound
#We have more than 1 + 2 + 4 + ... + 2^(n/2) = (2^(n/2+1)-1)/(2-1) = 2*sqrt(2)^n
#O(sqrt(2)^n)

#Define T(n) as the runtime of fib(n)
#T(n) = const + T(n-1) + T(n-2)
#T(n) ~ a*fib(n)
#We can say that the worst-case runtime complexity of fib(n) is O(fib(n))
#########################################################################################
#Clearly, recrusively calculating the same value is not efficient

#CACHING
#storing values that the recursive function computes

#cache: {1:1, 2:1, 3:2, 4:3, 5:5}

def fib_cache(n, cache):
    if n in cache:
        return cache[n]
    cache[n] = fib_cache(n-1, cache) + fib_cache(n-2, cache)
    return cache[n]

cache = {1:1, 2:1}
print(fib_cache(20,cache))

def fib_iter(n):
    fib_prev = 1
    fib_cur = 1

    if n<=2:
        return 1
    
    for i in range(3, n+1):
        fib_prev, fib_cur = fib_cur, fib_prev + fib_cur