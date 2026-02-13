s = input()
# print(s[::-1])

l = s.split()                       #converting sentence in list of string
k=[]                                #initializing k list
# rev = l[::-1]                     rev of l list
# print(rev)                        print rev
for i in l:                         #traversing in l list
    k.append(i[::-1])               #appending i in k list

print(k)