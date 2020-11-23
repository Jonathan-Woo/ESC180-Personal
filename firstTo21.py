#Race to 21

#two players
#start at 0
#players can alternately say +1 or +2
#The first player to get to 21 wins

def is_win21_simple(n):
    '''Return True if being at sum n leads to winning the game
    in this simpler example, each player can only go +1
    '''
    if n == 20:
        return True
    #for example, if you're at 15, your chance of winning is the opposite
    #of that of the 16th position
    return not is_win21(n+1)

def is_win21(n):
    '''Return True if being at sum n and having the turn results in a guaranteed
    win.
    '''
    if n == 21:
        return False
    #base case
    if n == 19 or n == 20:
        return True

    #for a position n to be winning, n+1 or n+2 must be losing
    #this function checks at position n, am I guaranteed to win if I play
    #optimally
    return not is_win(n+1) or not is_win(n+2)

def move21(n):
    '''Return a move that wins the Race to 21 Game (with optimal play) if
    possible, otherwise return a random move
    '''
    #if the a +1 position or a +2 position are losing, then you want to make
    #those moves
    if not is_win21(n + 1):
        return 1
    elif not is_win21(n + 2):
        return 2
    else:
        return int(2*random.random()) + 1

def game21():
    '''Plays the game 21. Constant while loop keeps the game playing
    with the game getting user and player moves repeatedly.
    '''
    n = 0
    print("n = ", n)

    while True:
        user_move = int(input("MOVE: "))
        n += user_move
        print("n = ", n)
        if n == 21:
            print("USER WON")
            return

        computer_move = move21(n)
        n += computer_move
        print("n = ", n)
        if n == 21:
            print("COMPUTER WON")
            return

def game21_nice(cur_player):
    '''A better version of playing the game instead of repeating code
    '''
    while n != 21:
        if cur_player == "USER":
            move = int(input("MOVE: "))
            cur_player = "COMPUTER"
        else:
            move = move21(n)
            cur_player = "USER"
        n += move
        print("n = ", n)
    if cur_player == "USER":
        print("COMPUTER WON")
    else:
        print("USER WON")
    #20: True
    #19: True
    #18: False
    #17: True
    #16: True
    #15: False
    #14: True
    #13: True
    #12: False
    #...

    #The pattern above shows that if at your position, (n+1) or (n+2) reaches
    #a multiple of 3, you are in a winning position. This also means that
    #multiples of 3 are in losing positions.
