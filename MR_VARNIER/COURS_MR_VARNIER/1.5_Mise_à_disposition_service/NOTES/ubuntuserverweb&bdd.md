pour changer l'adresse ip DHCP en static, suivre tuto de ce lien 
https://www.malekal.com/comment-configurer-une-adresse-ip-sur-ubuntu/



![image-20220323093820947](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20220323093820947.png)

![image-20220323093845865](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20220323093845865.png)

Pour installer apache2 il faut :

[Comment installer le serveur web Apache sur Ubuntu 20.04 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04-fr)

![image-20220323095343590](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20220323095343590.png)

![image-20220323095411443](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20220323095411443.png)

Si sudo ufw status retourne "inactive"

il faut rentrer la commande suivante "![image-20220323095456762](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20220323095456762.png)" trouvée sur [sudo ufw status return 'inactif' | DigitalOcean](https://www.digitalocean.com/community/questions/sudo-ufw-status-return-inactive)

faire également un "sudo ufw allow 'OpenSSH' si il n'est pas allow"

Tester la page d'apache en se connectant en ssh sur la machine physique en tapant  dans le cmd " ssh dan@192.168.168.129" puis taper le mot de passe de "dan" sur la vm. 

Ensuite ouvrir un navigateur et taper l'adresse ip de la vm pour voir apparaitre la page d'apache.



Il faut ensuite installer php 

[Installez WordPress 5.5 sur Ubuntu 20.04 LTS (linuxtut.com)](https://linuxtut.com/fr/b259493a39e36f5d524b/)

dispo dans la page (ainsi que apache2 si pas réussi avant)

![image-20220323104636349](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20220323104636349.png)



Installer wordpress 

toujours le même site

![image-20220323104719272](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20220323104719272.png)

Pour installer Mysql

[Comment installer MySQL sur Ubuntu 20.04 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04-fr)

![image-20220323105913355](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20220323105913355.png)
