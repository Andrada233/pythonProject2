def masini():
    T=0
    lista_timpi_reparatie_masini=[4,6,7,8,9,10]
    t=int(input("Timp maxim de lucru:"))
    lista_timpi_reparatie_masini.sort()
    t_ramas = T
    for i in range(len(lista_timpi_reparatie_masini)):
        if lista_timpi_reparatie_masini<=t_ramas:
            t = t_ramas - lista_timpi_reparatie_masini[i]
            lista_timpi_reparatie_masini.append(lista_timpi_reparatie_masini[i])


#Suma numerelor dintr o lista folosind recursivitatea
def suma_recursiv():
    i=0
    lista=0
    if len(lista) == 1:
        if lista[i]%2 == 0:
           return lista[0]
        else:
           return 0
    #pentru cele impare if lista[0] !=0:
    # se da o matrice patratica sa se determine valoarea elementul care contine val max si el care contine val min
def matrice(min,max):
    m=0
    n=0
    min = 9999
    max = 0
    for i in range (m):
        for j in range (n):
            #parcurgere matrice , definesc min nu cu o valoare foarte mare ex 9
        #definesc max cu o valoare mica de ex 0
        # intr o matrice i si j reprez indicii iar elementele matricei se reg. folosind expr matrice i,j
          if [i][j]>max:
            max = matrice [i] [j]
          if [i] [j]<min:
            min = matrice [i] [j]
        print("Maxim",max)
        print("Minim",min)
         # se da matrice patratica sa se genereze elementele matricii dupa urmatoarele reguli:
        # elementele pentru care produsul indicilor este un nr par vor avea valoare 1 el pt care produsu indicilor
        # este nr impar vor avea val 0 el de pe diagonala principala vor avea val 2
def elemente_matrice(matrice):
    j=0
    m = len(matrice[0])
    n = len(matrice[0])
    for i in range (m):
        for i in range (n):
            if i*j % 2 == 0:
                matrice [i][j]
            if i*j % 2 ==1:
                matrice [i] [j] = 0
            if i==j:
                matrice [i] [j] = 2
    #
def unire(listas, listad):
    rezultat = []
    i = 0
    j = 0
    while i<len(listas) and j< len(listad):
        if listas[1]<listad[i]:
            rezultat.append(listas[1])
            i = i+1
        else:
            rezultat.append(listad[1])
            j = j +1
    while i<len(listas):
        rezultat.append(listas[i])
        i = i+1
        while j<len(listad):
          rezultat.append(listad[j])

def msort(lista):
    if len(lista)<=1:
        return lista
    else:
        mij = len(lista)//2
        stanga = msort(lista[:mij])
        dreapta = msort(lista[mij:])
        return unire(stanga,dreapta)

def cautare(lista, element): #parcurgere
    list=[1,2,3,4,5,6,7]
    for i in range (len(lista)):
          print(lista[i])


def cautare(lista, element): #parcurgere trebuie sa contina if
    for i in range (len(lista)):
        if lista[i]==element:
            return 1
    return -1

if __name__ == '__main__':
    cautare()