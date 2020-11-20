#Remove elements of a list
#remove 4.0 from a list of numbers

m = [2.3,4.4,3.6,5.0,4.0]

for i in range (len(m)):
    if m[i] == 4.0:
        del m[i]

#the above solution doesn't work because editing the length of the list causes a list
#index out of range error. Unlike for i in m, for i in range(len(m)) checks the length
#only once

while i < len(m):
    if m[i] == 4.0:
        del m[i]
    i += 1

#this is a close solution but will skip values after you remove them

while i < len(m):
    if m[i] == 4.0:
        del m[i]
    else:
        i += 1

#This is the ideal solution. It will not skip any values.
