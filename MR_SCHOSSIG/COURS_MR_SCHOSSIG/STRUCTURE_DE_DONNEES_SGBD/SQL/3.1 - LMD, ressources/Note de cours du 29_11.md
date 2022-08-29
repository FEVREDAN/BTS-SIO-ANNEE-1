Note de cours du 29/11

# Le langage de description des données (LMD)



Création et modification de tables :



Plusieurs types de données :

Types numériques exacts:

- Les types « Entier »
- Le type « décimal »

Types numériques non exacts :

* FLOAT
* DOUBLE (ou REAL)

Les types chaînes de caractères 

* CHAR
* VARCHAR
* BLOB, TEXT

Les types temporels :

* DATE
* DATETIME
* TIMESTAMP
* TIME



## Création d’une base de données

Une base de données est créée à l’aide de la commande SQL suivante : 

```sql
CREATE DATABASE [IF NOT EXISTS] db_name 
	[create_specification [, create_specification] ...]
```

Les options "create_specification" peuvent être données pour spécifier des caractéristiques de la base. Cela concerne essentiellement le jeu de caractères utilisé.

Les informations minimales à préciser sont :

* nom de la table
* champs 
* * Pour chaque champs on précise :
  * * Son type 
    * Si la valeur NULL est acceptée
* champ(s) de la clé primaire
* clés étrangères
* * pour chaque clef on précise :
  * * Champs et table à laquelle elle est relié
    * Éventuellement les actions lors MAJ ou SUPP 

![image-20211129091838178](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20211129091838178.png)

## Suppression d’une base de données (et/ou) de table

La suppression d’une base de données est réalisée à l’aide de la commande : 

```sql
DROP DATABASE [IF EXISTS] db_name 
```

La suppression d’une table est réalisée comme ci-dessous : 

```sql
DROP TABLE [IF EXISTS] tbl_name [, tbl_name] ...
```

.