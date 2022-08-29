import random
import matplotlib.pyplot as plt

nbClasses = 20
nbExperience = 1000
tailleListe = 1000

e= [0] * nbExperience

for j in range(len(e)):

    gain = 0
    for i in range(tailleListe):
        if random.randint(0,1) == 0:
            gain = gain - 1
        else:
            gain = gain + 1

    e[j] = gain


plt.hist(e, bins = nbClasses)
plt.title('Représentation de ' + str(tailleListe) + ' jets de pièces ' + str(nbExperience) + ' fois', fontsize=10)
plt.savefig("jetPièce.png")
plt.show()