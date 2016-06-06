import json

def readfile(file):
    try:
        with open(file,'r') as jsonfile:
            file = json.load(jsonfile)
            process(file)

    except FileNotFoundError as e:
        print(e)


def process(file):
    for key in file.keys():
        print(key.items())
        process(key)


if __name__ == "__main__":
    readfile("web.json")
