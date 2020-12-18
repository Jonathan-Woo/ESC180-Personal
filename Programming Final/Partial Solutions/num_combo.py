def num_combo(n, start = 0):
    '''
    Returns a list of all number combinations of n
    '''
    #Base case
    if len(n) == 1 or len(n) == 0:
        return n
    #assuming len(n) > 1
    else:
        sol = [n[start]]
        temp_n = n[:]
        temp_n.remove(n[start])
        return sol.extend(num_combo(temp_n))

