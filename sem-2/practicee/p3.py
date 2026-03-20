li1 = [3,5,6,7,3,4,9]
li2 = [1,2,3,5,6]

# common = []

# for i in li1:
#     if i in li2:
#         common.append(i)
# print(common)

common = [x for x in li1 if x in li2]

print(common)

