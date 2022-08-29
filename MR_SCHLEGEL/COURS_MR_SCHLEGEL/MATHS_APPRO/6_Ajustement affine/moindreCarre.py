def donneEcart(l, a, b):
    s = 0
    for e in l:
        y_droite = a * e[0] + b
        s = s + (y_droite - e[1])**2
    
    return s

l = [
(0,0),
(1,5),
(2,9),
(3,16),
(4,18),
(5,20),
(6,27) ]
print("Droite 4*x+1 : ", donneEcart(l, 4, 1))
print("Droite 4.3*x+0.5 : ", donneEcart(l, 4.3, 0.5))
print("Droite idéale : ", donneEcart(l, 4.2857, 0.7143))


