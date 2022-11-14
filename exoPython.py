size = 3

def generateTable(size):

    table = []

    for i in range(size) :
        table.append([])
        for _ in range (size):
            table[i].append(0)

    for liste in table:
        print(liste)

    return table

def adjacent(liste:list,coordonnées:tuple):
    x=coordonnées[0]
    y=coordonnées[1]
    taille=len(liste)
    listeAdjacents=[]
    if x-1>=0 :
        listeAdjacents.append((x-1,y))
    if x+1<len(liste):
        listeAdjacents.append((x+1,y))
    if y-1>=0 :
        listeAdjacents.append((x,y-1))
    if y+1<len(liste):
        listeAdjacents.append((x,y+1))        
    return listeAdjacents




table = generateTable(size)
print(adjacent(table,(2,1)))