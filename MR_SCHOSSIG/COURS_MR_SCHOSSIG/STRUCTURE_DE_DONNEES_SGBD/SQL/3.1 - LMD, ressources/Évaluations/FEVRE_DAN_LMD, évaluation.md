

# 	FEVRE_DAN_LMD, évaluation



## R1 : Quel est l'ouvrage n°5 ?

```sql
SELECT titreOuvrage
FROM Ouvrages
WHERE numOuvrage = 5;

ou

SELECT numOuvrage, titreOuvrage
FROM Ouvrages
WHERE numOuvrage = 5;
```

## R2 : Quels sont les ouvrages dont le titre commence par la lettre « F » ?

```sql
SELECT titreOuvrage
FROM Ouvrages
WHERE titreOuvrage like  "F%";
```

## R3 : Quels sont les titre et année de parution des ouvrages traitant du Registre (dans Windows) ?

```sql
SELECT titreOuvrage, anneeParution
FROM Ouvrages
WHERE titreOuvrage LIKE ("%registre%");
```

## R4 : Quels sont les ouvrages qui traitent de Visual Basic à partir de l’année 1999 ?

```sql
SELECT titreOuvrage, anneeParution FROM Ouvrages
WHERE titreOuvrage LIKE '%Visual Basic%'AND anneeParution >= 1999;
```

## R5 : Quels sont tous les lecteurs qui s’appellent « Bernard » de toutes les façons possibles ?

```sql
SELECT nomLecteur, prenomLecteur
FROM Lecteurs
WHERE nomLecteur LIKE "Bernard" OR
	 prenomLecteur LIKE "Bernard";
```

## R6 : Quels sont les ouvrages ayant été empruntés au moins une fois depuis le début de l’année 2015 ?

```sql
SELECT titreOuvrage,dateEmprunt
FROM Ouvrages
INNER JOIN Emprunter
  ON Emprunter.numOuvrage = Ouvrages.numOuvrage 
  	WHERE Emprunter.dateEmprunt >=date '2015-01-01'
```

## R7 : Quels sont les ouvrages (titre et dates) non rendus par le lecteur « SPAGUETTI » ?

```sql
SELECT titreOuvrage, dateEmprunt
FROM Ouvrages
INNER JOIN Emprunter
  ON Emprunter.numOuvrage = Ouvrages.numOuvrage
  INNER JOIN Lecteurs
  	ON Lecteurs.numLecteur = Emprunter.numLecteur
  	WHERE nomLecteur = 'SPAGUETTI' AND  dateRetour IS NULL;
```

## R8 : Quel est le nombre d’emprunts déjà rendus enregistrés à ce jour ?

```sql
SELECT COUNT(*) empruntsRendus
FROM Emprunter
WHERE dateRetour IS NOT NULL;
```

## R9 : Quels sont les titres des ouvrages empruntés durant la première année d'emprunts dans la bibliothèque ?

```sql
SELECT titreOuvrage, dateEmprunt
FROM Ouvrages
	INNER JOIN Emprunter
    	ON Ouvrages.numOuvrage = Emprunter.numOuvrage
WHERE YEAR(dateEmprunt) = (SELECT MIN(YEAR(dateEmprunt))
                         FROM Emprunter);
```

bonus (pris de MR SCHOSSIG car pas trouvé)

```sql
SELECT titreOuvrage
FROM Ouvrages
WHERE numOuvrage NOT IN (SELECT numOuvrage
                         FROM Emprunter);
```

## R10 : Quel est le nombre total d’emprunts réalisés par lecteur et par année, mais non régularisés ? (pris de MR SCHOSSIG car pas trouvé)

```sql
SELECT 
	CONCAT(prenomLecteur, ' ', nomLecteur) As nom,
	YEAR(dateEmprunt) AS anneeEmprunt,
	COUNT(Emprunter.dateEmprunt) AS nbreEmprunts
FROM Emprunter
	INNER JOIN Lecteurs
		ON Emprunter.numLecteur = Lecteurs.numLecteur
WHERE dateRetour IS NULL
GROUP BY nom, anneeEmprunt;
```

# R11 : Ajouter le lecteur suivant dans la base :

Nom : « TATA »,
Prénom : « Arthur »

```sql
INSERT INTO Lecteurs (numLecteur, nomLecteur, prenomLecteur)
VALUES (31, 'TATA', 'TITI');
```



```sql
INSERT INTO Lecteurs (numLecteur, nomLecteur, prenomLecteur)
VALUES (((SELECT MAX(numLecteur) FROM Lecteurs) +1), 'TATA', 'TITI');
```

# R12 : Supprimer tous les emprunts de Bertrand INAUD de l’année 2013, restitués depuis.

```sql
DELETE *
FROM Emprunter
INNER JOIN Ouvrages
  ON Ouvrages.numOuvrage = Emprunter.numOuvrage
  INNER JOIN Lecteurs
  	ON Lecteurs.numLecteur = Emprunter.numLecteur
WHERE ;
```

```sql
DELETE 
FROM Emprunter
WHERE 
	numLecteur = (SELECT numLecteur
                 FROM Lecteurs
                 WHERE nomLecteur LIKE 'INAUD'
                 	AND prenomLecteur LIKE 'Bertrand')
     AND dateEmprunt LIKE '2013%'
     AND dateRetour IS NOT NULL
```

(pris de MR SCHOSSIG car pas trouvé)