#Nov 23, 2020
def power(x, n):
    '''Return x^n
    '''
    res = 1
    for i in range(n):
        res *= x
    return res
#O(n)

def power_rec(x, n):
    '''Return x^n
    '''
    if n == 0:
        return 1
    return x * power_rec(x, n - 1)
#n + 1 calls so complexity is O(n)

#currently we are defining x^n as:
#x^n = x*x^(n-1)
#we could also define it as:
#x^n = x^(n/2)^2

def power_rec2(x, n):
    '''Return x^n
    n = an integer
    x = a non-zero real number
    '''
    if n == 0:
        return 1
    if n == 1:
        return x #because x = x^1
    
    half_power = power_rec2(x,n//2)

    #x^n = half_power*half_power        (* x if n is odd)
    if n % 2 == 0:
        return half_power * half_power
    else:
        return half_power * half_power * x

#  1     -> our base case is n = 1 so this is the lower bound
#.......
#  n/4
#  |
# n/2
# |
# n

#1, 2, 4, 8, ... , n
#how many steps are there?
#2^number of steps = n, therefore:
#log2(n)
#O(log2(n))