#Importazione librerie
import csv
import datetime
from termcolor import colored
from faker import Faker
fake = Faker()
from random import randint
from generator import generaPSW

#Funzione di salvataggio
def file1():
    def savecsvFile(fileName, mod, header, data):
        with open(fileName, mod) as file:
            for value in header:
                file.write(str(value)+', ')
            file.write('\n')
            for row in data:
                for x in row:
                    file.write(str(row[x])+', ')
                file.write('\n')

    #definizione struct
    saldoConti = {
        "header": ["idConto", "Saldo", "timestamp"],
        "rows": []
    }

    listaMovimenti = {
        "header": ["idConto", "importo", "timestamp"],
        "rows": []
    }

    anagrafica = {
        "header": ["Nome", "Cognome", "idConto"],
        "rows": []  
    }

    #Generazione dati struct
    for i in range(0, 10):
        row = {
            "Nome": fake.name().split(" ")[0],
            "Cognome": fake.name().split(" ")[1],
            "idConto": i
        }
        anagrafica["rows"].append(row)

    for i in range(0, 10):
        row = {
            "idConto": randint(0, 10),
            "importo": randint(-150, 150),
            "timestamp": fake.date(),
        }
        listaMovimenti["rows"].append(row)

    for i in range(0, 10):
        row = {
            "idConto": i,
            "saldo": randint(2000, 8000),
            "timestamp": fake.date()
        }
        saldoConti["rows"].append(row)

    #Salvataggio dei file
    savecsvFile('./database/saldoConti.csv', "w", saldoConti["header"], saldoConti["rows"])
    savecsvFile('./database/listaMovimenti.csv', "w", listaMovimenti["header"], listaMovimenti["rows"])
    savecsvFile('./database/anagrafica.csv', "w", anagrafica["header"], anagrafica["rows"])

# file 2
def file2():
    #Definizione funzioni
    def readcsvFile(fileName):
        rows = []
        with open(fileName, "r") as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            header.pop(3)
            #print(header)
            for row in csvreader:
                row.pop(3)
                rows.append(row)
                #print(row[1])
        

        return {
            "header": header,
            "rows": rows
        }

    #Lettura dei file csv di DataBase
    anagrafica = readcsvFile("./database/anagrafica.csv")
    saldoConti = readcsvFile("./database/saldoConti.csv")
    listaMovimenti = readcsvFile("./database/listaMovimenti.csv")

    #Applicativo
    comando = 0
    while comando != 4:
        print("Seleziona un comando:")
        print("    1. Stampa lista conti")
        print("    2. Stampa saldo conto")
        print("    3. Stampa lista movimenti per conto")
        print("    4. Torna INDIETRO")

        comando = int(input("inserisci qui il tuo comando: "))
        print()

        if comando == 1:
            print("\nLista conti correnti")
            print(anagrafica["header"])
            for row in anagrafica["rows"]:
                print("		-> ", row)
            print()
        elif comando == 2:
            saldo = None
            idConto = int(input("Inserisci qui ID del conto ricercato: "))
            for row in saldoConti["rows"]:
                if int(row[0]) == idConto:
                    saldo = row[1]
                    break
                pwd = input("Inserisci la password del conto: ")
                for row in anagrafica["rows"]:
                    if row[3] == pwd:
                        print()
                        print(colored("Il saldo del conto {} ammonta a{} euro.".format(idConto, saldo), "green"))
                        print()
                    elif comando == 3:
                        idConto = int(input("Inserisci qui ID del conto ricercato: "))
                        print()
                        print("Lista movimenti del conto", idConto)
                        esisteM = False
                        for row in listaMovimenti["rows"]:
                            if int(row[0]) == idConto:
                                esisteM = True
                                print("		->", row)
                        if esisteM == False:
                            print(colored("Non ci sono movimenti per questo conto corrente!", "red"))
                        print()
                    elif comando == 4:
                        done = True
                    else:
                        print()
                        print("COMANDO INSESISTENTE!!!")
                        print()

# file 3
def file3():
    #DEFINIZIONE FUNZIONI
    def readcsvFile(fileName):
        rows = []
        with open(fileName, "r") as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            header.pop(3)
            #print(header)
            for row in csvreader:
                row.pop(3)
                rows.append(row)
                #print(row[1])
        

        return {
            "header": header,
            "rows": rows
        }

    def savecsvFile(fileName, mod, header, data):
        with open(fileName, mod) as file:
            for value in header:
                file.write(str(value)+', ')
            file.write('\n')
            for row in data:
                for x in row:
                    file.write(str(row[x])+', ')
                file.write('\n')

    def updatecsvFile(fileName, mod, data):
        with open(fileName, mod) as file:
            for row in data:
                for x in row:
                    file.write(str(x)+', ')
                file.write('\n')

    #Lettura dei file csv di DataBase
    anagrafica = readcsvFile("./database/anagrafica.csv")
    saldoConti = readcsvFile("./database/saldoConti.csv")
    listaMovimenti = readcsvFile("./database/listaMovimenti.csv")
    lastID = int(anagrafica["rows"][-1][2])
    #PROGRAMMA
    print()
    print("INSERISCI UN NUOVO CONTO")
    print()
    #Input valori
    newID = lastID + 1 
    nome = input("Inserire il NOME del correntista: ")
    cognome = input("Inserire il COGNOME del correntista: ")
    deposito = int(input("Somma da depositare inizialmente sul conto: "))
    
    timestamp = datetime.date.today()
    #Aggiornamento DB
    updatecsvFile("./database/anagrafica.csv", "a", [[nome, cognome, newID]])
    updatecsvFile("./database/saldoConti.csv", "a", [[newID, deposito, timestamp]])
    updatecsvFile("./database/listaMovimenti.csv", "a", [[newID, ("+"+str(deposito)), timestamp]])

