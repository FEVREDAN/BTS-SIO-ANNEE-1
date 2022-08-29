# Importation des modules requis
import matplotlib.pyplot as plt
import numpy as np

x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y = [0,0.9,4.2,8.7,16.7,24,37,45,68,89,99,130,144,150,170,220,280,285,300,370,407]

plt.scatter(x,y)

plt.title('Déplacement du véhicule')
plt.xlabel('Temps')
plt.ylabel('Distance en km')

# Définition de l'ajustement
x_ajust = np.arange(0, 20, 0.1)
plt.plot(x_ajust, 1.0286 * x_ajust**2 + 2.1846, color='green')

plt.savefig('courbe.png')
plt.show()






 

