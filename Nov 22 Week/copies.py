L1  = [[1,2],[3,4]]
L2 = L1[:]

#performs a deep copy
#we make a new list "copy" and append the values of L1
#instead of appending the list to "copy", we append the VALUES
copy = []
for e in L1:
    copy.append(e[:])

#the problem with the above solution is that it doesn't solve the 
#problem of lists of lists

def deep_copy(obj):
    '''Return a deep copy of the list of lists of ... lists of integers obj
    '''
    #determine whether it is a list or not
    if type(obj) != list:
        return obj
    
    #recursive step: obj is a list
    copy = []
    for elem in obj:
        copy.append(deep_copy(obj))

    return copy

copy = deep_copy(L1)

import copy
copy.deepcopy([1,2,3])