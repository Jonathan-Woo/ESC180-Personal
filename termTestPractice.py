MO = [[1,2,3,4],[5,0,5,0],[6,7,8,9]]

def largest_col_sum(M):
    append_list = []
    column_list = []

    for i in range (len(M[0])):
        for e in range (len(M)):
            append_list.append(M[e][i])
        column_list.append(append_list)
        append_list = []

    for i in range (len(column_list)):
        column_list[i] = sum(column_list[i])

    return max(column_list)

#############################################

def two_smallest(L):
    L = sorted(L)

    return [L[1],L[0]]

#############################################

def most_productive_elf(toys_produced):
    most_produced = 0
    most_produced_name = ""

    for i in toys_produced:
        if toys_produced[i] > most_produced:
            most_produced = toys_produced[i]
            most_produced_name = i

    return most_produced_name

#############################################

def filter_out_odds(L):
    if not L:
        return []
    if L[0] % 2 != 1:
        return [L[0]] + filter_out_odds(L[1:])
    return filter_out_odds(L[1:])

#############################################

if __name__ == "__main__":
    print(filter_out_odds([5,-2,4,0,3,7,8]))