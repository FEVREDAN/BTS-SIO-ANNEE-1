def sommeTermes(dep, arr):
    s = 0
    for i in range(dep, arr+1):
        s = s + (7 * (3**i))

    return s

def sommeTermeRapide(dep, arr):
    return (7 * (3**dep)) * ((1-(3**(arr-dep +1)))/(-2)) 


print(sommeTermes(1,5))
print(sommeTermeRapide(1,5))