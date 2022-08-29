LIGNE DE COMMANDE CMD WINDOWS



DIR : affiche les dossier et fichier du répertoire

rm-rf/:supprime ensemble des fichiers du répertoire à la racine

ip qui commence par 169 c'est une creer automatiquement par windows donc pas viable sur le reseau(après un ipconfi /release par exemple)

release = libere

renew = reprise de l'ip





> (>)pour creer et renseigner dans un text qu'on creer, si refait, cela ecrase ce qu'il y a dans le fichier
>





L’invite peut être composée de caractères normaux et des codes spéciaux suivants :

  $A     & (esperluette)
  $B     | (barre verticale)
  $C     ( (parenthèse gauche)
  $D     date actuelle
  $E     code ECHAP (code ASCII 27)
  $F     ) (parenthèse droite)
  $G     > (signe supérieur)
  $H     retour arrière (efface le caractère précédent)
  $L     < (signe inférieur)
  $N     lecteur en cours
  $P     lecteur et chemin d’accès en cours
  $Q     = (signe égal)
  $S     (espace)
  $T     heure actuelle
  $V     numéro de version de Windows
  $_     retour chariot et saut de ligne
  $$     $ (signe dollar)

COLOR

Les attributs de couleurs sont spécifiés par DEUX chiffres hexadécimaux -- le
premier correspond à l’arrière-plan, le second au premier plan. Chaque chiffre
peut prendre n’importe quelle de ces valeurs :

    0 = Noir        8 = Gris
    1 = Bleu        9 = Bleu clair
    2 = Vert        A = Vert clair
    3 = Bleu-gris        B = Cyan
    4 = Rouge      C = Rouge clair
    5 = Violet     D = Violet clair
    6 = Jaune        E = Jaune clair
    7 = Blanc       F = Blanc brillant

Si aucun argument n’est donné, cette commande restaure les couleurs
sélectionnées au moment où CMD.EXE a été ouvert. Cette valeur vient soit de la
fenêtre de la console, du commutateur en ligne de commande /T, ou de la valeur
DefaultColor du registre.

La commande COLOR met ERRORLEVEL à 1 si vous tentez de l’exécuter
avec la même couleur pour l’arrière et le premier plan.

Exemple : « COLOR fc » affiche du rouge sur du blanc

