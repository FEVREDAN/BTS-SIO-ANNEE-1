**Algorithme** (06/10/21)

non (A et B) = non (a) ou (b)

<u>**Transformation langage courant en Algorithme**</u>

si chat mâle et castré et (brun ou blanc)
alors oui
sinon si chat femelle et castré et non blanc
alors oui
sinon si chat est noir
alors oui

<u>Corrigé:</u>

Si couleur = "noir" 
alors oui
Sinon si sexe = "mâle" et castré = "oui" et (couleur = "blanc" ou "brun")
Alors oui
Sinon si sexe = "femelle" et castré = "oui" et couleur =/ "blanc" 
Alors oui 

Tant que <condition> faire
Ftant

==> partiellement 0 passage

Faire
Tant que <condition> 

=> au moins 1 passage dans la boucle
Pensez que la condition d'arrêt soit dans le tant que

energie_pompe = 10
energie_personne < lire
compteur < 0
Tant que energie_personne > energie_pompe
Faire energie_personne - energie_personne
Alors compteur + 1
Ftant

Corrigé:

Variables locales

energie, e_pompe, nb_pompe : entier

Début

nb_pompe <- 0
energie <- 100
e_pompe <- 10
.
Tant que energie >= e_pompe
Faire energie <- energie - e_pompe
nb_pompe <- nb_pompe + 1
.
Ftant
Ecrire nb_pompe
.
Fin

Variables locales

nb_random, joueur : entier

Début

nb_random <- 10
joueur <- lire
.
Tant que proposition <> solution
Faire si proposition > solution
Alors écrire "c'est moins"
.
Sinon écrire "c'est plus" 
.
Ftant
.
F

Variables

hauteur, longueur, compteur_longueur, compteur_hauteur

Début
.
longueur = 3
Hauteur = 5
Compteur_longueur <- 0
Compteur_hauteur <- 0

​	Tant que compteur_hauteur < hauteur
​		Faire c_l < 0

​			Tant que compteur_longueur < longueur 
​			Faire ecrire "*"
​			Compteur_longueur <- compteur_longueur +1
​			Ftant
​			Ecrire <retour à la ligne>

​	compteur_hauteur <- compteur_hauteur + 1 
Ftant
Fin







