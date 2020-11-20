import time
import matplotlib.pyplot as plt

def longest_run_1(s,c):
    run = 0
    max_run = 0

    if c == "z":
        s += "y"        #constant amount of time. So we just have to add it as b.
    else:
        s += "z"

    for ch in s:
        if ch != c:
            max_run = (run, max_run)
            run = 0     #t1
        else:
            run += 1    #t2

    #<= n*max(t1, t2) = a*n for some constant a
    #overall runtime: b + a*n for some constants a and b
    #runtime complexity: O(n) for n = len(s)

    return max_run

#the problem with this function is that the time complexity is too abstract
#we can't determine a general time complexity
def longest_run_2(s, ch):
    for longest in range(len(s), -1, -1):
        if ch*longest in s:
            return longest
    return 0

#this is a better function that we can actually analyze
#it is clear that the longest run time in this case is when the two for loops
#run to their maximum
def longest_run_2(s,ch):
    for longest in range(len(s),-1,-1):
        cur_run = 0
        for i in range(len(s)):
            if s[i] == ch:
                cur_run += 1
            else:
                cur_run = 0

            if cur_run == longest:      #in the worst case, the loop runs a maximum number of times
                return 0

    #therefore longest run time is n^2 because you have 2 loops
    #both loops run n times where n = len(s)

def apply_it(f,arg1):
    return f(arg1)

def time_it(f,arg1):
    t1 = time.time()
    f(arg1)
    t2 = time.time()
    return t2 - t1

def time_it2(f, arg1, arg2):
    t1 = time.time()
    f(arg1, arg2)
    t2 = time.time()
    return t2 - t1

#test for time
times = []
s_lengths = []
for s_length in range(10,10000,1000):
    s = s_length*"a" + "b"
    c = "z"
    times.append(time_it2(longest_run_2,s,c))
    s_lengths.append(s_length)
    #print(times)

plt.plot(s_lengths,times)
plt.show()


def g(n):
    return n + 2

def f(n):
    for i in range(n):
        pass

#in terms of n = len(s), what's the worst case runtime complexity?
