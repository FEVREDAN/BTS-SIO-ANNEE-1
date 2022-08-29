const urlParams = new
URLSearchParams(window.location.search);

const myParam = urlParams.get('ballon');


const ballon = data.find(x => x._id === myParam)
/*alert(ballon.name)*/

let titreh1=document.getElementById('titrePrincipal');
titreh1.innerText='La balle de '+ ballon.name;

let img = document.getElementById('imgBalle');
img.setAttribute("src", "images/" + ballon.imageUrl);

alert(localStorage.getItem('key'));

const btonCart=document.getElementById('addToCart');
btonCart.addEventListener("click", function() {
    localStorage.setItem('Panier', JSON.stringify(ballon));
});