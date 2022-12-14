# LMD, application





Soit le système d’information simplifié d’une bibliothèque dont voici le schéma relationnel :

<img src="Medias/3.0/BibliothequeStructure.png" alt="Structure Bibliothèque" style="zoom: 70%" />

**R1 :** *Qui est le lecteur n°30 ?*

```sql
SELECT *
FROM Lecteurs
WHERE numLecteur = 30;
```

**R2 :** *Quels sont les lecteurs dont le nom de famille commence par la lettre « S » ?*

```sql
SELECT *
FROM Lecteurs
WHERE nomLecteur LIKE "S%";

ou 

SELECT nomLecteur, prenomLecteur
FROM Lecteurs
WHERE nomLecteur LIKE "S%";
```

**R3 :** *Quels sont les titres et années de parution des ouvrages qui traitent de la méthode Merise ?*

```sql
SELECT titreOuvrage, anneeParution
FROM Ouvrages
WHERE titreOuvrage LIKE ("%Merise%");
```

**R4 :** *Quels sont les ouvrages qui traitent du registre Windows à partir de l’année 2000 ?*

```sql
SELECT titreOuvrage
FROM Ouvrages
WHERE titreOuvrage LIKE ("%registre%");
```

**R5 :** *Quels sont les lecteurs qui portent le nom (ou le prénom) « BERTRAND » ?*

```sql
SELECT nomLecteur, prenomLecteur
FROM Lecteurs
WHERE nomLecteur LIKE "BERTRAND" OR
	 prenomLecteur LIKE "BERTRAND";
```

**R6 :** *Quels sont les titre et année de parution du ou des ouvrage les plus anciens ?*

```sql
SELECT titreOuvrage, anneeParution
FROM Ouvrages
WHERE
```

**R7 :** *Quels sont les titres des ouvrages actuellement empruntés ou ayant déjà été empruntés ?*

```sql

```

**R8 :** *Quel est le nom des lecteurs ayant effectué au moins un emprunt depuis le début de l’année 2013 ?*

```sql

```

**R9 :** *Quels sont les emprunts (titres et dates) réalisés par le lecteur nommé « HAMSI » ?*

```sql

```

**R10 :** *Quels sont les emprunts en cours, avec pour chacun, le nom du lecteur, le titre de l’ouvrage et la date d’emprunt ?*

```sql

```

**R11 :** *Quel est le nombre total d’emprunts enregistrés à ce jour ?*

```sql

```

**R12 :** *Combien reste-t-il d’emprunts non régularisés pour l’année 2012 ?*

```sql

```

**R13 :** *Quel est le nombre total d’emprunts réalisés par lecteur ?*

```sql

```

**R14 :** *Ajouter l’ouvrage suivant dans la base :*
    N°40, Titre ouvrage : « Réseaux de neurones », 
    Année de parution : 2004

```sql

```

**R15 :** *Enregistrer le retour de l’ouvrage n°17 à la date du jour.*

```sql

```

**R16 :** *Supprimer tous les emprunts régularisés, c'est-à-dire les ouvrages restitués de l’année 2011.*

```sql

```

