def fact_while(n):
    cur_prod = 1    #cur_prod = (i-1)!
    i = 1

    while i != n+1:
        cur_prod *= i
        i += 1
        #Invariant: cur_prod = (i-1)!

    return cur_prod

#DEFAULT VALUES
#if you don't supply values, even if you supply partial 
#values, the default values are used
def f(a = 2, b = 3):
    return a + b

def fact_iter(n, cur_prod = 1, i = 1):
    '''Return n!
    Arguments:
    n = an integer
    cur_prod = (i-1)!
    '''
    if i == n + 1:
        return cur_prod

    return fact_iter(n, cur_prod*i, i+1)

#this example shows how you can transform an iterative function
#into a recursive one

#fact_iter(3, 1*2*3, 4)
#                           ->6
#fact_iter(3, 1*2, 3)
#                           ->6
#fact_iter(3, 1*1, 2)
#                           ->6
#fact_iter(3, 1, 1)

def fact_rec(n):
    '''Calculates the factorial recursively.
    At each level it multiplies its level number by numbers ahead of it.
    it finds these numbers ahead of it by recursion
    '''
    if n == 0:
        return 1
    return n * fact_rec(n-1)

#fact_rec(0)                ->1
#                           = 1 * 1
#fact_rec(1)                ->1
#                           = 2 * 1
#fact_rec(2)                ->2
#                           = 3 * 2 * 1
#fact_rec(3)                ->6

###################################################################################
#Another thing to note is that fact_iter used upstream computation.
#Meaning to say, it computed and hten moved up into the next level.
#On the other hand, fact_rec computed downstream.
#Meaning to say, it computed afte the program began returning and the data flowed down.