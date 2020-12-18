import math

#Question 1
def is_sorted(L):
    '''
    Takes a list of ints L and returns True iff the list L is sorted,
    in either non-increasing or non-decreasing order.
    '''
    if L == L.sort() or L == L.sort(reverse = True):
        return True
    return False

    #O(1) time

#Question 2
def euc_distance(u, v):
    '''
    Returns the Euclidean distance between teh endpoints of two sparce
    vectors u and v
    '''
    sum = 0
    for i in range(max(max(list(u.keys())), max(list(v.keys())))):
        sum += (u.get(i, 0) - v.get(i, 0))**2

    return math.sqrt(sum)

#Question 3
def movies_by_release_date(movies):
    '''
    Takes a dictionary whose keys are movie names and values are release dates
    and returns a list of movie names in order from the most recent
    to the earliest release date
    '''
    sorted_movies = {}
    long_time_ago = []
    for movie, release_date in movies.items():
        if "a long time ago" in release_date:
            long_time_ago.append(movie)
        else:
            year = remove_letters(release_date)
            if year in sorted_movies:
                sorted_movies[year].append(movie)
            else:
                sorted_movies[year] = [movie]

    final = []
    sorted_movies = sorted(sorted_movies.items(), reverse = True)
    for items in sorted_movies:
        final.extend(items[1])

    final.extend(long_time_ago)
    return final

def remove_letters(sentence):
    '''
    Returns the integers from the beginning of a string
    '''
    for letter in range(len(sentence)):
        if sentence[letter] in ["1","2","3","4","5","6","7","8","9","0"]:
            pass
        else:
            sentence = sentence[:letter]
            return int(sentence)

#Question 4
def merge(L1, L2):
    if len(L1) == 0 or len(L2) == 0:
        return L1 + L2
    else:
        if L1[0] < L2[0]:
            return [L1[0]] + merge(L1[1:], L2)
        else:
            return [L2[0]] + merge(L1, L2[1:])

#Question 5
