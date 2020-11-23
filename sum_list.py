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



