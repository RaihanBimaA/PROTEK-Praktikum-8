def kuadrat(bil) :
    
    bilSquare = []
    
    for i in range(len(bil)) :
        
        kuadrat = bil[i] * bil[i]
        bilSquare.append(kuadrat)
        
    return bilSquare




bil = [2, 4, 5, 6, ]

hasil = []

hasil = kuadrat(bil)

print(hasil)

