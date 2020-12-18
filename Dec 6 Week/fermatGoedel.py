'''
def f():
    while True:
        pass
'''

'''
def g():
    n = 3
    while True:
        if n % 2 == 0 and is_prime(n):
            return
        n += 1
'''

'''
def fermat(n):
    n = 1
    while True:
        for i in range(1, n):
            for j in range(1, n):
                for k in range(1, n):
                    if i**p + j**p == k**p:
                        return i, j, k
        n +=1
'''



def halt (function_text, function_input):
    '''Returns True if the function halts (i.e. there is no infinite loop in it)
    and False otherwise
    '''

def confused(f):
    if halt(f,f):
        while True:
            pass
    else:
        return False

#Suppose halt(confused, confused) is True. So confused(confused) halts. Therefore
#confused(confused) does not halt because within confused(confused), halt(confused, confused)
#is called. When halt(confused) is True, it enters an infinite loop. Contradiction.

#Suppose halt(confused, confused) is False. So confused(confused) does not halt.
#But if halt(confused, confused) is False, confused halts. Contradiction again.

#The point of this exercise is that it is impossible to write the halt() function.
#Such a function would have to prove



#######################################################################################

#Goede's Theorem

#There are true statements that cannot be proven.

#If any true statement can be proven, then we can write halt(function_text, function_input),
#but we can't, so not any true statement can be proven.

#Here's a possible way to write halt(f,x)
#Generate all strings s over the latin alphabet
#For every s, check whether it's a proof that f(x) halts (if yes, return True)
            # check whether it's a proof that f(x) doesn't halt (if yes, return False)

#This halt(f,x) function would eventually find a proof whether True or False
#for any given f. However, we previously proved that halt(f,x) cannot be written.
#The difference between this and the previous example is that we are assuming
#that any True statement has a proof. In fact, not all True statements do.