# Créer et intégrerdes styles CSS



## A quoi ça sert ? 

Le CSS sert à gérer la mise en page de notre site. Les commande CSS peuvent être utiliser directement dans le code HTML mais il est préférable de les mettre dans un fichier CSS pour faciliter les modification ou pouvoir modifier l'interface sans toucher au code HTML.

```html
<!-- Commande pour lier le fichier CSS au code html -->
<head>
    <link rel="stylesheet" href=".style/monStyle.css" type="text/css" >
</head>
```

Le CSS permet les chose suivante :

- Gérer le fond de mon site
- Changer la police
- Changer l'emplacement de mon menu
- Effet quand on survole un bouton
- Dimension adaptative 

il y a possibilité de mettre un balise ***<style>***  pour mettre du CSS dans de l'html

## Les première commande :

### Couleur police titre

```css
/* Modifier le style des titre */
h1{
    color: blue;
}
```



### Couleur fond paragraphe

```css
/* Modifier fond des paragaphe */
p{
    background-color: gray;
}
```



### Les balise

```css
Balise{
    prop1:val1;
    prop2:val2;
}
```



### Le Regroupement de Propriété :

```css
Balise1, Balise2{
    color: red;
}
```



## Appliquer de style sur des zone précise

### Les ID

``` html
<!-- HTML -->
<h1 id="titre_Principal">Votre Titre principal</h1>
```

```css
/* CSS */
#titre_Principal {
    prop1:val1;
    prop2:val2;
}
```

***NOTA :*** les ID sont a usage unique

### Les Class

```html
<!-- HTML -->
<h1 class="ZONE_1">Votre Titre principal</h1>
<p class="ZONE_1">
    TEXT
</p>
```

```css
/* CSS */
.ZONE_1 {
    prop1:val1;
    prop2:val2;
}
```

***NOTA :*** les Class sont utilisable plusieurs fois

### Les balise div

```html
<!-- HTML -->
<div class="ZONE">
    <h1>Titre</h1>
    <p>
        TEXT
    </p>
</div>
```

````css
/* CSS */
div.ZONE {
    prop1:val1
    prop2:val2
}
````

***NOTA :*** les div sont des balise block qui entoure de zone

### Les balise span

```html
<!-- HTML -->
<p>
    TEXT<span class="ZONE">TEXT DIF</span>
</p>
```

```css
/* CSS */
span.ZONE {    
    prop1:val1    
    prop2:val2
}
```

***NOTE :*** les span sont des balise qui permette de modifier des style dans des balise

## Les sélecteur avancer :

``` css
* {} /*Toute les balises*/
.para1et2 p {} /*Une balise dans une autre*/
.h3 + p {} /*Une balise qui suis une autre*/
img[title] {} /*Balise qui possède un attribut*/
img[title="île déserte"] {} /*Balise qui possède un attribut précie*/
img[title*="île"] {} /*Balise qui posséde un attribut contenant "île"*/
```

## Les style de texte :

### Les tailles de police

```css
/*Absolue (en px cm ou mm)*/
p{front-size: 14px;}
h1{ front-size: 40px;}

/*Relatif (en pourcentage)*//*recommandée*/
h1{font-size: 1.5em;}/*1.5 = 150 %*/
```

### Le type de police

Sélectionner la police :

```css
p{front-family: Arial,"Courier New", Verdana, serif;} /*Applique la police la plus a gauche si il la possède sinon passe à la suivante*/
```

Forcer une police pas disponible en la faisant ce faire DL par le client :

```css
@font-face {
    font-family: 'maPolice';
    src:	url('maPolice.eot') format('eot'),
        	url('maPolice.ttf') format('truetype');
}
h1 {
	font-family: 'maPolice', Arial, serif;
}
```

### Le Style de la police

```css
h1{
    front-style: italic; /*Italic*/
    front-weigth: bold; /*Gras*/
    text-decoration: underline; /*Souligner*/
}
h2{
    front-style: italic;
    text-decoration: line-through;
}
p{
    front-style: normal;
}
```

### Les alignements horizontaux :

```css
h1{
    text-align : center
}
h2{
    text-align : left
}
h3{
    text-align : right
}
p{
    text-align : justify
}
```

