m = [-1, 3, 5,9, -7, 9, -11, 13, 15]
n = [5, 5, 5, 3, 2, 1, 1, 11, -7, -7, 15, 17]

m.sort()  
n.sort()

x = m + n

z = []

for i in x:
    if i not in z:
        z.append(i)
        


z = set(z)
print(z)




