# **BASE DE SGBD :**

- Structurer/organiser les données
- stocker les données
- Mettre à jour les données (ajout, modification et suppression d'informations)
- Interroger les données



## Les différents modèles :

* **Fichier XML** : Un peu comme l'HTML (crée plus ou moins à la même époque), est pratique pour un transfère de texte, ce n'est pas lourd et assez pratique. C'est un ancêtre des bases de données  Pour améliorer le XML, ils  ont utiliser ce modèle réseau : c'est quasiment la même chose que le modèle hiérarchique  On peut ajouter des liens facilement.  Le défaut de ce modèle est qu'il nécessite un même développeur sinon, on peut se perdre facilement  

- **Modèles hiérarchique**      # format héritier du modèle hiérarchique est le xml  

  <img src="https://upload.wikimedia.org/wikipedia/commons/d/d0/Pyramid_to_linear_hierarchy.png" alt="Base de données hiérarchique — Wikipédia" style="zoom: 67%;" />

- **modèle réseau** # extension du modèle hiérarchique

  

  ![Les modèles de SGBD - Comment Ça Marche](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMkAAAB3CAMAAACe2JQyAAAAKlBMVEX////N2vPQ0NAhHSBBPkAwLC+trK1xbnAUEBPAv7+TkZJAPD9gXl9QTU+AUZ1RAAADsElEQVR4nO1b25akIAxsgYRw+//fXbS3d72AovZK2KHmYc4ZMzalCRSk+vXq+EEQZag9zGMIWQTgT0VILHgjKFtgIoZjiM7kQXQm/NCZ8ENnwg+dCT90JvzQmfBDZ8IP250W6kZ3WsqpBYCIYPW3GMOfyRoWgo9U7FB7IDchtLSvlyepnMbag7kD45wZf3uQ3jVQGlloqd+jFy4A6cqjuQ4R4E9CmfGMy9YczQ1Y8LN00tJY6VvML+FXr2AYqwZMpeFchwGXGPSgm8uwWOrp9QOhqQwzs1JfQ6j8NXbYr+yYYY1Mx5tS3wAhtJBhCOpwfhI72ccFQ7bUlygMqwdTXM4GWMv6M4v4cTnVw9mxsRUvcUY6KUV4ipdLqwRH8XL18fISL3gn5TmJF0/aw/Uk4SNeUAa6V7hMxIsAILp51MBCvIjIQ+Ft4fGweEm4T4wisN/wCD0qXpIeoZhZlzxC22cSqTzlnPqmR6iuc+qb3YS6zqnvMqnZY+lMOhMmTIbcov2+0AoTgR4oI8WQnBVNMEHyDpS2uWkWpQ7gAhn2TPTUHnVAoJKIF1xUBoTsmQhptYKgZSa7DAXn0TSQXdOnC+tzTHDq17VQJ59P3xfpLTF57l6dSWfCi8l6sTPaXN5pVWWS9AitV74yjxCr76gILQOpj5vj7D+vn0oSzzinjAOMbx/hxvEjB4jJWjPm8WDlcV+RLxDcuM14V6TQF1OsPsTnxPAztxglm3TU2T9t6r+zpH2/pKYwbybO5vv4nnxb5WLnzcTFymV8S+ViwmLOXa3B6FqZkYd1D26tJoZYQi2Ui9k88q0uGsuFe4oNiVUjpfBMYO5IiapkmzdprZoM5QKR7p5lVHd8fWfdEk8Bk+7MLJNp0eE4I4/DSmf+zk7IKH5fCbB5Y83uno6bgIlTUX6129+d8hIw+36Uo302HwEzJvve9eMTg+oCZmrXpNbCJQrOPmpvKTXhtFHfDRoQJR4/8Y+AqVL+Rjp3nOJIEH8K6mCcNQZNFdJMOAAqsPWF+LTLrFkWQNawomqQUkl/GIdKptf+LYyk8Lzn0ZJ0wRWs0AOQK74nyJiKz1LBsU9YpjQ8Hb+43xgEBkn/jsr2KNboSGR9cJ0Lt5T4GuzMypS499oMtoi/QSRp2No6tnLh29CFlSlx+9R/fMP6lDoxN5tGAsps+LbpMD9gf/BAvrSLcTJcXIzvTDqTzqQz6Uw6k86kM+lMOpPO5EczKdsKnQyvsdMq9CadDBcX4zv+G/wCGBMxB2jSgkQAAAAASUVORK5CYII=)

  

- **Modèle relationnel** # fondé sur la théorie mathématique des relations  (SGBDR     le sql est basé dessus). Il est structuré comme des tableaux **Exemple** : Si on veut inscrire des étudiants à un module, on refait un tableau avec le numéros de l'étudiant et le module le correspondant. Nous allons rajouter un tableau quand on veut faire des liens entre d'autres informations. Mathématiquement, on peut stocker n'importe quelle type d'informations rapidement sur ce genre de tableau. L'inconvénient de ce genre de structure, c'est que cela prend pas mal de place. (Langage SGBDR, R pour relationnel)

  

  ![Memoire Online - Conception et réalisation d'un logiciel de suivi des  patients au sein du centre de santé UHAKI - Grâce MURHULA KABI](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiR4OkG_ZDml5S-_4IMLUIuieF9GAxmbV3kA&usqp=CAU)

  

- **Modèle objet** #les données sont représentées sous forme d'objets abandonnées de nos jours ce ne sont plus vraiment des modèles objets . Existe depuis le début de l'informatique, cela à pris 40 ans avant que cela ne prenne forme (depuis 1970) Le langage objet, c'est comme le C#, le C++, php ect... Ce n'est pas parce que ces langages sont dit objet, que le développeur est en train de faire de l'objet

  

  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRH_2C2w6ctm8dkJvlzANyYb6hRPAyB41H5fw&usqp=CAU" alt="Une étude de cas — Documentation Cours de bases de données Septembre 2020" style="zoom: 200%;" />

  * **Base de données objet** : ça n'a pas bien marché, étant donné que les langages objets n'ont que été efficace à partir de nos jours, de plus les machines n'étaient pas assez puissante pour supporter ce genre de langage. 

  * **Base de données SQL**: Les objectifs sont clair, il faut que ce soit rapide et pas très lourd néanmoins la qualité des informations n'est pas de bonne qualité 

  

  - **NOSQL-non structuré** (Not Only SQL)  #

  ![Unité Découverte des fondamentaux des bases de données | Salesforce](data:image/png;base64,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)

  

  Un SGBD est un ensemble de logiciels parmi lesquels on trouve un moteur interprète du langage SQL, une interface de programmation et une interface utilisateur

- Interprète SQL 

  SQL est un language 



## Les principaux gestionnaire de base de données :

- ORACLE (Conçu pour très grosse base de données)
- SQLite (pour petite base de données)
- PostgreSQL( base de données Moyenne 30000 ou 400000)   (linux)
- MySQL ( base de données Moyenne 30000 ou 400000)  (linux)
- Microsoft SQLSERVER'200
- IBM DB2
- Maria DB(projet open source , basé sur MYSQL) (linux)



Les principaux fonctionnalités d'un gestionnaire de base de données:

- Administration des données (créer base, répliquer, sauvegarde)
- Manipulation (CRUD créer lire modifier supprimer (en anglais))
- Efficacité d'accès au données (le temps d'attente doit être en correspondance aux besoins)
- Cohérence des données (si on interroge aujourd'hui et demain la réponses doit être la même)
- Partage des données  (plusieurs accès possible)
- sécurité des données (sécurisé dans le temps et dans le cas d'un accès ou non, interdire des modifications non voulues)



## Les différents types d'utilisateurs :

- Le développeur (avant existence de la base de données; il imagine la structure)
- L'administrateur (garant de la base, assure les fonctionnalités d'administration)
- L'utilisateur (pas informaticiens,utilisateurs final, averti si capable d'interroger le base  )

  
