# Langage de manipulation des données fichier

```sql
 SELECT [ALL] | [DISTINCT] <liste des noms de colonnes> | *
    FROM <Liste des tables>
    [WHERE <condition logique>]
    [ORDER BY ...]
  
    [GROUP BY ...]
    [HAVING ...]
    
    expression IN (<expression 1, expression 2, ...>)
    expression BETWEEN <expression 1> AND <expression 2>
    expression LIKE "chaîneDeCaractères"
    expression LIKE "toto%"
    expression LIKE "_toto"
    
    "Les critères de tri sont indiqués dans la clause **ORDER BY** :"
    ORDER BY <Champ 1> [ASC|DESC] [, <Champ 2> [ASC|DESC]] ...
    
   "Ces fonctions du langage SQL effectuent un calcul sur des ensembles de valeurs."
    AVG(<Champ>) : moyenne arithmétique
    SUM(<Champ>) : somme arithmétique
    MAX(<Champ>) : valeur maximum
    MIN(<Champ>) : valeur minimum
    COUNT(*), COUNT(<Champ>), COUNT(DISTINCT <Champ>) : nombre d'enregistrements
    
```

```sql
    "La commande **INSERT** permet l'insertion de nouvelles données dans une table :"
    INSERT INTO NomDeLaTable [(liste des noms de champs)]
    VALUES (Valeur1, Valeur2, Valeur3…)
    
    
    "La commande **UPDATE** permet de modifier des enregistrements dans une table :"
    UPDATE NomDeLaTable
    SET Colonne1 = Expression1 [, Colonne2 = Expression2]...
    [WHERE <condition logique>]
```

