#Deep copy practice

#The first thing that we are going to do is initiate a LOL that we are going
#to copy.
#L = [[1,2,3],[4,5,6],[7,8,9]]
L = [[[1,2],[1,2],[1,2]],[[1,2],[1,2],[1,2]],[[1,2],[1,2],[1,2]]]


#We are going to use a nested for loop to index each element directly
temp_list = []
c = []
for list in L:
    c.append(list[:])