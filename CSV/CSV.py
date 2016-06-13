import csv
import simplejson as json

def readFile(file,feildNames):
    try:
        with open(file,'r') as C_file:

            if(feildNames == 'Y'):
                reader = csv.DictReader(C_file)
                headers = reader.fieldnames
                Data_dict = []
                for line in reader:
                    line_as_dict = {}
                    for h in headers:
                        line_as_dict[h]=line[h]
                        # print(h, ":",line[h])
                    Data_dict.append(line_as_dict)
                    # print()
                dataJson = json.dumps(Data_dict)
                print(Data_dict)
            else:
                reader = csv.reader(C_file)
                for line in reader:
                    for d in line:
                        print(d)
                    print()


    except IOError as e:
        print(e)

if __name__ == "__main__":

    fileName = input("Please type the File Name: ")
    fieldNames = input("Feild Names? (Y/N)")
    readFile(fileName,fieldNames)