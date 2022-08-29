# RÉVISION #

[TOC]



# SEM1.S1 Recenser et identifier les ressources numériques

## Système d'exploitation = Un système d'exploitation ( OS Operating System) est un ensemble de programmes qui dirige

l'utilisation des capacités d'un ordinateur (matériel) par des logiciels applicatifs. Grace aux pilotes, préviens erreur en gérant mémoire vive, mémoire de masse, périphériques de saisie. Optimise ressources; gère Système Gestion Fichier (SGF)

SGF = (manipulation fichier dossiers, localisation dossier, sécurité et contrôle fichier) (ex FAT32 , NTFS, ext4)

Poste de travail = ordinateur sur lequel travail un utilisateur.

Le système d'exploitation offre également une interface pour interagir avec composants. Cette interface peut être : 

* mode texte (MS-DOS, Shell Unix ou Linux)    
* mode graphique (Windows, Linux, MacOS, tel port)

MemTest86 = diagnostique défaillances mémoire vive 

OS moderne = Multi : 

* tâche / utilisateurs / processeurs

système d'exploitation  = noyau + bibliothèques + outils système + applications de base

PATCH = correctif logiciel installe après le OS. Corrige bugs ou failles, des fois ajoutent fonctionnalités ou combler défauts et lacunes. Sortie en général hebdomadaire ou mensuel.

mise à jour critique = patch corrige faille de sécurité sérieuse

Service Pack = correctif très volumineux regroupe en 1 mise à jour, tous les patchs. Sortie annuel.

R2 = deuxième version OS avec mises à jour de sécurité et de nouvelles fonctionnalités

RC (Release Candidate) = une des dernières versions bêta d'un OS juste avant sa sortie

RTM (Release To Manufacturer) = version achevée d'un OS destinée à être livrée aux constructeurs pour pré-installent sur machines.

OEM (Original Equipment Manufacturer) = logiciel vendu en même temps qu'un ordinateur. interdit de séparer le logiciel de l'ordinateur avec lequel il a été acheté.

jailbreaker(rooter OS) = donner droits plus élevés sur un OS pour contourner sécurités éditeurs et installer des app non autorisées

Pour distrib Linux Ubuntu version LTS = Long Term Support,

Version 32 bits :

* peut adresser en théorie 232 octets, soit 4 Go de RAM.
* peut adresser en théorie 264 octets, soit 16 Go de RAM

## Licence propriétaire ou libre

Format 

* ouvert = créateur publie spécifications, permet à sociétés de réutiliser format. Il peut demander une redevance s'il veut
* logiciel libre (open-source) = code source téléchargeable mais appartient à personne (linux, distribution)
* logiciel propriétaire = soumis droit d'auteur, décide façon est utilisé logiciel et rétribution (pas forcément "payant".)
* Gratuiciel (freeware) = logiciel propriétaire, distribué gratuitement mais pas libre donc pas consultation de code source
* Partagiciel (shareware) = propriétaire, soumis droit auteur, autorise qu'on l'utilise gratuit pendant une période ou nbr utilisations



## Distribution Linux

OS plus répandu au monde, 

Distribution linux (dépôts de paquetages,maintenance des logiciels,scripts de lancement) :

* Noyau (linux)
* environnement Shell (cmd)
* gestion du système (ajout utilisateur)
* applications
* interfaces graphiques
* communautés…

distribution live = distribution sans installation, boote sur un CD ou USB qui lance OS. (mém de masse pas nécessaire,mais pratique)

# SEM1.S2 GLPI

## Parc informatique 

3 catégories équipements :

- Clients :

  - Ordinateurs (fix ou portable)
  - Moniteurs (attention pas tours)
  - Logiciel et périphériques (clavier souris tablette graphique)
  - Téléphones, tablettes

  

- Réseau :

  - Switches, routeurs, bornes wifi
  - Baies (brassage ou serveurs, grosses armoire métal)
  - Châssis (pour accueillir serveur lames)
  - PDU (Power Distribution Unit = délivre électricité dans salles serveurs)

- Impression :

  - Imprimantes, cartouches, toners

## Les plans

Plan organisationnels :

