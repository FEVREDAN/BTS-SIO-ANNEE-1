# def somme(n):
    
#         if n == 0:
#             return 0
#         else:
#             return (n + somme(n-1))


# print(somme(6))


# def somme(n):
#     while True:
#         if n == 0:
#             return 0
#         else:
#             n = (n + somme(n-1))
#             print(n)
#             return (n)


# print(somme(6))

# liste_temperatures = [15, 16, 17, 18, 15]

# moyenne = ((sum(liste_temperatures))/(len(liste_temperatures)))

# print(moyenne)

# liste_temperatures = [15, 16, 17, 18, 15]
# tot = 0

# for i in range(len(liste_temperatures)):
#     tot = tot + liste_temperatures[i]

# print(tot/len(liste_temperatures))



# t= input()
# tab.append(t)

# print(tab)
# t= input()
# tab.append(t)
# print(tab)

tab = [0] * 30

for i in range(len(tab)):
    tab[i]= input()

print(tab)