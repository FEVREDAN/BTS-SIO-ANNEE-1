mat1 = [
    [2, 3],
    [3, 4]
]

mat2 = [
    [-4, 3],
    [3, -2]
]

mat3 = [
    [0, 0],
    [0, 0]
]

print("Multiplication :")
if len(mat1[0]) == len(mat2):
    for i in range(len(mat3)):
        for j in range(len(mat3[0])):
            for k in range(len(mat1[0])):
                mat3[i][j] = mat3[i][j] + (mat1[i][k] * mat2[k][j])

    for i in mat3:
        print(i)
else:
    print("Multiplication impossible")

print("Addition :")
if len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]):
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat3[i][j] = mat1[i][j] + mat2[i][j]

    for i in mat3:
        print(i)

else:
    print("Addition impossible")
