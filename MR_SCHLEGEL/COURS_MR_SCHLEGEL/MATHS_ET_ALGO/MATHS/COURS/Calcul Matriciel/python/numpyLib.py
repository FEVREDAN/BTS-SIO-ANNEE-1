import numpy as np

def infoTableau(t):
    print("Type de tableau : ", type(t))
    print("Nombre d'axes : ", t.ndim)
    print("Dimensions du tableau : ", t.shape)
    print("Nombre d'éléments dans le tableau : ", t.size)
    print("Types des éléments du tableau : ", t.dtype)
    print("Taille en bytes des éléments : ", t.itemsize)
    print("Buffer contenant le tableau : ", t.data)

# Création de tableau avec numpy

a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
infoTableau(a)

print("Creation de tableau séquentiel et reformatage np.arange = range python")
b = np.arange(15)
print(b)
b = b.reshape(3,5)
print(b)

print("Creation de tableau a parttir d'un interval et d'un nombre de valeurs désirées")
f = np.linspace(0,2,9)
print(f)
print(np.sin(f))

print("Creation tableau avec que des 0")
c = np.zeros((3,4))
print(c)
print("Creation tableau avec que des 1")
d = np.ones((2,3,4))
print(d)
print("Création tableau non initialisé")
e = np.empty((2,3))
print(e)

# Opération sur les tableaux
m1 = np.arange(6).reshape(2,3)
m2 = np.arange(7,13).reshape(2,3)
print("Addition matricielle : ", m1 + m2)
print("Multiplication des éléments : ", m1 * m2)
print("Puissance : ", m1 ** 2)
print("Comparaison : ", m1 < 4)
m2 = m2.reshape(3,2)
print("Multiplication matricielle : ", m1 @ m2)

# Opération unaires
print("Somme des éléments : ", m1.sum())
print("Minimum : ", m1.min())
print("Maximum : ", m1.max())
print("Somme par rapprot à un axe : ", m1.sum(axis=0))
print("Minimum de chaque ligne : ", m1.min(axis=1))
print("Somme cumulée sur les lignes : ", m1.cumsum(axis=1))
print("Exponentiel : ", np.exp(m1))
print("Racine carrée : ", np.sqrt(m1))
print("Sinus : ", np.sin(m1))

# Accès aux informations
print("Accès direct : ", m1[0,2])
print("Accès à la colonne 1 : ", m1[ : ,1])
print("Accès à la première ligne : ", m1[0:1, : ])
print("Mise à plat de la structure : ")
for e in m1.flat:
    print(e)

# Manipulation de la forme de la structure (shape)
rg = np.random.default_rng(1)
a = np.floor(10*rg.random((3,4)))
print("Mise à plat de la structure : ", a.ravel())
print("Modification de forme : ", a.reshape(6,2))
print("Transposition de la structure : ", a.T)
a.resize((2,6))
print("Resize modifie l'objet lui-même : ", a)
print("Si une dimension est à -1, elle est déduite : ", a.reshape(3,-1))
print("Empilement vertical : ", np.vstack((a,a)))
print("Empilement horizontal : ", np.hstack((a,a)))
print("Split vertical : ", np.vsplit(a, 2))
print("Split horizontal : ", np.hsplit(a, 2))

# Copie
b = a.copy()

#Indexage avancé
b = np.arange(15,20)
i = np.array([0, 0, 2, 1])
print("Indexage avec un tableau d'élément : ", b[i])
i = np.array([[0, 0], [2, 1]])
print("Indexage avec un tableau d'élément en 2D : ", b[i])
i = np.array([False, True, True, False, True])
print("Indexage avec un tableau de boolean : ", b[i])

# Opération algébrique
a = np.array([[1.0, 2.0], [3.0, 4.0]])
print("Transposition : ", a.transpose())
print("Matrice inverse : ", np.linalg.inv(a))
print("Matrice identité d'ordre 3 ", np.eye(3))
b = np.array([6.0, 15.0])
print("Résolution du système d'équation : ", np.linalg.solve(a, b))
