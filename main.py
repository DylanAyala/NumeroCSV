import pymongo
from Conf import conf
import re

myclient = pymongo.MongoClient(conf.DATA_BASE)
mydb = myclient[conf.DB_NAME]
mycol = mydb[conf.COLLECTION]

myquery = conf.MY_QUERY
count = mycol.count(myquery)
x = mycol.find(myquery)
contador = 0
x2 = ""
num = ""
print(count)
f = open("./CSVs/" + conf.NAME_CSV + ".csv", "w")
f.write("Numero" + "\n")
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
    contador += 1
f.close()
