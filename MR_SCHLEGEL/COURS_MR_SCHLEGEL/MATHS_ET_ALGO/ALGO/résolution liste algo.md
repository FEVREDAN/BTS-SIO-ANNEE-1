```css
Variables

Début
Fsi
Fin
```



## Affichage d’une somme :

Ecrire un algorithme qui demande à un utilisateur de saisir deux nombres entiers et affiche la somme des nombres.

| ![image-20211116113923952](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20211116113923952.png) | ![image-20211116090107823](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20211116090107823.png) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

------



## Vérification de nombre :

Ecrire un algorithme qui demande à un utilisateur de saisir deux nombres entiers et affiche « identique » si les deux nombres ont la même valeur ou « différent » sinon.

| ![image-20211116114225434](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20211116114225434.png) | ![image-20211116181303892](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20211116181303892.png) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

------





## Chaîne la plus longue :

Ecrire un algorithme qui demande à un utilisateur de saisir deux chaînes de caractères et affiche la plus longue des deux.

| ![image-20211116114305581](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20211116114305581.png) | ![image-20211116181542975](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20211116181542975.png) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

------



## Multiple de 7 et de 4:

Ecrire un algorithme qui demande à un utilisateur de saisir un nombre entier et affiche « correct » si le nombre est à la fois multiple de 7 et de 4 ou « différent » sinon.

| ![image-20211116121042565](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20211116121042565.png) | ![image-20211116182036448](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20211116182036448.png) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

------



## Nombre de ‘e’ :

Ecrire un algorithme qui demande à un utilisateur de saisir une chaîne de caractères et qui affiche le nombre de fois que la lettre ‘e’ apparait dans la chaîne.

| ![image-20211116121442458](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20211116121442458.png) | ![image-20211116183044915](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20211116183044915.png) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

------



## Fonction puissance :

Ecrire une fonction qui prend en paramètre deux nombres entier a et b et retourne a^b.

fonction simple:

| ![image-20211116095847066](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20211116095847066.png) | ![image-20211116095909140](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20211116095909140.png) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

fonction compliqué

| ![image-20211116121811409](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20211116121811409.png) |      |
| ------------------------------------------------------------ | ---- |

------



## Fonction Nombre premier :

Ecrire une fonction qui prend en paramètre un nombre entier et renvoie VRAI si le nombre est un nombre premier et FAUX sinon.

```css
Fonction puissance (a:entier):Booléen
Début 
	pour i de 2 à a-1 faire
		si a % i = o 
			retourner faux
		Fsi
	Fpour
	Retourner Vrai
Fin

ou

fonction puissance (a:entier):Booléen
Début 
	pour i de 2 à √a faire
		si a % i = o 
			retourner faux
		Fsi
	Fpour
	Retourner Vrai
Fin

```

## Fonction Moyenne :

Ecrire une fonction qui prend en paramètre une liste de nombres entiers et renvoie la moyenne des nombres de la liste.

```css
Fonction moyenne (l:entier[]):réel
variables locales : 
	somme : entier
Début 
	somme <-0
	pour i de l faire
		sommme <- somme + i
	Fpour
	retourner somme/longueur(l)
	

```



## Fonction Heure exacte :

Ecrire une fonction qui prend en paramètre un nombre entier (< 86 400) symbolisant un nombre de secondes. Cette fonction ne retourne aucune valeur mais affiche l’heure au format hh:mm:ss

```css
Fonction Heure Exacte (s : entier):


h = s // 3600
reste = s % 3600
m = reste // 60
s = reste % 60
```



## Fonction Factorielle itérative :

Ecrire une fonction qui prend en paramètre un nombre entier positif et qui donne la valeur factorielle de ce nombre. Utiliser une boucle dans cette fonction.

```css
Fonction Factorielle itérative (n : entier): reel

Variables locales :
	factorielle = entier
	liste = [1,2,3...98]
Début
	factorielle <-0
	pour factorielle de n faire 
		factorielle <- somme de 1x1 ---> nxi
		
Fsi
Fin

```



## Fonction Factorielle récursive :

Ecrire une fonction qui prend en paramètre un nombre entier positif et qui donne la valeur factorielle de ce nombre. Utiliser une fonction récursive.