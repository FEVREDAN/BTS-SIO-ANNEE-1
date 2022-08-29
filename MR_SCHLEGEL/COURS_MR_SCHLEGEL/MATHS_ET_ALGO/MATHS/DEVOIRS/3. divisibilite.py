import math

def diviseurs(n):
    cpt = 0
    div = []
    for i in range(round(math.sqrt(n))):
        if n % (i+1) == 0:
            div.append(i+1)
            div.append(n // (i+1))

        cpt = cpt + 1
    print(cpt)
    return list(set(div))

n = 630
l = diviseurs(n)
print(sorted(l))
