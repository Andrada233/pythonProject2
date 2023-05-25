# Din lista de adiacenta [[0,1],[0,2][1,2][1,3][3,4]]
# Sa se construiasca matricea prezentata
#nr de elemente
def nr(lista):
 max=0
for element in ():
    for e in element:
        if e>max:
         max=e
return max
#
matrice [0]
n=nr(lista)
for i in range(n):
    rand=[]
    for j in range(n):
        rand.append(0)
        matrice.append(rand)
    for element in lista:
         x=element[0]
         y=element[1]
         matrice[x][y]=1
         matrice[y][x]=1

def lista_adiacenta(mat):
    mat=[]
    matrice=0
    lista=[]
    for i in range(len(mat)):
        for j in range(len(mat)):
            if matrice[i][j]==1:
              lista.append([i][j])

def roll_dice():
    random=0
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    if dice1 ==dice2:
        return True
    else:
        return False
    v=0
    for i in range(1000):
        v+=roll_dice()

