from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervarea
from Domain.rezervare import toString


def showAll(lista_1):
    if bool(lista_1) is False:
        print("Lista de rezervari este acum goala")
    else:
        for rezervare in lista_1:
            print(toString(rezervare))


def main_command_line(new_list_1):
    while True:
        mesaj = input()
        if mesaj == "help":
            print("adaugare,Id,Nume,Clasa,Pret,Checkin_facut - va adauga un element nou in lista de rezervari")
            print("modificare,Id,Nume,Clasa,Pret,Checkin_facut - va modifica o rezervare existenta din lista")
            print("stergere,Id - va sterge elementul cu id-ul dat din lista")
            print("showall - va afisa toate elementele din lista curenta")
            print("stop - va opri programul")
        else:
            string = mesaj.split(";")
            if string[0] == "stop":
                break
            else:
                for elemente in string:
                    elementNou = elemente.split(",")
                    if elementNou[0] == "adaugare":
                        try:
                            new_list_1 = adaugaRezervare(int(elementNou[1]), elementNou[2], elementNou[3], float(elementNou[4]), elementNou[5], new_list_1)
                        except ValueError:
                            print("Eroare! Nu ati introdus un numar zecimal pentru pret! Va rugam, incercati!")
                    elif elementNou[0] == "modificare":
                        try:
                            new_list_1 = modificaRezervarea(int(elementNou[1]), elementNou[2], elementNou[3], float(elementNou[4]), elementNou[5], new_list_1 )
                        except ValueError:
                            print("Eroare! Nu ati introdus un numar zecimal pentru pret! Va rugam, incercati!")
                    elif elementNou[0] == "showall":
                            showAll(new_list_1)
                    elif elementNou[0] == "stergere":
                        new_list_1 = stergeRezervare(int(elementNou[1]), new_list_1)
                    else:
                        print("Optiune invalida! Va rugam reincercati!")


listaNoua = []
main_command_line(listaNoua)



