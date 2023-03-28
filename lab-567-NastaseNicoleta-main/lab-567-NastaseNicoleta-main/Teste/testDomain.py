from Domain.rezervare import creeaza_rezervare
from Domain.rezervare import getPret
from Domain.rezervare import getId
from Domain.rezervare import getNume
from Domain.rezervare import getClasa
from Domain.rezervare import getCheckin_facut

def testRezervare():
    rezervare = creeaza_rezervare("454", "Costachescu", "business", 400, "da")
    assert getId(rezervare) == "454"
    assert getNume(rezervare) == "Costachescu"
    assert getClasa(rezervare) == "business"
    assert getPret(rezervare) == 400
    assert getCheckin_facut(rezervare) == "da"
    
