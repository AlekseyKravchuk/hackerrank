'''
Generate all permutations for cuboid specified by corresponding coordinates x,y and z where sum of x,y,z != given n
'''
x = 5
y = 3
z = 2
n = 6

permutations = [[i, j, k]
                for i in [i for i in range(x + 1)]
                for j in [i for i in range(y + 1)]
                for k in [i for i in range(z + 1)] if (i+j+k) != n]
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# The code above is equivalent to the following:
# permutations = []
# for i in range(x + 1):
#     for j in range(y + 1):
#         for k in range(z + 1):
#             if (i + j + k) != n:
#                 permutations.append([i, j, k])
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

for idx, elm in enumerate(permutations):
    print(f'{idx+1}) {elm}')





# x = ['a', 'b', 'c']
# y = ['K', 'L']
# z = [1, 2, 3, 4, 5]
# permutations = [[i, j, k] for i in x for j in y for k in z]
# for idx, elm in enumerate(permutations):
#     print(f'{idx+1}) {elm}')
# print(type(permutations[0]))

# List comprehension for generating matrices
# to generate matrix 4x6 filled in with numbers 1, 2, 3, 4, 5, 6
# matrix = [[i for i in range(1, 7, 1)] for _ in range(4)]
# for lst in matrix:
#     print(lst)

