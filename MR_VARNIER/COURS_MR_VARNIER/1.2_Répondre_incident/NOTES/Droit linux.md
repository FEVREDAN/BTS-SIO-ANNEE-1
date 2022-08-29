Droit linux 



![image-20211119142311025](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20211119142311025.png)

accorder les droit : 

("d" pour repertoire, "-" pour fichier et "l" pour lien logique)  rwx(proprietaire) rwx(groupe) rwx(autre)

chmod (u g ou o pour utilisateur, groupe, autre)+(wpour write,r poue read, x pour executer) "fichier que je veux accorder les droits sans les guillements"

chmod u+wrx fichierauhasard.txt

r w x = 7 

r = 4

w = 2

x = 1

-= 0

rwx r-x  r--  = 754

rwx rwx rwx = 777

rwx rwx rwx = 7(utilisateur)7(groupe)7(autre)

ls (voir les droits)

 -l (l pour liste)

donc ls -l voir les droit du répertoire courant en liste

ls -lR( R pour récursivité)

si on a un repertoire A/AA/AAA/AAAA.text

si on fait ls -lR A/  (affiche tout les dossier et sous--dossier et fichier qui sont contenus dans A/)

si on fait chmod -R 750 A/   (enlève tout les droit au autres sur les dossier A et les sous-dossier et fichiers)





pwd =voir fichier courant

exo 2)

cp -R TravauxPratique2 TravauxPratique3bis

rm -R TravauxPratique3bis

exo 3)

touch test.txt

rm : supprimer 'test.txt' qui est protégé en écriture et est du type « fichier vide » ? 
