import json
import os

class FileFactory:
    #path: path to serialize array of product
    #arrData: array of Product
    def writeData(self,path,arrData):
        jsonString = json.dumps([item.__dict__ for item in arrData],default=str,ensure_ascii=False)
        jsonFile = open(path, "w", encoding='utf-8')
        jsonFile.write(jsonString)
        jsonFile.close()
    #path: path to deserialize array of Product
    #ClassName: Product
    def readData(self,path,ClassName):
        if os.path.isfile(path) == False:
            return []
        file = open(path, "r", encoding='utf-8')
        # Reading from file
        self.arrData = json.loads(file.read(), object_hook=lambda d: ClassName(**d))
        file.close()
        return self.arrData