from Domain.rezervare import getClasa, getPret, getId
from Logic.CRUD import adaugaRezervare
from Logic.functionalitati import trecereLaClasaSuperioara, ieftinireRezervariCuCheckinFacut, \
    determinarePretMaximPeClasa, ordonareDescDupaPret, sumaPreturilorPentruFiecareNume


def testTrecereLaClasaSuperioara():
    lista = []
    lista = adaugaRezervare("454", "Costachescu", "business", 400, "da", lista)
    lista = adaugaRezervare("325", "Grigore", "economy", 230, "nu", lista)

    lista = trecereLaClasaSuperioara("Grigore", lista)

    assert getClasa(lista[0]) == "business"
    assert getClasa(lista[1]) == "economy plus"

    lista = trecereLaClasaSuperioara("Costachescu", lista)

    assert getClasa(lista[0]) == "business"

def testIeftinirePretCuUnProcentajDat():
    lista = []
    lista = adaugaRezervare("454", "Costachescu", "business", 400, "da", lista)
    lista = adaugaRezervare("325", "Grigore", "economy", 230, "nu", lista)

    lista = ieftinireRezervariCuCheckinFacut(20, lista)

    assert getPret(lista[0]) == 320.0
    assert getPret(lista[1]) == 230.0

def testDeterminarePretMaximPeClasa():
    lista = []
    lista = adaugaRezervare("454", "Costachescu", "business", 400, "da", lista)
    lista = adaugaRezervare("325", "Grigore", "economy", 230, "nu", lista)
    lista = adaugaRezervare("57", "Galateanu", "business", 456, "da", lista)
    lista = adaugaRezervare("276", "Marin", "economy", 124, "nu", lista)
    lista = adaugaRezervare("973", "Calin", "economy plus", 250, "da", lista)
    lista = adaugaRezervare("100", "Georgescu", "economy plus", 224, "da", lista)

    pretMaximEconomy, pretMaximEconomyPlus, pretMaximBusiness = determinarePretMaximPeClasa(lista)
    assert pretMaximEconomy == 230
    assert pretMaximEconomyPlus == 250
    assert pretMaximBusiness == 456


def testOrdonareDescDupaPret():
    lista = []
    lista = adaugaRezervare("454", "Costachescu", "business", 400, "da", lista)
    lista = adaugaRezervare("325", "Grigore", "economy", 230, "nu", lista)
    lista = adaugaRezervare("57", "Galateanu", "business", 456, "da", lista)
    lista = adaugaRezervare("276", "Marin", "economy", 124, "nu", lista)
    lista = adaugaRezervare("973", "Calin", "economy plus", 250, "da", lista)
    lista = adaugaRezervare("100", "Georgescu", "economy plus", 224, "da", lista)
    lista = ordonareDescDupaPret(lista)
    assert getId(lista[0]) == "57"
    assert getId(lista[1]) == "454"
    assert getId(lista[2]) == "973"
    assert getId(lista[3]) == "325"
    assert getId(lista[4]) == "100"
    assert getId(lista[5]) == "276"

def testSumaPreturilorPentruFiecareNume():
    lista = []
    lista = adaugaRezervare("454", "Costachescu", "business", 400, "da", lista)
    lista = adaugaRezervare("325", "Costachescu", "economy", 230, "nu", lista)
    lista = adaugaRezervare("57", "Galateanu", "business", 456, "da", lista)
    lista = adaugaRezervare("276", "Galateanu", "economy", 124, "nu", lista)
    lista = adaugaRezervare("973", "Calin", "economy plus", 250, "da", lista)
    lista = adaugaRezervare("100", "Calin", "economy plus", 224, "da", lista)
    suma = sumaPreturilorPentruFiecareNume(lista)
    assert suma["Costachescu"] == 630
    assert suma["Galateanu"] == 580
    assert suma["Calin"] == 474

