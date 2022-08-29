128 64 32 16 8 4 2 1

145.245.45.225



  classe b                              145                                                245                                   45                        225                     2^6 > 60>2^5

adresse ip                      1001 0001                                      1111 0101                         0010 1101           1110 0001

masque                   255(1111 1111)                                255(1111 1111)                        0000 0000          0000 0000 

adresse reseau              1001 0001                                       1111 0101                         0000 0000          0000 0000

CIDR : 145.245.0.0/16

le cidr correspond au bit en 1 dans le masque sous réseau

donc un masque 255.255.0.0/16pour avoir 60 sous réseau :

je regarde doit prendre l'interval entre 64 et 32 donc c'est 2^6 (le plus grand)donc on prend 128+64+32+16+8+4 (6bit) qui font 252

donc 255.255.0.0/16 se change en 255.255.252.0/22

![image-20220124165747332](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20220124165747332.png)



97.124.36.142                 97                                    124                                          36                           142                     

adresse ip                0110 0001                           0111 1100                               0010 0100               1000 1110

masque            255(1111 1111)                            0000 0000                               0000 0000                 0000 0000  

adresse reseau       0110 0001                            0000 0000                               0000 0000                 0000 0000

cidr de base = 97.124.36.142/8

![image-20220126082426687](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20220126082426687.png)

![image-20220126082532645](C:\Users\fevre\AppData\Roaming\Typora\typora-user-images\image-20220126082532645.png)

39 = 0010 0111

127 = 0100 0001

199 = 1100 0111

245 = 1111 0101

32.0.10.5

32 = 0010 0000

0 = 0000 0000

10 = 0000 1010

5 = 0000 0101



136.254.12.1

136 = 1000 1000

254= 1111 1110

12 = 0000 1100

1 = 0000 0001

192.168.0.1

192 = 1100 0000

168 = 1010 1000

0 = 0000 0000

1 = 0000 0001