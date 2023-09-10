import pymongo

myclient = pymongo.MongoClient("cluster0.naej2hs.mongodb.net")
mydb = myclient["slenov21"]
mycol = mydb["db_eig.LICUADORA_artefacta"]

datos = mycol.find({"title" : "price"})
print(datos)