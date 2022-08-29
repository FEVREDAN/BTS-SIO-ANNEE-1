FONCTION RECURSIVE

* Une fonction récursive est une fonction qui s'appelle elle-même.
* C'est aussi une façon de boucler sur un traitement.
* Elle doit nécessairement changer la valeur d'au moins un pas



Exemple :

```
Fonction manger_hotdogs(nombre_hotdog : Entier)
Début
	if nombre_hotdog > 0 alors
		Ecrire "Je mange un Hotdog"
		manger_hotdogs(nombre_hotdog - 1)
```

```
Fonction somme(n:entier) : entier

Début 
	si n = 0
		retour <- 0
	Sinon
		retour <- n+Somme(n-1)
	Fsi
Fin
```

```
liste_temperatures = [15, 16, 17, 18, 15]

moyenne = somme(liste_temperatures/(lens(liste_temperatures)))
```

