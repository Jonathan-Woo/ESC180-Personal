s = 0
for i in range(n):
    for j in range(int(n/2)):
        s += i+j    #runs n^2/2 times. 2 loops, first one going n/2 times, other one going n times.

#a^p = b^p + c^p        a,b,c are positive integers
#no solutiosn for p>2

def fermat(p):
    n = 1
    while True:
        for i in range(1,n):
            for j in range(1,n):
                for k in range(1,n):
                    if i**p + j**p == k**p:
                        return i,j,k
        n += 1

s = 0
for i in range(n):
    for j in range(i,n):    #runs (n-1) times
        s += (i+j)

#n + (n-1) + (n-2) + ... + 1 = n(n+1)/2 = n^2/2 + n/2 which is O(n^2)

#Complexity of addition
#the complexity of adding large integers: O(n) where n is the number of digits of the longer integer
#                                         O(log(x)) where x is the larger number
#except for integers, all numerical variables in python are limited in magnitude

#addition and multiplication of floats: we can assume that it's constant as it depends on the user's hardware

#Complexity of Multiplication
#the long multiplication algorithm: O(n^2) where n is the number of digits of the largeer number
#however, long multiplication is not actually the most efficient. Karatsuba's algorithem 
#Karatsuba's algorithm O(n^1.6) is better.