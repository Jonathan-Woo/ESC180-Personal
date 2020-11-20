#Sparce Matrices

a = [[1,0,0,2],
     [0,0,0,5]]

#instead of storing the matrix entry by entry, only make entries that are non-zero
#we use tuples as keys because it's helpful for marking coordinates

sparce_a = {(0,0):1,(0,3):2,(1,3):5}

def sparce_mat_to_mat(sparce, dims):
    #dims[0] rows, dims[1] columns
    mat = []
    for row in range(dims[0]):
        mat.append[0] * dims[1]

    for coord,value in sparce.items():
        mat[coord[0]][coord[1]] = value

    return mat

def mult_sparce_by_vec(sparse, vec, m):
    '''Multiply the sparse matrix sparse by the vector vec

    m is the number of rows of the matrix.

    matrix m x n, vector n x 1, product m x 1
    '''

    out = [0] * m

    for coord, value in sparse.items():
        out[coord[0]] += value * vec[coord[1]]

#files
#.read() makes one big string.
#splitting the string at line breaks makes a list that starts and ends at line breaks. It also removes the line breaks.
f = open("versedog.txt")
poem = f.read()
lines = poem.split("\n")

for line in lines:
    print(line)

#recall that split and read lines both make lists of the values
#read lines adds a line break. Unlike the previous example, line breaks are kept here.
#if you do print a readlines(), you'll have 2 line breaks
f = open("versedog.txt")
lines1 = f.readlines()

#number of sentences
f = open("proust.txt")
text = f.read()

sentences = text.replace("!", ".").replaces("?",".").split(".")
num_sentences = len(sentences)

words = text.split(" ")
num_words = len(words)

#writing to a file
#open(name, argument): The open() function can make a new file by specifying a file name and passing through "w" to specify that you are writing.
f = open("macbeth.txt", "w")
text = "Tomorrow and tomorrow and tomorrow creeps in this petty pace from day to day"
f.write(text)
f.close()