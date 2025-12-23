L1 = [1,2,3,4,5,6,7,8]
L2 = [1,2,7,45,34,23,4,67]
#common = [1,24,7]
#union = =[ 1,1,2,2,3,4,4,5,6,7,7,8,45,34,23,67]
#symmetry=[3,5,6,8,45,34,23,67]
common = list(set(L1) & set(L2))
print(common)
union = list(set(L1) | set(L2))
print(union)
symmetry = list(set(L1) ^ set(L2))
print(symmetry)
union_with_duplicates = L1 + L2
print(union_with_duplicates)
'''
dynamic implementation
L1 = input('enter items in L1= ' ).split(',')
print(f"Type L1= {type(L1)}")
print(f"My L1 = {L1}")

#output:

[1, 2, 4, 7]
[1, 2, 3, 4, 5, 6, 7, 8, 34, 67, 45, 23]
[34, 67, 3, 5, 6, 8, 45, 23]
[1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 7, 45, 34, 23, 4, 67]
'''
