Fonction pgcd(a:entier, b:entier):entier

variable locales : 

ecrire a 

ecrire b 

début

​	si b > a alors

​		swap (a,b )     (en python a, b = b, a   inverse la valeur)

​	Fsi

​	tant que b > 0

​		r <- a% b

​		a<- b

​		b<- r

​	ftant

retourne a 

Fin

​	