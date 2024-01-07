# carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
# carnes2 = carnes
# carnes2.append("ponta de alcatra")

# carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
# carnes2 = []

# for cns in carnes:
#     carnes2.append(cns)
# carnes2.append("ponta de alcatra")

# carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
# carnes2 = carnes[:]
# carnes2.append("ponta de alcatra")

carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
x = carnes
del (x[-1])

print(carnes)
print(x)