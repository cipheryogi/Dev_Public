# very nice code comprehension style

t = [[3-i for i in range(3)] for j in range(3)]
print(t)
s = 0
for i in range(3):
    s += t[i][i]
print(s) # 6
