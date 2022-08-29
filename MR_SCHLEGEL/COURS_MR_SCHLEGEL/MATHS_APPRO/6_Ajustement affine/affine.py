# Importation des modules requis
import matplotlib.pyplot as plt
import numpy as np

x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y = [0,0.948683298,2.049390153,2.949576241,4.086563348,4.898979486,6.08276253,6.708203932,8.246211251,9.433981132,9.949874371,11.40175425,12,12.24744871,13.03840481
,14.83239697,16.73320053,16.88194302,17.32050808,19.23538406,20.174241]

plt.scatter(x,y)

plt.title('Nuage de points avec Matplotlib')
plt.xlabel('x')
plt.ylabel('y')

# Définition de l'ajustement
x_ajust = np.arange(0, 20, 0.1)
plt.plot(x_ajust, 0.9941 * x_ajust + 0.0215, color='green')

plt.savefig('affine.png')
plt.show()