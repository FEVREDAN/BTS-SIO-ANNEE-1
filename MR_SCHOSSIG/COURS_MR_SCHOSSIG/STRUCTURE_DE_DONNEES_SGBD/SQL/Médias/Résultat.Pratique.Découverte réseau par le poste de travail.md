B1.U4.1.2.SEM1.S6.Pratique.Découverte réseau par le poste de travail

1.1. Récupération des informations en mode commande

● Ouvrir une invite de commande :
	○ Menu Windows / rechercher « commande » ou « invite de commandes » ou « cmd »
ou
	○ Menu Windows/ Système Windows / Invite de commande
● Trouver le nom du fichier de commande exécuté pour lancer cette invite de commande :

​	cmd.exe

​	○ les propriétés d’un raccourci sont accessibles avec le clic droit ;
​	○ il faut ouvrir l’emplacement du raccourci pour voir ses propriétés.
Faire une copie d’écran.

![image-20220110163152163](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20220110163152163.png)

![image-20220110163228029](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20220110163228029.png)

NB : Une fois que vous connaissez la commande, vous pouvez aussi lancer l’invite de commande en utilisant : Menu
Démarrer / Exécuter / <nom-de-la-commande>
	● Taper la commande ipconfig
	● Relever les informations propres à la carte réseau réelle
NB : Si des outils de virtualisation ou si une connexion distante type VPN sont installés sur le poste, il peut y avoir
d’autres cartes, notamment des cartes virtuelles. Mais la seule carte dont on se préoccupe pour l'instant est la carte
Ethernet généralement nommée "Connexion au réseau local".

![image-20220110163751623](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20220110163751623.png)

ou 

![image-20220110163853957](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20220110163853957.png)



​	● Taper la commande ipconfig /all
​	● Quelles informations supplémentaires voit-on pour la carte Ethernet (toujours la carte réelle uniquement) ?

![image-20220110164002464](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20220110164002464.png)

ou 

![image-20220110164022927](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20220110164022927.png)

● Voit-on des informations sur la configuration IP de Windows en général (en dehors de toute carte réseau) ?

![image-20220110164153343](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20220110164153343.png)

Taper la commande « set ». Elle affiche le contenu de toutes les variables système à l’instant t.

● Repérer les valeurs de variables et noter leur valeur
	○ COMPUTERNAME = LAPTOP-NUGGVF2I
	○ USERDOMAIN = LAPTOP-NUGGVF2I
	○ USERDNSDOMAIN
	○ USERNAME = fevre
	○ LOGONSERVER = \\LAPTOP-NUGGVF2I
● Pouvez-vous expliquer / deviner à quoi chaque variable correspond concrètement
	○ COMPUTERNAME = Nom de l'ordinateur
	○ USERDOMAIN = Nom de l'utilisateur du domaine
	○ USERDNSDOMAIN
	○ USERNAME = Nom du profil
	○ LOGONSERVER = Nom du serveur de domaine

1.2. Accès aux informations en mode graphique
1.2.1. Informations système
Effectuer un clic droit sur l’icône du menu Windows, choisir le menu contextuel Système, agrandir la fenêtre.
Cliquer sur « Informations système » dans l’angle supérieur droit (lorsque la fenêtre est maximisée)
	● Quelles sont les informations accessibles directement (dans la page d’accueil) ?

![image-20220110165026977](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20220110165026977.png)

​	● A quels aspects de la configuration peut-on accéder via les différents onglets / liens présents dans cette
fenêtre (liens sur la gauche) ?

![image-20220110165059710](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20220110165059710.png)

​	● Que se passe-t-il si on tente d’accéder aux différents items / liens / onglets ? (faire des copies d’écran du
message et/ou de la fenêtre obtenue).

​	● Peut-on accéder au moins en consultation à certaines informations ? (si oui, faire des copies d’écran de la
fenêtre obtenue).

1.2.2. Informations réseau
	● Vous trouverez l’icône « Réseau » :
		○ sur le bureau. Si l’icône n’y est pas, et si une stratégie de sécurité ne vous l’interdit pas, vous pouvez
l’ajouter (cf. point suivant)
		○ dans le menu démarrer (dépend de la version de Windows)

​	○ dans l’explorateur Windows (que vous pouvez ouvrir par la touche windows + e)
● Pour ajouter l’icône « Réseau » sur le bureau :
​	○ Clic droit sur le bureau (en dehors de toute icône),
​	○ Menu contextuel « Personnaliser »
​	○ Clic sur Thèmes
​	○ Clic sur « Paramètres des icônes de bureau »
​	○ Cocher « Réseau »
​	○ [Autre solution : Taper « icône » dans la barre de recherche Windows 10 et ouvrir « Afficher ou
masquer les icônes communes sur le bureau »]
● Une fois l’icône réseau accessible, quel que soit le moyen (essayez les différentes possibilités), pour avoir
accès aux propriétés réseau :
​	○ Cliquer droit sur les propriétés de « Réseau », puis :
■ Cliquer sur « Modifier les paramètres de la carte», puis cliquer droit sur la connexion au
réseau local Ethernet (attention de ne pas cibler une connexion VMWARE ou VIRTUAL BOX)
■ Choisir dans le menu contextuel « Propriétés » dans un premier temps.
​	○ Que se passe-t-il ?

![image-20220110165820144](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20220110165820144.png)

​	○ Comprenez-vous ce qui s’est passé ?