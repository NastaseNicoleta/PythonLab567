def creeaza_rezervare(id, nume, clasa, pret :float, checkin_facut):
    '''
    creeaza un dictionar pentru o rezervare facuta la o companie aeriana
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin_facut: string
    :return: o lista

    '''
    rezervare = []
    rezervare.append(id)
    rezervare.append(nume)
    rezervare.append(clasa)
    rezervare.append(pret)
    rezervare.append(checkin_facut)
    return rezervare



def getId(rezervare):
    '''
    ia id-ul unei rezervari
    :param rezervare: un dictionar ce retine o rezervare
    :return: id-ul rezervarii
    '''
    return rezervare[0]

def getNume(rezervare):
    '''
    ia numele folosit pentru o rezervare
    :param rezervare: un dictionare ce retine o rezervare
    :return: numele folosit pentru rezervare
    '''
    return rezervare[1]

def getClasa(rezervare):
    '''
    ia clasa unei rezervari
    :param rezervare: un dictionar ce retine o rezervare
    :return: clasa rezervarii
    '''
    return rezervare[2]

def getPret(rezervare):
    '''
    ia pretul unei rezervari
    :param rezervare: un dictionar ce retine o rezervare
    :return: pretul rezervarii
    '''
    return rezervare[3]
def getCheckin_facut(rezervare):
    '''
    ia stadiul checkin-ului unei rezervari
    :param rezervare: un dictionar ce retine o rezervare
    :return: stadiul checkin-unului rezervarii
    '''
    return rezervare[4]

def toString(rezervare):
    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin_facut: {}".format(
        getId(rezervare),
        getNume(rezervare),
        getClasa(rezervare),
        getPret(rezervare),
        getCheckin_facut(rezervare)
    )
