from doctest import script_from_examples


def year (int):
    leap=False
    if int % 4==0:
        leap=True

    elif int % 4==1:
        leap=False

    return leap

def numeros_seguidos(n):
    for i in range(1, n+1):
        #Eend controla qué se imprime después de cada print.
        print(i, end="")
#print(numeros_seguidos(5))

def max_score():
    score=[1,2,3,4,4,6,6]
    max_score=max(score)
    while max_score in score:
        score.remove(max_score)
    print(max(score))
#print(max_score())

def names_score():
    name=["brandon","milton","valeria","sandra"]
    name.sort()
    score=[1,2,3,4]
    ptyhon_students=[]
    for n in range(len(name)) :
        ptyhon_students.append([name[n], score[n]])

    # Buscar el numero mas pequeño y eliminarlo porque necesitamos el segundo mas pequeño
    min_score = min(score)
    while min_score in score:
        score.remove(min_score)
    # Ahora si estaria el segundo mas pequeño
    min_score_2 = min(score)

    ptyhon_students_organice=[]
    for n in range(len(ptyhon_students)):
        if ptyhon_students[n][1]==min_score_2:
            ptyhon_students_organice.append(ptyhon_students[n])


#print(names_score())


def ciclos():
    localizadores=["hola","buenas"]
    for localizador in localizadores:
        print (localizador)

#print(ciclos())

def ciclos2():
    forms_container=["hola","buenas"]

    for index, container_form in enumerate(forms_container):
        print(index, container_form)
#print(ciclos2())

def ciclos3():
    person_types=("ADT", "CNN", "INF")
    for key in person_types:
        print(key)
print(ciclos3())