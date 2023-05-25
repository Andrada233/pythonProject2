# o fct cautare intr o lista daca el este gasit sa reintoarca pozitia
def cautare(lista,element_cautat):
    l=[2,3,4,5,6]
    for i in range (len(l)):
         if lista[i]==element_cautat:
            return i
    return -1

# cautare

def generareCNP(gen,an,luna,zi,judet,nnn,):
    CNP=""
    if gen =="M" or gen =="m" or gen=="masculin":
        if an<2000:
            CNP +="1"
        else:
            CNP+="5"
    else:
        if an<2000:
            CNP+="2"
        else:
            CNP+="6"
    if an<2000:
        an=an-1900
    else:
        an=an-2000
    if an<10:
        CNP +="0"
    CNP += str(an)
    if luna<10:
        CNP+="0"
    CNP += str(luna)
    if zi<10:
        CNP +="0"
    CNP += str(zi)
    if judet<10:
        CNP +="0"
    CNP += str(judet)
    if nnn<10:
        CNP +="00"
    elif nnn<100:
        CNP +=""
    CNP += str(nnn)
    return CNP

def generareC(sir):
    sirControl="279146358279"
    suma=0
    for i in range(len(sir)):
        suma+=int(sir[i])
    if suma%11==10:
        return 1
    else:
        return suma%11


if __name__=="__main__":
    print(generareCNP("m", 1980, 1, 1, 24, 999))