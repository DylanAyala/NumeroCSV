import pymongo
from Conf import conf
import re
import csv
import os.path as path
import mysql.connector
from threading import Thread

myclient = pymongo.MongoClient(conf.DATA_BASE)
mydb = myclient[conf.DB_NAME]
mycol = mydb[conf.COLLECTION]

mydb = mysql.connector.connect(
    host="192.168.33.80",
    user="soporte",
    passwd="Soporte.3135",
    database='fijos'
)


def fijos(filtros, vuelta):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Telefono FROM todopais WHERE " + filtros)
    myresult = mycursor.fetchall()
    if vuelta == 0:
        f = open("./CSVs/" + conf.NAME_CSV_FIJOS + ".csv", "w")
        f.write("Numero" + "\n")
    else:
        f = open("./CSVs/" + conf.NAME_CSV_FIJOS + ".csv", "a")
    for x1 in myresult:
        x1 = str(x1)
        x1 = x1.replace("(", "")
        x1 = x1.replace(")", "")
        x1 = x1.replace(",", "")
        f.write(x1 + "\n")
    # print(x1)
    f.close()


def celulares(filtros, vuelta):
    if filtros == "":
        myquery = conf.MY_QUERY
        count = mycol.count(myquery)
        x = mycol.find(myquery)
    else:
        # myquery = conf.MY_QUERY
        count = mycol.count(filtros)
        x = mycol.find(filtros)
    x2 = ""
    num = ""
    print(count)
    if vuelta == 0:
        f = open("./CSVs/" + conf.NAME_CSV_CELULARES + ".csv", "w")
        f.write("Numero" + "\n")
    else:
        f = open("./CSVs/" + conf.NAME_CSV_CELULARES + ".csv", "a")
    for x1 in x:

        # Numeros que empiezan con 11
        patron1 = re.compile('^11')
        # Itero lo numeros
        match = patron1.match(x1['numero'])
        if match == None:
            x2 = str(x1["numero"])
            num = x2[0:3] + "15" + x2[3:12]
        else:
            x2 = str(x1["numero"])
            num = x2[0:2] + "15" + x2[2:12]

        f.write(num + "\n")
    f.close()


def NumerosCeluares():
    filtros = ""
    vuelta = 0
    if path.exists('./CSVConFiltros/test1.csv'):
        with open('./CSVConFiltros/test1.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                filtros = {"provincia": "SANTA FE", "$or": [{"localidad": row[0]}, {"localidad": row[0].upper()}]}
                print(filtros)
                celulares(filtros, vuelta)
                vuelta += 1
    else:
        celulares(filtros, vuelta)


def NumerosFijos():
    filtros = ""
    vuelta = 0
    if path.exists('./CSVConFiltros/test1.csv'):
        with open('./CSVConFiltros/test1.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                filtros = "Provincia = 'Santa Fe' AND (Localidad = '" + row[0] + "' OR Localidad = '" + row[
                    0].upper() + "')"
                print(filtros)
                fijos(filtros, vuelta)
                vuelta += 1


t = Thread(target=NumerosFijos)
t2 = Thread(target=NumerosCeluares)
t.start()
t2.start()
