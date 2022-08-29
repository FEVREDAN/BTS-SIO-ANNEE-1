#installation
"""
    https://numpy.org/ --> install
"""

import numpy as np

# Définition d'une Matrice
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

# Accès aux informations
print("Accès direct : ", m1[0,2])
print("Accès à la colonne 1 : ", m1[ : ,1])
print("Accès à la première ligne : ", m1[0:1, : ])

# Propriété de la Matrice
"""
a.shape
- permet de savoir si on est dans une matrice ligne
- permet de savoir si on est dans une matrice colonne
- permet de savoir si on est dans une matrice carré
"""

# Matrice reconnaissables
"""
- Matrice identite : np.eye(3)
- Matrice nulle : np.zeros((3,4))
- Matrice opposée : -1 * a
- Matrice inverse : np.linalg.inv(a) --> a = np.array([[1.0, 2.0], [3.0, 4.0]])
"""

# Opération sur les matrices
"""
- Vérifier la possibilité de somme et de multiplication avec a.shape
- Puissance a ** 2 (fermeture transitive graphe)
- Somme : a + b
- Somme avec l'opposé : a + (-1 * a)
- Multiplication terme à terme : a * b
- Multiplication matricielle : a @ b
"""

#Résolution de système avec les matrices
"""
- 2 tartes + 3 baguettes = 7 euros
- 3 tartes + 4 baguettes = 10 euros
a = np.array([[2,3],[3,4]])
b  = np.array([[7],[10]])
- np.linalg.inv(a) * b
- np.linalg.solve(a, b)
"""
