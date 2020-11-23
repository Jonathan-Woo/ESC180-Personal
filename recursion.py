#n! = 1 * 2 * ... * n
#   = 1 * 2 * ... * (n-1) * n

def fact(n):
    #base case
    if n == 1:
        return 1

    return n * fact(n-1)

def is_even(n):
    '''Return True if n is even and False if n is odd
    n -- a non-negative integer
    '''
    #base case
    if n == 0:
        return True

    #a number being even or odd can be determined by it's previous number
    #it's the opposite of the previous number
    return not is_even(n-1)

def print_list(L):
    '''Print the list L element-by-element, one element per line
    '''
    #base case
    if len(L) == 0:
        return

    print(L[0])
    print_list(L[1:])

def print_list_backwards(L):
    '''Print the list L element-by-element, one element per line backwards
    '''
    #base case
    if len(L) == 0:
        return

    print_list_backwards(L[1:])
    print(L[0])

if __name__ == "__main__":
    L = [12, 10, 23, 10, 34, 10]
