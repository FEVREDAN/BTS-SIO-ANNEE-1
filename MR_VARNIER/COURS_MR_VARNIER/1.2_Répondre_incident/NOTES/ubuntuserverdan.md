



ubuntuserverdan

dan

mdp:210612



pour voir son ip faire : ip a



ip "inet" 192.168.168.130

2 eme vm = 192.168.55.83

pour se co en ssh , depuis le cmd taper : ssh "dan"@192.168.168.130

![image-20211202154057160](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20211202154057160.png)



pour faire instalation auto des mises à jour paquet (avec validation -y)

sudo apt update && sudo apt upgrade -y



pour installer apache 2 :

sudo apt install apache2 -y

![image-20211202154122115](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20211202154122115.png)

sudo systemtxctl status apache2

![image-20211202154138874](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20211202154138874.png)

pour voir server sur navigateur

http:192.168.168.130   (l'ip de la machine )

cd /etc/apache2

![image-20211202154020254](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20211202154020254.png)

configuration de appache2 c'est dans /etc/apache2

apache reconnait uniquement index.html (il faudra changer le nom du portfolio)



pour accéder au fichier install sur le cmd :

sudo vim index.html

pour modifier du texte, il faut appuyer sur "i" pour passer en insertion.  (avec nano on sera directement en insertion)



touche echap ensuite ":"  pour ecrire wq   (w pour enregistre et q pour quitter)



index of (beaucoup du hacking donc faire attention)

pour ajouter un fichier texte faire : sudo touch texte.txt

 pour modifier le fichier : sudo vim texte.txt





"un seul nav qui contient une liste ordonné"



idée savonnerie-nans.fr





pour afficher un fichier faire "cat nomdufichier" ou sudo cat nomdu fichier

pour le modifier faire sudo vim nomdufichier

i pour rentrer en mode insertion

pour quitter le fichier sans modifier 

"touche :echap" ensuite ":" ensuite "q" en "touche:entrée"