def donneSomme(dep, arr):
    somme = 0
    for i in range(dep, arr+1):
        somme = somme + (3 * i + 2)
    return somme

def donneSommeFormule(dep, arr):
    return (arr - dep +1) * ((3 * dep + 2) + (3* arr + 2)) / 2

print(donneSomme(25, 37))
print(donneSommeFormule(25, 37))