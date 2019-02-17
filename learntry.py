
m=1
e=-1


biglist=[]

for i1 in range(3):
    for i2 in range(3):
        for i3 in range(3):
            for i4 in range(3):
                for i5 in range(3):
                    newlist=[]
                    newlist.append(i1)
                    newlist.append(i2)
                    newlist.append(i3)
                    newlist.append(i4)
                    newlist.append(i5)
                    biglist.append(newlist)

print(biglist)
print(len(biglist))


a=\
[[0, 0, 0, 0, 0],  [0, 0, 0, 0, e], [0, 0, 0, m, 0], [0, 0, 0, m, m],
 [0, 0, 0, m, e], [0, 0, 0, e, 0], [0, 0, 0, e, m], [0, 0, 0, e, e], [0, 0, m, 0, 0],
 [0, 0, m, 0, m], [0, 0, m, 0, e], [0, 0, m, m, 0], [0, 0, m, m, m], [0, 0, m, m, e],
 [0, 0, m, e, 0], [0, 0, m, e, m], [0, 0, m, e, e], [0, 0, e, 0, 0], [0, 0, e, 0, m],
 [0, 0, e, 0, e], [0, 0, e, m, 0], [0, 0, e, m, m], [0, 0, e, m, e], [0, 0, e, e, 0],
 [0, 0, e, e, m], [0, 0, e, e, e], [0, m, 0, 0, 0], [0, m, 0, 0, m], [0, m, 0, 0, e],
 [0, m, 0, m, 0], [0, m, 0, m, m], [0, m, 0, m, e], [0, m, 0, e, 0], [0, m, 0, e, m],
 [0, m, 0, e, e], [0, m, m, 0, 0], [0, m, m, 0, m], [0, m, m, 0, e], [0, m, m, m, 0],
 [0, m, m, m, m], [0, m, m, m, e], [0, m, m, e, 0], [0, m, m, e, m], [0, m, m, e, e],
 [0, m, e, 0, 0], [0, m, e, 0, m], [0, m, e, 0, e], [0, m, e, m, 0], [0, m, e, m, m],
 [0, m, e, m, e], [0, m, e, e, 0], [0, m, e, e, m], [0, m, e, e, e], [0, e, 0, 0, 0],
 [0, e, 0, 0, m], [0, e, 0, 0, e], [0, e, 0, m, 0], [0, e, 0, m, m], [0, e, 0, m, e],
 [0, e, 0, e, 0], [0, e, 0, e, m], [0, e, 0, e, e], [0, e, m, 0, 0], [0, e, m, 0, m],
 [0, e, m, 0, e], [0, e, m, m, 0], [0, e, m, m, m], [0, e, m, m, e], [0, e, m, e, 0],
 [0, e, m, e, m], [0, e, m, e, e], [0, e, e, 0, 0], [0, e, e, 0, m], [0, e, e, 0, e],
 [0, e, e, m, 0], [0, e, e, m, m], [0, e, e, m, e], [0, e, e, e, 0], [0, e, e, e, m],
 [0, e, e, e, e],  [m, 0, 0, 0, m], [m, 0, 0, 0, e], [m, 0, 0, m, 0],
 [m, 0, 0, m, m], [m, 0, 0, m, e], [m, 0, 0, e, 0], [m, 0, 0, e, m], [m, 0, 0, e, e],
 [m, 0, m, 0, 0], [m, 0, m, 0, m], [m, 0, m, 0, e], [m, 0, m, m, 0], [m, 0, m, m, m],
 [m, 0, m, m, e], [m, 0, m, e, 0], [m, 0, m, e, m], [m, 0, m, e, e], [m, 0, e, 0, 0],
 [m, 0, e, 0, m], [m, 0, e, 0, e], [m, 0, e, m, 0], [m, 0, e, m, m], [m, 0, e, m, e],
 [m, 0, e, e, 0], [m, 0, e, e, m], [m, 0, e, e, e], [m, m, 0, 0, 0], [m, m, 0, 0, m],
 [m, m, 0, 0, e], [m, m, 0, m, 0], [m, m, 0, m, m], [m, m, 0, m, e], [m, m, 0, e, 0],
 [m, m, 0, e, m], [m, m, 0, e, e], [m, m, m, 0, 0], [m, m, m, 0, m], [m, m, m, 0, e],
 [m, m, m, m, 0], [m, m, m, m, m], [m, m, m, m, e], [m, m, m, e, 0], [m, m, m, e, m],
 [m, m, m, e, e], [m, m, e, 0, 0], [m, m, e, 0, m], [m, m, e, 0, e], [m, m, e, m, 0],
 [m, m, e, m, m], [m, m, e, m, e], [m, m, e, e, 0], [m, m, e, e, m], [m, m, e, e, e],
 [m, e, 0, 0, 0], [m, e, 0, 0, m], [m, e, 0, 0, e], [m, e, 0, m, 0], [m, e, 0, m, m],
 [m, e, 0, m, e], [m, e, 0, e, 0], [m, e, 0, e, m], [m, e, 0, e, e], [m, e, m, 0, 0],
 [m, e, m, 0, m], [m, e, m, 0, e], [m, e, m, m, 0], [m, e, m, m, m], [m, e, m, m, e],
 [m, e, m, e, 0], [m, e, m, e, m], [m, e, m, e, e], [m, e, e, 0, 0], [m, e, e, 0, m],
 [m, e, e, 0, e], [m, e, e, m, 0], [m, e, e, m, m], [m, e, e, m, e], [m, e, e, e, 0],
 [m, e, e, e, m], [m, e, e, e, e], [e, 0, 0, 0, 0], [e, 0, 0, 0, m], [e, 0, 0, 0, e],
 [e, 0, 0, m, 0], [e, 0, 0, m, m], [e, 0, 0, m, e], [e, 0, 0, e, 0], [e, 0, 0, e, m],
 [e, 0, 0, e, e], [e, 0, m, 0, 0], [e, 0, m, 0, m], [e, 0, m, 0, e], [e, 0, m, m, 0],
 [e, 0, m, m, m], [e, 0, m, m, e], [e, 0, m, e, 0], [e, 0, m, e, m], [e, 0, m, e, e],
 [e, 0, e, 0, 0], [e, 0, e, 0, m], [e, 0, e, 0, e], [e, 0, e, m, 0], [e, 0, e, m, m],
 [e, 0, e, m, e], [e, 0, e, e, 0], [e, 0, e, e, m], [e, 0, e, e, e], [e, m, 0, 0, 0],
 [e, m, 0, 0, m], [e, m, 0, 0, e], [e, m, 0, m, 0], [e, m, 0, m, m], [e, m, 0, m, e],
 [e, m, 0, e, 0], [e, m, 0, e, m], [e, m, 0, e, e], [e, m, m, 0, 0], [e, m, m, 0, m],
 [e, m, m, 0, e], [e, m, m, m, 0], [e, m, m, m, m], [e, m, m, m, e], [e, m, m, e, 0],
 [e, m, m, e, m], [e, m, m, e, e], [e, m, e, 0, 0], [e, m, e, 0, m], [e, m, e, 0, e],
 [e, m, e, m, 0], [e, m, e, m, m], [e, m, e, m, e], [e, m, e, e, 0], [e, m, e, e, m],
 [e, m, e, e, e], [e, e, 0, 0, 0], [e, e, 0, 0, m], [e, e, 0, 0, e], [e, e, 0, m, 0],
 [e, e, 0, m, m], [e, e, 0, m, e], [e, e, 0, e, 0], [e, e, 0, e, m], [e, e, 0, e, e],
 [e, e, m, 0, 0], [e, e, m, 0, m], [e, e, m, 0, e], [e, e, m, m, 0], [e, e, m, m, m],
 [e, e, m, m, e], [e, e, m, e, 0], [e, e, m, e, m], [e, e, m, e, e], [e, e, e, 0, 0],
 [e, e, e, 0, m], [e, e, e, 0, e], [e, e, e, m, 0], [e, e, e, m, m], [e, e, e, m, e],
 [e, e, e, e, 0], [e, e, e, e, m], [e, e, e, e, e]]