- Nommage : donner un nom à chacun des équipements (le mieux est d'afficher étiquette sur machine)

  Équipement sur réseau = doit posséder un nom unique NBT (“NetBIOS Over TCP/IP”) ou “Nom NetBIOS”.

  On doit retrouver :

  - Type équipement (pour type maintenance)
  - Lieu présence (situé équipement)
  - Date achat (voir temps d'amortissement)
  - Numéro 

  

- Adressage : permet de donner une adresse IP à chaque équipement connecté au réseau pour être capable d’en déduire info localisation.

  Adresse IP = 4 octets divisés en un num CIDR d'un côté et num Machine de l'autre. Ce découpage s’effectue dans l’adresse IP grâce au masque de sous-réseau qui permet de connaître où s'arrête la
  partie CIDR et où commence la partie numéro de machine.

  ex adressage 10.3.32.1:

  * 1er octet commun ensemble poste = 10
  * 2eme octet lieu géographique = 3 
  * 3eme octet numéro bureau =32
  * 4eme octet numéro machine = 1

## GESTION DE PARC

L’inventaire est le point de départ de toute gestion de parc informatique, on peut anticiper la surutilisation d’un équipements. Il doit être fait **tous les ans**.

deux méthodes : 

- créer les fiches manuellement (longue et fastidieuse,impose vérification, que pour petits parcs)
- FusionInventory

### GLPI

**G**estion **L**ibre de **P**arc **I**nformatique » est un outil ITSM (IT Service Management) qui centralise
info gestion  parc. notamment l’inventaire, ticketing (assistance) et gestion admin et financière.

GLPI est open source sous licence GPL (General Public License) V3 maintenu par Teclib, il est libre d’être installé, modifié et copié

GLPI architecturé référentiel ITIL.

### FusionInventory 

C'est un plugin (s’intégrant dans GLPI) et un agent d’inventoring, automatisant remontée infos depuis postes à inventorier vers serveur GLPI. Il tend à remplacer  OCS Inventory dans GLPI, en simplifiant requêtes dans le
serveur GLPI.

OCS Inventory nécessite une synchronisation entre sa BDD et celle de GLPI, grâce plugin de synchro

Agent OCS → Serveur OCS → Plugins OCS dans GLPI → Serveur GLPI.

FusionInventory agit direct avec GLPI sans passer par serveur tiers. Il est fusionné dans GLPI, les interactions sont en direct. FusionInventory = client serveur GLPI.

Agent FusionInventory → Plugins FusionInventory dans GLPI → GLPI

### Agent d’inventoring

Sert à inventorier l’ordinateur (composants et logiciels) automatiquement

FusionInventory est un “agent” qu'on installe sur un ordinateur ou un serveur. il synchronise avec le plugin FusionInventory installé dans GLPI ,se comporte comme un intermédiaire direct entre GLPI et l’agent Fusion,créer ou de modifier une fiche dans la partie PARC de GLPI.

### Dictionnaire d’importation

Ensemble de règles qui permettent de regrouper en une fiche plusieurs objets identiques dès
qu’elles y détectent un mot clé prédéfini.

### Cycle de vie d’un équipement du parc

* Exprimer besoin utilisateur (récolte demande et comprendre pour savoir ce qu’il faut pour parc.)
* Devis fournisseur (choisir devis correspondant le mieux à vos contraintes et à vos besoins)
* Achat & mise en service
* Utilisation
* Inventaire
* Réforme :
  * Jeter (déchèterie, point de collecte)
  * Démonter (pièces)
  * Don (Green IT) (assoc, écoles, personnel)

# SEM1.S4 Partage local

## Répertoire partagé

ils permettent un accès direct à une ressource stockée sur un ordinateur ou un serveur, qui devient disponible pour les utilisateurs du réseau. L’accès s’effectue par chemin UNC (Universal Naming Convention). Contient le nom de l’ordi ou serveur qui héberge ainsi que nom de partage de la ressource (exemple : \\SRV01\Data).

Pour cacher un partage et transformer en partage administratif = UNC suivis de "$"

## Gérez comptes utilisateurs

Administrateur = seul à pouvoir modifier paramètres système OS et droits autres utilisateurs 

Listez les utilisateurs présents sur votre ordinateur (disponible que version Pro ou Entreprise de Windows) = clic droit sur le menu Démarrer et "Gestion de l'ordinateur > Outils système > Utilisateurs et Groupes
locaux, cliquez sur « Utilisateurs »".

### Les groupes

facilitent la gestion des droits utilisateur, par défaut, Windows place votre utilisateur dans le groupe Administrateurs(droit installe logiciels et regarder dossiers de tous utilisateur) et dans le groupe Utilisateurs (peut pas installer de logiciels et ne peut consulter que ses fichiers.)