def testUndoRedo():
    lista = []

    'Cream o lista goala'

    undoList = []
    redoList = []

    'Adaugarea a 3 obiecte in lista'

    rezervare = adaugaRezervare("454", "Costachescu", "business", 400, "da", lista)
    undoList.append(lista)
    lista = rezervare
    rezervare = adaugaRezervare("325", "Grigore", "economy", 230, "nu", lista)
    undoList.append(lista)
    lista = rezervare
    rezervare = adaugaRezervare("57", "Galateanu", "business", 456, "da", lista)
    undoList.append(lista)
    lista = rezervare

    'Assert-uri pentru cele 3 rezervari adaugate'

    assert getId(lista[0]) == "454"
    assert getId(lista[1]) == "325"
    assert getId(lista[2]) == "57"

    'Facem undo si apoi assert'

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 2
    assert getId(lista[1]) == "325"
    assert undoList == [[], [["454", "Costachescu", "business", 400, "da"]]]

    'Se mai face un undo si un assert'

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "454"
    assert undoList == [[]]

    'Se mai face un undo si un assert'

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 0
    assert  undoList == []
    assert getId(redoList[2][0]) == "454"

    'Se mai face un undo si un assert, dar acesta nu va avea rezultat'

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert len(lista) == 0
    assert undoList == []
    assert getId(redoList[2][0]) == "454"

    'Se mai adauga 3 rezervari si se fac assert-uri pentru ele'

    rezervare = adaugaRezervare("276", "Galateanu", "economy", 124, "nu", lista)
    undoList.append(lista)
    lista = rezervare
    redoList.clear()
    rezervare = adaugaRezervare("973", "Catalin", "economy plus", 250, "da", lista)
    undoList.append(lista)
    lista = rezervare
    rezervare = adaugaRezervare("100", "Calin", "economy plus", 224, "da", lista)
    undoList.append(lista)
    lista = rezervare

    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3

    'Se face redo, dar acesta nu va avea rezultat'

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()

    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3

    'Se fac doua undo-uri si assert-uri pentru acestea'

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 2
    assert getId(lista[1]) == "973"
    assert undoList == [[], [["276", "Galateanu", "economy", 124, "nu"]]]

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "276"
    assert undoList == [[]]

    'Se face redo si assert pentru acesta'

    undoList.append(lista)
    lista = redoList.pop()
    assert len(redoList) == 1
    assert len(undoList) == 2
    assert len(lista) == 2

    'Se face redo si assert pentru acesta'

    undoList.append(lista)
    lista = redoList.pop()
    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3

    'Se fac doua undo-uri si assert-uri pentru acestea'

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 2
    assert getId(lista[1]) == "973"
    assert undoList == [[], [["276", "Galateanu", "economy", 124, "nu"]]]

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "276"
    assert undoList == [[]]

    'Se mai adauga o rezervare in lista'

    rezervare = adaugaRezervare("199", "Maris", "business", 900, "da", lista)
    undoList.append(lista)
    lista = rezervare
    redoList.clear()

    'Se face redo, dar acesta nu va avea rezultat'

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(lista) == 2
    assert len(undoList) == 2
    assert undoList == [[], [["276", "Galateanu", "economy", 124, "nu"]]]

    'Se face undo si assert'

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert len(undoList) == 1
    assert len(redoList) == 1

    'Se face undo si assert'

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 0
    assert len(undoList) == 0
    assert len(redoList) == 2

    'Se fac doua redo-uri si assert-uri pentru acestea'

    undoList.append(lista)
    lista = redoList.pop()
    assert len(lista) == 1

    undoList.append(lista)
    lista = redoList.pop()
    assert len(lista) == 2
    assert len(redoList) == 0

    'Se mai face un redo'

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(lista) == 2
    assert len(redoList) == 0
    assert len(undoList) == 2

    #Undo si Redo pentru functionalitati

    'Se vor face undo si redo pentru testul de trecere la o clasa superioara pentru rezervarile de pe un anumit nume'

    nume = "Catalin"
    undoList.append(lista)
    redoList.clear()

    lista = trecereLaClasaSuperioara(nume, lista)
    assert lista[1][2] == "business"

    redoList.append(lista)
    lista = undoList.pop()

    assert len(lista) == 2
    assert len(redoList) == 1
    assert len(undoList) == 2
    assert lista[1][2] == "business"

    undoList.append(lista)
    redoList.pop()
    assert lista[1][2] == "business"

    redoList.append(lista)
    lista = undoList.pop()

    assert len(lista) == 2
    assert len(redoList) == 1
    assert len(undoList) == 2
    assert lista[1][2] == "business"

    'Se vor face undo si redo pentru testul de ieftinire a preturilor rezervarilor ce au checkin-ul facut, cu un anumit procentaj'

    procentaj = 20
    undoList.append(lista)
    redoList.clear()

    lista = ieftinireRezervariCuCheckinFacut(procentaj, lista)
    assert lista[1][3] == 720

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 2
    assert len(redoList) == 1
    assert len(undoList) == 2
    assert lista[1][3] == 900

    undoList.append(lista)
    lista = redoList.pop()
    assert lista[1][3] == 720

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 2
    assert len(redoList) == 1
    assert len(undoList) == 2
    assert lista[1][3] == 900














