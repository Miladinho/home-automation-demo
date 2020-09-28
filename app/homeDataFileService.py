import os
import json

class HomeDataFileService:
    def getComponents(self, fileName):
        data = json.loads(self.readFile(fileName))
        return data
        
    def readFile(self, fileName):
        data = ""
        with open(fileName, "r", encoding = "utf-8") as reader:
            data = reader.read()
        return data

    def writeComponentsToFile(self, components, fileName):
        with open(fileName, "w", encoding = "utf-8") as writer:
            writer.write(json.dumps({"components": list(map(lambda comp: comp.__dict__, components))}))
