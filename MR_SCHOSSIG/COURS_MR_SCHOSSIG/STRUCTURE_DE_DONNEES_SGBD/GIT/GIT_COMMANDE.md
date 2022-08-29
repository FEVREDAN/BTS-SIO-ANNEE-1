**GIT_COMMANDE_ANNEXE**

http://rogerdudler.github.io/git-guide/index.fr.html

- git init # créer un nouveau dépôt
- git clone /path/to/repository # créer une copie de votre dépôt local
- git clone username@host:/path/to/repositery # si vous utilisez serveur distant
- git add . (pour tout ajouter sinon juste git add nomdufichier)
- git status # pour voir les changement
- git commit -m "choisir quoi mettre pour voir si c'est une modif" # pour mettre un message
- git commit -a -a "message modif"  # (pour eviter le git add .     et à la fin du cours git push)
- git push # pour envoyer
- git fetch
- ls afficher repertoire sous forme de ligne
- ls -al affiche tous les répertoire en liste même les fichiers cachés*
- ls -a affiche les éléments cachées
- ls -l # affiche les autorisations utilisateurs/groupes/autres





### Ordre pour enregistrer fichier sur GITHUB 

- git add .
- git commit -m "message"
- git push
- git status à tout moments



## Pour créer une clef ssh :

ssh-keygen -t rsa -b 4096    

(la clef sera stocker dans un dossier .ssh dans le dossier utilisateur )

clef ssh = clef asymétrique d'un coté clef privé, l'autre clef public (celle qu'on eut donner au autre) clef privé(crypte) clef public(décrypté)