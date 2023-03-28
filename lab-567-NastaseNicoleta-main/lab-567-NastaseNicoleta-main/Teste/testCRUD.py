from Domain.rezervare import getId, getNume, getClasa, getPret, getCheckin_facut
from Logic.CRUD import adaugaRezervare, getById, stergeRezervare, modificaRezervarea
from Logic.functionalitati import trecereLaClasaSuperioara, ieftinireRezervariCuCheckinFacut, \
    determinarePretMaximPeClasa


def testAdaugaRezervare():
    lista = []
    lista = adaugaRezervare("454", "Costachescu", "business", 400, "da", lista)
    assert len(lista) == 1
    assert getId(getById("454", lista)) == "454"
    assert getNume(getById("454", lista)) == "Costachescu"
    assert getClasa(getById("454", lista)) == "business"
    assert getPret(getById("454", lista)) == 400
    assert getCheckin_facut(getById("454", lista)) == "da"

def testStergereRezervare():
    lista = []
    lista = adaugaRezervare("454", "Costachescu", "business", 400, "da", lista)
    lista = adaugaRezervare("325", "Grigore", "economy", 230, "nu", lista)

    lista = stergeRezervare("454", lista)
    assert len(lista) == 1
    assert getById("454", lista) is None
    assert getById("325", lista) is not None


def testModificareRezervare():
    lista = []
    lista = adaugaRezervare("454", "Costachescu", "business", 400, "da", lista)
    lista = adaugaRezervare("325", "Grigore", "economy", 230, "nu", lista)

    lista = modificaRezervarea("454", "Dumitru", "economy", 230, "nu", lista)
    rezervareUpdatata = getById("454", lista)
    assert getId(rezervareUpdatata) == "454"
    assert getNume(rezervareUpdatata) == "Dumitru"
    assert getClasa(rezervareUpdatata) == "economy"
    assert getPret(rezervareUpdatata) == 230
    assert getCheckin_facut(rezervareUpdatata) == "nu"


    rezervareNeupdatata = getById("325", lista)
    assert getId(rezervareNeupdatata) == "325"
    assert getNume(rezervareNeupdatata) == "Grigore"
    assert getClasa(rezervareNeupdatata) == "economy"
    assert getPret(rezervareNeupdatata) == 230
    assert getCheckin_facut(rezervareNeupdatata) == "nu"















