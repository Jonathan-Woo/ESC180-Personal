# alpha = "acbded"
#
# #all passwords of length 3
#
# for c1 in alpha:
#     for c2 in alpha:
#         for c3 in alpha:
#             print(c1 + c2 + c3)
#
#
# #all passwords of length up to N
#
# code = '''a = 5
# b = a + 10
# print(b)
# '''
#
# code = '''def f():
#     return 5'''
#
# s = "I got {} on the calc midterm".format(12)
#
# code = '''def f():
#     return {}'''.format(12)
#
# #write a function with a nested loop with N levels that
# #prints all passwords of length N

def gen_code_all_passwords_len(N):
    code = ""
    for i in range(N):
        code += "for c{} in alpha:\n".format(i)
        code += "   " * (i + 1)

    code += "print("

    for i in range(N-1):
        code += "c{}".format(i) + " + "
    code += "c{}".format(N-1)

    code += ")"

    return code

alpha = "abcdefghijklmnopqrstuvwxyz"
gen_code = gen_code_all_passwords_len(9)
exec(gen_code)