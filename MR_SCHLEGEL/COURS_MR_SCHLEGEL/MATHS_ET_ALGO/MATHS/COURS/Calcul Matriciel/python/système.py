ordre = 3

m1 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

"""
ai,j =
- 0 si i <> j
- 1 si i = j
"""

for i in range(ordre):
    m1[i][i] = 1

for i in m1:
    print(i)
