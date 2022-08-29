test au cas ou forms ne fontcionne pas 

![image-20220124091954723](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20220124091954723.png)

1.Donnez la liste des employés travaillant à Créteil. (2points)

```sql
SELECT nom
FROM Employes
INNER JOIN Departemens
          ON Departemens.numDepartement = Employes.numDepartement
WHERE
        lieu LIKE 'Crétail';
```

2.Donnez les noms des fournisseurs qui approvisionnent une usine de Paris ou de Créteil en produit rouge.  (2points)

```sql
SELECT nom
FROM Fournisseurs
INNER JOIN Livraisons
          ON Livraisons.numFournisseur = Fournisseurs.numFournisseur
INNER JOIN Produits
          ON Produits.numProduit = Livraisons.numProduit
INNER JOIN Usines
          ON Usines.numUsine = Livraisons.numUsine
WHERE
         ((nom LIKE 'Créteil' or nom LIKE 'Paris' FROM Usines) AND
              (couleur LIKE 'rouge' FROM Produits));
              
SELECT DISTINCT nomFournisseur 
FROM Livraisons
INNER JOIN Produits
	ON Produits.nomProduit = Livraisons.nomProduit
WHERE (nom = 'Paris' OR nom = 'Créteil')
	and couleur LIKE 'rouge';
```

3.Donnez la moyenne des salaires. (1point)

```sql
SELECT AVG(salaire) 
FROM Employes
```

4.Donnez les numéros des fournisseurs qui approvisionnent l’usine de numéro 2 en produit de numéro 100. (1point)

```sql
SELECT numFournisseur
FROM Livraisons
WHERE 
        (numUsine = 2 AND numProduit = 100);
```

5.Donnez les numéros des fournisseurs qui approvisionnent toutes les usines avec un même produit.  (2points)

```sql
SELECT numFournisseur
FROM Livraisons
GROUP BY (numProduit FROM Livraisons);
```

6.Donnez les numéros des usines qui utilisent au moins un produit disponible chez le fournisseur de numéro 3 (c’est-à-dire un produit que le fournisseur livre, mais pas nécessairement à cette usine)(2 points)

```sql

```

7.



8.Donnez le numéro, le nom, la ville de toutes les usines. (1point)

```sql
SELECT *
FROM Usines
```

9.Donnez le nombre de commissions non NULL. (1point)

```sql
SELECT COUNT(commission)
FROM Employes
WHERE commissions IS NOT NULL;
```

10.Donnez les numéros des fournisseurs qui approvisionnent l’usine de numéro 2 en un produit rouge(2 points)

```sql
SELECT numFournisseur
FROM Fournisseurs
INNER JOIN Livraisons
           ON Livraisons.numFournisseur = Fournisseurs.numFournisseur
INNER JOIN Produits
           ON Produits.numProduit = Livraisons.numProduit

WHERE 
       ((numUsine = 2 FROM Livraisons) AND couleur = 'rouge' FROM Produits);
```

11.Donnez les noms et date d'embauche des personnes embauchées depuis le 01-09-2006.(1point)

```sql
SELECT nom, dateEmbauche
FROM Employes
WHERE dateEmbauche >= '01-09-2006';
```

12.



13.



14.Changer la ville du fournisseur 3 par Toulouse. (1point)

```sql
UPDATE Fournisseurs
SET ville = 'Toulouse' 
WHERE numFournisseur = 3;
```

15.Donnez le numéro, le nom, la ville de toutes les usines de Paris. (1point)

```sql
SELECT * 
FROM Usines
WHERE ville LIKE 'Paris';
```

24.Supprimer tous les produits de couleur noire et de numéros compris entre 100 et 199.(1 point)

```sql
DELETE FROM 'Produits'
WHERE 
       (couleur = "noire" or couleur = "noir") AND (numProduit BETWEEN '100' AND '199');
```

25.Ajouter un nouveau fournisseur avec les attributs de votre choix.(1 point)

```sql
INSERT INTO Fournisseurs VALUES ('SELECT MAX+1', 'Random', 'client', 'Mulhouse')
```

