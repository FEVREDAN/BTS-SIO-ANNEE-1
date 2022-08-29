***MISE A NIVEAU***

**Un digit**

Un digit est un symbole graphique représentant une unité d'une base de donnée (jamais négatif), ca peut-être : 

- un chiffre

				  - une lettre

Les digits sont la totalités des éléments qui compose une base de données.

**Une base de numérotation**

C'est un système de mesure spécifique a un domaine. Dans une base de numérotation, on lit un nombre de droite à gauche pour connaitre le poids de chaque digit.

Le digit le plus à gauche, à le poids le plus fort et celui tout à droite à le plus faible.

Pour chaque système de mesure, la méthode de calcul est différente. peut avoir deux appellations littéraire/ mathématique :

- Le système Binaire ou Base 2

  C'est la base de prédilection en informatique. les digits qui la compose sont les "0" et les "1", un de ces digits représente un "bit" (pas confondre avec Bytes qui est le mot anglais pour octet qui se compose de 8 bits).

  Le poids d'un bit est toujours une puissance de 2.

  ![](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20210922183620363.png)

  Pour changer une base décimal en binaire, il faut rentré les bits le plus fort a droite vers la gauche, prendre le bits le plus faible, regarder dans le tableau décimale le chiffre le plus proche du dessous et ensuite retirer le nombre puis passer au chiffre d'à côté.

  Ex : pour 550

  on prend 550 et on enlève 512 et osn note 1 dans la colonne correspondante. il reste 38, on passe a droite, dans 256 on met zéro parce qu'il est plus grand que 38, idem pour 128 et 64. On met "1" dans 32 et il reste 6, on met "0" dans 8 puis 1 dans "4" et 1 dans "2" et 0 dans "1"

  ![](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20210922194108589.png)

- Le système Décimal ou Base 10  (depuis Egypte, courant parce que 10 doigts)

  On compte 10 digits de 0 à 9.

  ![](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20210922183433883.png)

- Le système Hexadécimal ou Base 16

  Le système hexadécimal, « base 16 » est comme son nom l’indique une base de numération composé de 16 digits.0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F

  Un digit hexadécimal correspond à un ensemble de 4 digits binaire soit 4 bits. Un entier s’écrit en concaténant des digits hexadécimaux.

  

  ex : 55BE

  ![](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20210922195042324.png)



ou 

Pour convertir un nombre décimal (base 10) en un nombre binaire (base 2), il suffit de diviser le nombre décimal par 2 et répéter l’opération sur le quotient obtenue de la division. Si le quotient de l’opération est pair, on poursuit normalement la division en annotant qu’il reste 0.Si le quotient est impair ou à virgule, on poursuit la division en indiquant qu’il reste 1. Puis on interprète le résultat de bas en haut en concaténant les restes de l’ensemble des opérations en les inscrivant de gauche à droite.

![image-20210922195208415](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20210922195208415.png)



