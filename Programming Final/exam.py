import math

#Problem 1
def most_common_frequent_word(files):
    '''
    Returns the word that is the most frequent word in the most files of filenames
    files
    '''
    dict_freq_word = {}
    dict_most_freq_word = {}
    most_freq_word = ""
    #loop through the list of filenames and determine the most common word
    #one at a time
    for filename in files:
        text = open(filename, encoding = "latin-1").read()

        #we want one big string so we are going to remove all line breaks
        text = text.replace("\n", " ")

        #now that we have the text without line breaks, we begin by
        #removing all punctuation
        text = remove_punctuation(text)

        #Since we are case insensitive, here we change case
        text = text.lower()

        #now we split on spaces to make a list of words
        text = text.split(" ")

        #Now add all text to a dictionary, each unique word is a new key
        for word in text:
            if word in dict_freq_word:
                dict_freq_word[word] += 1
            else:
                dict_freq_word[word] = 1

        #Now we have to get the most frequent word from dict_freq_word
        most_freq_word = dict_max_value(dict_freq_word)

        #add the word to the dictionary dict_most_freq_word
        if most_freq_word in dict_most_freq_word:
            dict_most_freq_word[most_freq_word] += 1
        else:
            dict_most_freq_word[most_freq_word] = 1

        #Now, we must reset the dict_most_freq_word
        dict_freq_word = {}

    #after going through all the files, we must find the most freq word
    #from dict_most_freq_word
    return dict_max_value(dict_most_freq_word)

def remove_punctuation(text):
    '''
    Removes all punctuation as specfied in the exam outline from string text
    '''
    #we will replace all punctuation with a space since we will be splitting on
    #spaces afterwards. Splitting on multiple spaces makes no difference.
    return text.replace(".", " ").replace(",", " ").replace("!", " ").replace("?", " ").replace("-", " ")

def dict_max_value(dict):
    '''
    Returns the key of the highest value in dictionary dict
    '''
    highest_key = 0
    highest_value = 0
    for key, value in dict.items():
        if value > highest_value:
            highest_value = value
            highest_key = key
    return highest_key

#########################################################################

#Problem 2
def get_links(html_text):
    '''
    Takes the text of an html file and returns a dictionary whose keys
    are the link texts and whose values are the corresponding URLs
    '''
    #Assuming that links start with href and end at the next
    #</a> we will use those texts as anchors to finding the start and end
    #of link sequences
    sub_text = ""
    link = ""
    link_text = ""
    dict_sol = {}
    while 'href' in html_text:
        start = html_text.index('href')
        end = html_text.index('</a>')

        #now that we have the start and end of the link sequence, we can get
        #the text by slicing assuming the link texts are consistent with the
        #exam outline example

        #we create a subtext of the string by removing the start of the
        #html link
        sub_text = html_text[start + 8:]
        sub_text_end = sub_text.index(">")
        link = sub_text[:sub_text_end-1]

        sub_text = sub_text[sub_text_end + 1:]
        sub_text_end = sub_text.index("</a>")
        link_text = sub_text[:sub_text_end]

        dict_sol[link_text] = link

        #after adding the link and link text to the dictionary, we must slice
        #the text such that the previous block is removed
        html_text = html_text[end + 4:]

    #once there are no more href in html_text, we can return the dictionary
    return dict_sol

#########################################################################
#Problem 3
def f(n):
    '''
    A function for which the tight asymptotic bound on the runtime complexity
    is O((n^2)*log(n)) given list n.
    '''
    #Take inspiration from merge sort. Determine runtime by assuming there is
    #constant runtime complexity per level so we just have to determine
    #how many levels.
    if len(n) == 1:
        return
    else:
        mid = len(n)//2
        return n2_helper(f(n[:mid]) + f(n[mid:]))

def n2_helper(n):
    '''
    This helper function takes a list n assuming len(n) > 1. Does operations
    of complexity n^2
    '''
    #max() takes O(n) time
    max = max(n)
    #if we do it recursively on itself through each element, it will take
    #O(n^2) time
    return n2_helper(n[1:])

#f(n) takes O((n^2)*log(n)) time. The call tree shows that there are log_2(n)
#levels. For each leve, the time complexity is O(n^2) because max() is called
#for each element of n. Therefore, the time complexity is:

#O(n^2 * log_2(n))
#which is equivalent to
#O((n^2)*log(n))

#########################################################################
#Problem 4
def get_target_noparens(nums, target):
    '''
    Takes a list of 3 numbers nums and returns a string of arithmetic operations
    that equals the target number target
    '''

    #Not enough time to think of a clever solution so I'm going to brute force
    #it. Generate all combinations of numbers and operators.

    #There are 16 combinations of operators and 6 combinations of numbers
    #We need to do every combination of numbers with every combination of
    #operations

    #first, determine the combinations of numbers
    num_combo = []
    for first_num in nums:
        temp_second_num = nums[:]
        temp_second_num.remove(first_num)
        for second_num in temp_second_num:
            temp_third_num = nums[:]
            temp_third_num.remove(second_num)
            temp_third_num.remove(first_num)
            for third_num in temp_third_num:
                num_combo.append([first_num, second_num, third_num])

    #now, determine teh combinations of operations
    operations = ["+", "-", "*", "/"]
    op_combo = []
    for first_op in operations:
        for second_op in operations:
            op_combo.append([first_op, second_op])

    #We now have all combinations of numbers and operations
    for num_pair in num_combo:
        for ops in op_combo:
            sol = str(num_pair[0]) + ops[0] + str(num_pair[1]) + ops[1] + str(num_pair[2])
            num_sol = eval(sol)
            if num_sol == target:
                return sol
    return

#########################################################################
#Problem 5
def get_target(nums, target):
    '''
    Takes a list of numbers nums and returns a string of arithmetic operations
    that equals the target number target. Can use parentheses.
    '''
    #Like before, let's get the combination of numbers
    for item in range(len(nums)):
        nums[item] = str(nums[item])
    num_combos = num_combo(nums)

    #now, determine the combinations of operations
    operations = ["+", "-", "*", "/"]
    op_combo = []
    for first_op in operations:
        for second_op in operations:
            op_combo.append([first_op, second_op])

    #First check if a solution exists for no parentheses
    #Unlike last time, this time we are going to store all combinations
    #so that we can test it later
    combos = []
    for num_pair in num_combos:
        for ops in op_combo:
            sol = eval(num_pair, ops)
            combos.append(eval(num_pair,ops))
            num_sol = eval(sol)
            if num_sol == target:
                return sol

    #If there isn't a solution without parentheses, we must use parentheses
    #Parentheses must go around at least one operation
    open = 0
    close = len(solution)
    for solution in combos:
        parentheses_combos = (((0.5)*len(nums)) - 0.5) * len(nums)
        for i in parentheses_combos:
            inner_solution = solution[open:close]
            sol = solution[:open] + "(" + inner_solution + ")" + solution[close:]
            if eval(sol) == target:
                return sol
            if close == (open + 4):
                open += 2
                close = len(solution)
            else:
                close -= 2

def num_combo(n):
    out = []
    if len(n) == 1:
        return n
    else:
        for i, let in enumerate(n):
            for perm in num_combo(n[:i] + n[i+1:]):
                out += [let + perm]
    return out

def eval(num_pair, ops):
    '''
    returns a string of an expression with numbers num_pair and operations ops
    '''
    if len(num_pair) == 1:
        return num_pair[0]
    else:
        sol = str(num_pair[0]) + str(ops[0])
        return (sol + eval(num_pair[1:], ops[1:]))






