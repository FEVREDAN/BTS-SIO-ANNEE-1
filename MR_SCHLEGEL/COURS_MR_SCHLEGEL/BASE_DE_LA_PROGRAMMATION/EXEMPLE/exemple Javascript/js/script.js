
/* ID */
const titreH1 = document.getElementById('titrePrincipal');

titreH1.addEventListener('click', function(event) {
   if  (titreH1.innerText == "Tu voulais un nouveau titre ?") {
    titreH1.innerText = "Pourquoi apprendre à programmer ?"
    alert(event.offsetX + '-' + event.offsetY);
   } else {
    titreH1.innerText = "Tu voulais un nouveau titre ?"
   }
}
);

let eleselect = document.getElementById('couleur');

eleselect.addEventListener('change', function(event) {
    if(event.target.value == "") {
        alert("Sélectionner une couleur");
    } else {
        alert("Vous aimez le " + event.target.options[event.target.selectedIndex].text);
    }
});

let eleInput = document.getElementById('textequirendfou');
eleInput.addEventListener('input', function(event) {
    if(event.target.value == "") {
        alert("c'est vide");
    } else {
        alert("Pour le moment ça convient " + event.target.value);
    }
});

/*const titreH1 = document.getElementById('titrePrincipal');

titreH1.addEventListener('click', function() {
    if (titreH1.innerText == "Tu voulais un nouveau titre ?") {

        titreH1.innerText = "Pourquoi apprendre à programmer ?"

    } else {

        titreH1.innerText = "Tu voulais un nouveau titre ?"

    }

}
);*/

/*if (true) {
    titreH1.hidden = true;
} else {
    titreH1.hidden = false;
}*/

/*modifier titre h1*/
titreH1.textContent = "Voila un nouveau titre";
titreH1.classList.add('classTitre');

/* CLASS */
const eMenu = document.getElementsByClassName('eleMenu');
for (let i = 0; i <eMenu.length;i++)
{
  console.log(eMenu[i].textContent);
}

/* Balise */
const titreH2 = document.getElementsByTagName('H2');
for (let i = 0; i <titreH2.length;i++)
{
  console.log(titreH2[i].textContent);
}

/* Recuperer la liste de toutes les div contenant des images */
const img = document.getElementsByClassName('eleImage');
for (let i = 0; i <img.length;i++)
{
  console.log(img[i].textContent);
}

/* afficher la classe du parent de la première div (classname) */
const ediv = document.getElementsByTagName('div');
console.log(ediv[0].parentElement.className);


/* afficher la source du premier fils de la première div (src) */
const eimg = document.getElementsByClassName('eleImage');
console.log(eimg[0].children[0].src);

/* afficher la source du premier fils de l'element qui suit la première div (src) */
console.log(eimg[0].nextElementSibling.children[0].src);

/* ajout class Navigation au nav et condition (visible dans la console)*/
const eNav = document.getElementsByTagName('nav');
eNav[0].classList.add('navigation');
eNav[0].style.backgroundColor = '#C2B3B3'  /*change la couleur du background de la balise nav*/
if (eNav[0].classList.contains('navigation')) {
    console.log("La balise nav contient bien la classe navigation");
} else {
    console.log("La balise nav ne contient pas la classe navigation");
}

if (eNav[0].classList.contains('ClassAbsente')) {
    console.log("La balise nav contient bien la classe navigation");
} else {
    console.log("La balise nav ne contient pas la classe navigation");
}

/* Navigation*/
const eLien = document.getElementsByTagName('a');
eLien[0].setAttribute("href",'#conclusion');
eLien[0].setAttribute("baliseQuiNexisteprobablementpas",'12');
console.log("Valeur de l'attribut" + eLien[0].getAttribute("baliseQuiNexisteprobablementpas"));

/*creation d'un paragraphe et ajout dans le footer */
const para = document.createElement("p");
para.innerText = "2022";
const eFoot = document.getElementsByTagName('footter');
eFoot[0].appendChild(para);

/* ajout info dans html */
const divFin = document.getElementById('fin');
const eleUl = document.createElement("ul");
const eleLi1 = document.createElement("li");
eleLi1.innerText = "element1";
const eleLi2 = document.createElement("li");
eleLi2.innerText = "element2";
eleUl.appendChild(eleLi1);
eleUl.appendChild(eleLi2);
divFin.appendChild(eleUl);

/* changer titre h1 quand on cliqu dessus */
