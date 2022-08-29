● La lecture (r) : on peut par exemple lire le fichier avec un logiciel. Lorsque ce droit est alloué à un dossier, il
autorise l'affichage de son contenu (liste des fichiers présents à la racine de ce dossier).
● L'écriture (w) : on peut modifier le fichier et le vider de son contenu. Lorsque ce droit est alloué à un dossier,
il autorise la création, la suppression et le changement de nom des fichiers qu'il contient (quels que soient
les droits d’accès). Le droit spécial sticky bit permet de modifier ce comportement.
● L'exécution (x) : on peut exécuter le fichier s'il est prévu pour, c'est-à-dire si c'est un fichier exécutable.
Lorsque ce droit est attribué à un dossier, il autorise l'accès (ou ouverture) au dossier.
On appelle parfois r, w et x des « flags » ou « drapeaux ». Sur un fichier donné, ces 3 « flags » doivent être définis
pour son propriétaire, son groupe, mais aussi les autres utilisateurs (différents du propriétaire et n'appartenant pas
au groupe).

![image-20211208075304599](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20211208075304599.png)