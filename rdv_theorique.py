somme = 0

for i in range(0,60):
    for j in range(0,60):
        attente = abs(i-j)
        somme += attente

nb = 60*60
moyenne = somme/nb
print("La moyenne (theorique) : ", moyenne);