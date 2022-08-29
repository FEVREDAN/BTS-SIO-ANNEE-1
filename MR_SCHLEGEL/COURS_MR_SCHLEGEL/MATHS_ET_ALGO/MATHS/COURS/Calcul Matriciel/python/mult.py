import numpy as np

def mult(m1, m2):
    if len(m1[0]) == len(m2):
        m3 = np.zeros((len(m1), len(m2[0])))
        for i in range (len(m3)):
            for j in range(len(m3[0])):
                for k in range (len(m1[0])):
                    m3[i][j] =  m3[i][j] + m1[i][k] * m2[k][j]
        return m3
    else:
        return [[0]]

a = np.array([[1, 5], [-3, 2]])
b = np.array([[4],[1]])
print(mult(a, b))