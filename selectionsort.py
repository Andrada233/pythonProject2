# presupune ca primul element este minimul
#se compara primul cu urmatorul, daca al doilea e mai mic i se atribuie minim
def selectionSort(itemsList):
    n = len(itemsList)
    for i in range(n):
        minValueIndex=i

        for j in range(i+1,n):
            if itemsList[j]<itemsList[minValueIndex]:
                minvalueindex=j

        if minValueIndex !=i:
            temp=itemsList[i]
            itemsList[i]=itemsList[minValueIndex]
            itemsList[minValueIndex]=temp

    return itemsList
data=[1,5,9,1,4,3]
selectionSort(data)
print('Sorted Array in Ascending Order:')
print(data)

employee1={
    'id':14,
    'name':'John Doe',
    'age':36,
    'position':'Business Manager.'
}
employee2={
    'id': 2,
    'name': 'Jane Doe',
    'age': 20,
    'position': 'N/A'
}
employee3={
    'id': 110,
    'name': 'John Smith',
    'age': 40,
    'position': 'Software Deleveloper.'
}
employee4={
    'id': 40,
    'name': 'Jane Smith',
    'age': 35,
    'position': 'Engineer.'
}
#functie care cauta angajatu pt care id este 2
list1=[employee1, employee2,employee3,employee4]
def cautareID(lista, id_cautat):
        for i in range (len(lista)):
            if lista[i]['id']==id_cautat: #cautare dupa ID
               return lista[i]
            return None