#file 4
#Importazione librerie

def file4():
    #DEFINIZIONE FUNZIONI - lettura e scrittura
    def readcsvFile(fileName):
        rows = []
        with open(fileName, "r") as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            header.pop(3)
            #print(header)
            for row in csvreader:
                row.pop(3)
                rows.append(row)
                #print(row[1])
        

        return {
            "header": header,
            "rows": rows
        }

    def savecsvFile(fileName, mod, header, data):
        with open(fileName, mod) as file:
            for value in header:
                file.write(str(value)+', ')
            file.write('\n')
            for row in data:
                for x in row:
                    file.write(str(x)+', ')
                file.write('\n')

    def updatecsvFile(fileName, mod, data):
        with open(fileName, mod) as file:
            for row in data:
                for x in row:
                    file.write(str(x)+', ')
                file.write('\n')

    #Lettura dei file csv di DataBase
    anagrafica = readcsvFile("./database/anagrafica.csv")
    saldoConti = readcsvFile("./database/saldoConti.csv")
    listaMovimenti = readcsvFile("./database/listaMovimenti.csv")
    lastID = int(anagrafica["rows"][-1][2])

    #Definizione funzioni principali
    def prelievo(idConto, importo, saldoConti=saldoConti, listaMovimenti=listaMovimenti):
        for conto in saldoConti["rows"]:
            if int(conto[0]) == idConto:
                print("Effettuo un prelievo")
                conto[1] = int(conto[1])
                if conto[1]>importo:
                    conto[1] -= importo
                    listaMovimenti["rows"].append([idConto, "-"+str(importo), str(datetime.date.today())])
                    savecsvFile("./database/saldoConti.csv", "w", saldoConti["header"], saldoConti["rows"])
                    updatecsvFile("./database/listaMovimenti.csv", "a", [listaMovimenti["rows"][-1]])
                    return True
                else:
                    print(colored("Importo inserito maggiore del saldo: inserire un importo valido", "red"))
                    return False
        return False
                
        print(colored("Impossibile effettuare il prelievo!", "red"))
        return False
    def versamento(idConto, importo, saldoConti=saldoConti, listaMovimenti=listaMovimenti):
        for conto in saldoConti["rows"]:
            if int(conto[0]) == idConto:
                timestamp = datetime.date.today()
                conto[1] = int(conto[1])
                conto[1] += importo
                conto[2] = str(timestamp)
                listaMovimenti["rows"].append([idConto, "+"+str(importo), str(datetime.date.today())])
                savecsvFile("./database/saldoConti.csv", "w", saldoConti["header"], saldoConti["rows"])
                updatecsvFile("./database/listaMovimenti.csv", "a", [listaMovimenti["rows"][-1]])
                return True	
        return False
        

    #prelievo(10, 80000)
    #versamento(10, 1100)

    #Applicativo
    comando = 0
    print()
    print("BENVENUTO NEL SOFTWARE DI GESTIONE CONTI")
    print()
    while comando != 3:
        print()
        print("Seleziona un comando:")
        print("    1. Effettua un versamento")
        print("    2. Effettua un prelievo")
        print("    3. ESCI e chiudi il programma")

        comando = int(input("Inserisci qui il tuo comando: "))
        print()

        if comando == 1:
            idConto = int(input("Inserisci ID del conto: "))
            importo = int(input("Inserisci l'importo da versare: "))
            if versamento(idConto, importo) == True:
                print(colored("Versamento effettuato con successo", "green"))
            else:
                print(colored("ERRORE nell'operazione, ritentare", "red"))
        elif comando == 2:
            idConto = int(input("Inserisci ID del conto: "))
            importo = int(input("Inserisci l'importo da prelevare: "))
            if prelievo(idConto, importo) == True:
                print(colored("Prelievo effettuato con successo!", "green"))
            else:
                print(colored("ERRORE nell'operazione, ritentare", "red"))
        elif comando == 3:
            done = True
        else:
            print()
            print(colored("COMANDO INSESISTENTE!!!", "yellow"))
            print()

def menuInterazione():
    comando = 0
    print()
    print("BENVENUTO NEL SOFTWARE DI SMART BANKING")
    print()
    while comando != 5:
        print("Seleziona un comando:")
        print("    1. Genera DB correntisti")
        print("    2. Visualizza informazioni relative i conti")
        print("    3. Crea un nuovo conto")
        print("    4. Crea un nuovo movimento")
        print("    5. ESCI e chiudi il programma")

        comando = int(input("inserisci qui il tuo comando: "))
        print()
        if comando == 1:
            file1()
        elif comando == 2:
            file2()
        elif comando == 3:
            file3()
        elif comando == 4:
            file4()
        elif comando==5:
            done = True
        else:
            print()
            print(colored("COMANDO INSESISTENTE!!!", "yellow"))
            print()


menuInterazione()