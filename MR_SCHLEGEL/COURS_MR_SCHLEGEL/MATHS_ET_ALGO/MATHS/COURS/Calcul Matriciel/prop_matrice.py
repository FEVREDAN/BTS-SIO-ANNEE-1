def info_matrice(m):
    if len(m) == len(m[0]):
        print('matrice carre')
        tstid = True
        for i in range(0, len(m)):
            for j in range(0, len(m[0])):
                if i == j and m[i][j] != 1:
                        tstid = False
                if i != j and m[i][j] != 0:
                        tstid = False
        if tstid:
            print('Matrice identite')
    elif len(m) == 1:
        print('Matrice ligne')
    elif len(m[0]) == 1:
        print('Matrice colonne')
    else:
        print('Matrice quelconque')

    tst = True
    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            if m[i][j] != 0:
                    tst = False
    if tst == True:
        print('Matrice nulle')
    else:
        print('matrice non nulle')

m1 = [[1, 2, 3]]
m2 = [[1], [2], [3]]
m3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m4 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
m5 = [[1, 0, 0], 
      [0, 1, 0], 
      [0, 0, 1]]
info_matrice(m1)
info_matrice(m2)
info_matrice(m3)
info_matrice(m4)
info_matrice(m5)