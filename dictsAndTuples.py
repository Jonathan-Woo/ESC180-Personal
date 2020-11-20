#dictionaries and tuples

#Properties of dictionaries:
#1. keys are immutable (cannot be changed)

grades = {'PHY':90,'CIV':100,"PRA":93,"ALG":85,"CAL":89}

#you can add items to a dictionary easily
grades["Course"] = 65

#prints a dictionary
print(grades)

#prints the keys and values in "dict_keys" and "dict_values"
#NOT A LIST. Must cast to a list to represent it as a list
print(grades.keys())
print(grades.values())

#prints the keys and values in a "dict_items" NOT A LIST. Must
#cast to a list to represent it as a list
print(grades.items())

#converting a dictionary to a list can be done too
#converts a dictionary into a list of tuples
list(grades.items())

#you can then reference items of the list like normal
#since each item in the list is a tuple, there is [0] and [1]
#representing key and value of that given index
list(grades.items())[0][0]
list(grades.items())[0][1]

#there are several ways of printing a dictionary
for keys in grades:
    print(keys,grades[keys])

for keys, values in grades.items():
    print(keys,values)

########################################
#tuples are immutable (cannot be changed)

#recall that keys in a dictionary must be immutable so
#you cannot use a list as a key. However, you can use a tuple
grades[("aaa","bbb")] = 15