### Les alignements verticaux :

```css
#case1 {
    vertical-align : text-top;
}
#case2{
    vertical-align : baseline;
}
#case3{
    vertical-align : text-bottom;
}
```

### Entourer avec du texte :

```html
<p><img src="image.gif" class="imageClass" /> Voici un petit texte qui si tout se passe bien habillera de manière assez habile une image.</p>
```

```css
. imageClass {
	float : left; /*Alignement à gauche*/
}
```

```css
. Jeveuxquecasarrete {
	clear : both; /*Fin de l'alignement*/
}
```

### Gestion majuscule :

```css
h1 {
	text-transform : uppercase;
}

h2 {
	text-transform : capitalize;
}

h3 {
	text-transform : lowercase;
}
```



## La couleur 

### Couleur de police :

```css
h1 {
	color : blue /*Couleur Texte*/
}

h1 {
	color : #B2F020 /*Couleur hexadecimal*/
}

h1 {
	color : rgb(240, 96, 204) /*Couleur RGB*/
}
```

### Couleur de fond :

```css
h1{
    background-color : rgb(240, 96, 204) /*Fond uni pour titre 1*/
}
```

```css
body {
	background-image : url("monImage.png");
	background-size: 300px 300px; /*regler la taille du fond*/
}

body {
	background-image : url("monImage.png");
	background-attachment: fixed /*Fixe le fond lors du deffilement*/
}
body {
	background-image : url("monImage.png");
	background-repeat: repeat; /*repete le motif hori repeat-x verti repeat-y */
}
body {
	background-image : url("monImage.png");
	background-repeat: no-repeat; /*pas de repetition*/
	background-position: 50px 100px; /*50px a gauche 100px en bas*/
}
body {
	background-image : url("monImage.png");
	background-repeat: no-repeat;
	background-position: top right; /*pour positioner en au a droite*/
}
```

### La transparance :

```css
h1 {
	opacity: 0.6; /*60%*/
}
```

```css
h1 {
	background-color: rgba(140, 22, 250, 0.5); /*rgb + opaciter = RGBA*/
}
```

***NOTA :*** Les vieux navigateur le gère pas le RGBA donc on utilise

```css
h1 {
	background-color: rgb(140, 22, 250);
	background-color: rgba(140, 22, 250, 0.5);
}
```



## Habillages de balises

### Les bordures :

```css
h1{
    border-width : 2px;
    border-color : #FF0000;
    border-style : solid;
}

/*Version Factoriser*/
h1{
    Border : 2px #FF0000 solid
}

/*On peut selectionner un coter avec*/

Border-top		Border-top-width
Border-bottom	Border-bottom-style
Border-left		Border-left-color
Border-right	

```

### Les arrondis de bordure :

```css
h1 {
	border-radius: 10px;
}

h1 {
	border-radius: 10px 5px 10px 5px; /*Haut G, Haut D, Bas D, Bas G*/
}
```

### Les Ombres :

```css
p {
	text-shadow: 2px 2px 1px black;
}
/*Les 4 valeurs de la propriété correspondent à :
	Décalage horizontal de l'ombre
	Décalage vertical de l'ombre 
	Adoucissement du dégradé
	Couleur de l'ombre
*/
```

### Les effets en survol

```css
p:hover		/*Survol*/
p:active	/*Clic*/
p:focus		/*Selection*/
p:visited	/*Visiter*/
```

Images de fond fixe 

```css
#background {
    position: fixed;
    z-index: -1; /* pour que ce sois en "arriere plan" */
    top: 0; /* on place la division en haut a droite */
    left: 0;
}
```

image de fond 

```css
header.fond {
    background-image: url("../images/accueil.jpg"); /* The image used */
    background-color: #6a6363; /* Used if the image is unavailable */
    background-position: center; /* Center the image */
    background-repeat: no-repeat; /* Do not repeat the image */
    background-size: cover; /* Resize the background image to cover the entire container */
    background-attachment: fixed;
}
```

```css
<img class="fond" alt="fond" src="../CSS/images/accueil.jpg" width="100%"/>
```

