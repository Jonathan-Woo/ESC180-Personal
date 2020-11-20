#compute the number of trailing zeros in n!

#n! = 1*2*3*...*n

def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i

    return res

def trailing_zeros_fact(n):
    fact_n = fact(n)

    counter = 0 #the number of zeros encountered

    while fact_n % 10 == 0:
        fact_n //= 10
        counter +=1

    return counter

if __name__ == '__main__':
    print(trailing_zeros_fact(500))