mat = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

if len(mat) == len(mat[0]):
    print("La matrice est carrée")
    testId = True
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i == j and mat[i][j] != 1:
                testId = False

            if i != j and mat[i][j] != 0:
                testId = False
    if testId:
        print("C'est une matrice identité")
    else:
        print("Ce n'est pas une matrice identité")

elif len(mat) == 1:
    print("Il s'agit d'une matrice ligne")
elif len(mat[0]) == 1:
    print("Il s'agit d'une matrice colonne")
else:
    print("La matrice est quelconque")

testNul = True
for i in mat:
    for j in i:
        if j != 0:
            testNul = False

if testNul:
    print("La matrice est nulle")
else:
    print("La matrice est non nulle")
