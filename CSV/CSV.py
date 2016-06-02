import csv

def readFile(file,feildNames):
    try:
        with open(file,'r') as C_file:

            if(feildNames == 'Y'):
                reader = csv.DictReader(C_file)
                headers = reader.fieldnames
                for line in reader:
                    for h in headers:
                        print(h, ":",line[h])
                    print()
            else:
                reader = csv.reader(C_file)
                for line in reader:
                    for d in line:
                        print(d)
                    print()


    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":

    fileName = input("Please type the File Name: ")
    fieldNames = input("Feild Names? (Y/N)")
    readFile(fileName,fieldNames)