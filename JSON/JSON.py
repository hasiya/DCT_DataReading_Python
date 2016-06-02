import json

def readfile(file):
    try:
        with open(file,'r') as jsonfile:
            file = json.load(jsonfile)
            print()

    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    readfile("web.json")
