# 1.Sa se defineasca o functie care primeste ca parametru  un numar natural si o lista de nr naturale si
# reintoarce true daca nr natural folosit ca parametru este regasit in lista si false in caz contrar

def cautare(lista,n):
    for i in range(len(lista)):
        if n == lista[i]:
            return True
    return False

# 2.definiti o functie care primeste ca parametru o matrice de nr naturale si functia sa reintoarca true daca
# gaseste nr nat in interiorul matricii si False in caz contrar

def cautare(matrice,n):
    r = len(matrice)
    c = len(matrice(0))
    for i in range(r):
        for j in range(c):
            if matrice [i] [j] == n:
               return True
    return False
# 3 Sa se scrie o functie recursiva care calculeaza factorialul unui nr natural primit ca parametru
# 4 Sa se scrie o functie recursiva care primeste ca parametru un nr natural si calculeaza de cate ori apare cifra 0
# in numarul respectiv

def factorial(n):
    if n == 0:
        return 1
        return n*f(n-1)
# Sa se det min si maxim dintr o lista
def min_max(lista):
    min=lista[0]
    #index 0
    max=lista[0]
    for i in range(len(lista)):
        if lista[i]>max:
           max=lista[i]
            #i=0
        if lista[i]<max:
           min=lista[i]
        print(min,max)

def min_max(lista):
    min1=lista[0]
    #index 0
    max1=lista[0]
    for i in range(len(lista)):
        if lista[i]>max1 and lista[i]!=max:
            max=lista[i]
            #i=0
        if lista[i]<min1 and lista[i]!=min:
              min1=lista[i]
    print(min,min1,max,max1)

def min_max_sortare(lista):
    lista.sort()
    min1=lista[0]
    min2=lista[1]
    max1=  lista[len(lista)-2]
    max2=  lista[len(lista-1)]
    print(min1,min2,max1,max2)
#Parcurgerea unei matrice
def parcurgere_m(matrice):
    sir="abcd" #sir de aceeasi dimensiune cu n
    n=len(matrice)
    for i in range(n):
        for j in range(n):
            if matrice[i][j]==1:
                print(sir[i], end="")
def nr_cif_zero(n):
    nr_zero=0
    if n==0:
        return 0
        if n%10==0:
            return 1+nr_zero(n//10)
        else:
            return nr_cif_zero(n//10)





    #n=dimensiunea matricii
if __name__=="__main__":
    parcurgere_m([0, 1, 1, 0], [1, 0, 1, 1], [0, 1, 0, 1], [1, 1, 1, 0])