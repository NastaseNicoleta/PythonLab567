from Domain.rezervare import toString
from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervarea
from Logic.functionalitati import trecereLaClasaSuperioara, ieftinireRezervariCuCheckinFacut, \
    determinarePretMaximPeClasa, ordonareDescDupaPret, sumaPreturilorPentruFiecareNume


def printMenu():
    print("1. Adauga rezervare")
    print("2. Sterge rezervare")
    print("3. Modifica rezervare")
    print("4. Trecere rezervare cu un nume dat la o clasa superioara")
    print("5. Ieftinire pret rezervari, care au checkin-ul facut, cu un procentaj dat ")
    print("6. Determinare pret maxim pe clase")
    print("7. Ordoneaza descrescator rezervarile dupa pret")
    print("8. Afiseaza suma preturilor pentru fiecare nume")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare rezervari")
    print("x. Iesire")


def uiAdaugareRezervare(lista, undoList, redoList):
    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    clasa = input("Dati clasa: ")
    pret = float(input("Dati pretul: "))
    checkin_facut = input("Dati stadiul checkin-ului: ")
    rezultat = adaugaRezervare(id, nume, clasa, pret, checkin_facut, lista)
    undoList.append(lista)
    redoList.clear()
    return rezultat


def uiStergereRezervare(lista, undoList, redoList):
    id = input("Dati id-ul rezervarii de sters: ")
    rezultat = stergeRezervare(id, lista)
    undoList.append(lista)
    redoList.clear()
    return rezultat


def uiModificareRezervare(lista, undoList, redoList):
    id = input("Dati id-ul rezervarii de modificat: ")
    nume = input("Dati noul nume: ")
    clasa = input("Dati noua clasa: ")
    pret = float(input("Dati noul pret: "))
    checkin_facut = input("Dati noul stadiu al checkin-ului: ")
    rezultat = modificaRezervarea(id, nume, clasa, pret, checkin_facut, lista)
    undoList.append(lista)
    redoList.clear()
    return rezultat

def uiTrecereLaClasaSuperioara(lista, undoList, redoList):
    try:
        nume = input("Dati numele pentru care doriti sa se modifice clasa:")
        rezultat = trecereLaClasaSuperioara(nume, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiIeftinirePretRezervariCuCheckinFacut(lista, undoList, redoList):
    try:
        procentaj = float(input("Dati procentajul cu care doriti sa se faca ieftinirea:"))
        rezultat = ieftinireRezervariCuCheckinFacut(procentaj, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiDeterminarePretMaximPeClasa(lista):
    try:
        pretMaximEconomy, pretMaximEconomyPlus, pretMaximBusiness = determinarePretMaximPeClasa(lista)
        print("Pretul maxim la clasa economy este " + str(pretMaximEconomy))
        print("Pretul maxim la clasa economy_plus este " + str(pretMaximEconomyPlus))
        print("Pretul maxim la clasa business este " + str(pretMaximBusiness))
    except ValueError as ve:
        print("Eroare: {}".format(ve))



def uiOrdonareDescDupaPret(lista):
    listaNoua = []
    listaNoua = ordonareDescDupaPret(lista)
    if len(listaNoua) > 0:
        print("Rezervarile ordonate sunt:")
        showAll(listaNoua)
    else:
        print("Nu exista rezervari")

def uiSumaPreturilorPentruFiecareNume(lista):
    suma = sumaPreturilorPentruFiecareNume(lista)
    for nume in suma:
        print("{} are suma de {}".format(nume, suma[nume]))



def showAll(lista):
    if len(lista) > 0:
        for rezervare in lista:
            print(toString(rezervare))

    else:
        print("Nu exista rezervari")


def runMenu(lista):
    undoList = []
    redoList = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugareRezervare(lista, undoList, redoList)
        elif optiune == "2":
            lista = uiStergereRezervare(lista, undoList, redoList)
        elif optiune == "3":
            lista = uiModificareRezervare(lista, undoList, redoList)
        elif optiune == "4":
            lista = uiTrecereLaClasaSuperioara(lista, undoList, redoList)
        elif optiune == "5":
            lista = uiIeftinirePretRezervariCuCheckinFacut(lista, undoList, redoList)
        elif optiune == "6":
            uiDeterminarePretMaximPeClasa(lista)
        elif optiune == "7":
            uiOrdonareDescDupaPret(lista)
        elif optiune == "8":
            uiSumaPreturilorPentruFiecareNume(lista)
        elif optiune == "u":
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redoList) > 0:
                undoList.append(lista)
                lista = redoList.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")








