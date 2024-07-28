import json

def getJsonData():
    with open("./jasons/items.json", "r") as file:
        data = json.load(file)
        file.close()
        return data