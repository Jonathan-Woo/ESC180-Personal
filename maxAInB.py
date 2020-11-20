def n_as_plus_b(s):
    '''return the maximum number of "a"s followed by a "b" in the string s
    '''

    for length in range(len(s), -1, -1):
        if "a" * length + "b" in s:
            return length

def n_as_plus_b2(s):
    '''more efficient solution
    '''

    cur_run = 0 #number of a's in the current run
    cur_max_run = 0 #highest number of a's in s so far

    for i in range len(s):
        if s[i] == "a":
            cur_run += 1
        elif if s[i] != "a":
            cur_run = 0
        elif if s[i] == "b":
            cur_max_run = max(cur_run, cur_max_run)
            cur_run = 0

    return cur_max_run