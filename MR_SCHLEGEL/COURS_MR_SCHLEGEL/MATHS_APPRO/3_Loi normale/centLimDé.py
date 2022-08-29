import random
import matplotlib.pyplot as plt

nbClasses = 20
nbExperience = 1000
tailleListe = 1000

e= [0] * nbExperience

for j in range(len(e)):

    l = [0] * tailleListe
    for i in range(len(l)):
        l[i] = random.randint(1,6)

    e[j] = sum(l)


plt.hist(e, bins = nbClasses)
plt.title('Représentation de ' + str(tailleListe) + ' jets de dés ' + str(nbExperience) + ' fois', fontsize=10)
plt.savefig("jetD6Somme.png")
plt.show()