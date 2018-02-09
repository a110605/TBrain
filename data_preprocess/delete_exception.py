import csv
import os

exception_train = "/exception_testing.txt"
exception = set() # from line 1 to 5647 is malware (1), otherwise is not (0)

def build_exception_set(file_name):
    with open(file_name, "r") as file:
        for line in file:
            line = line.rstrip("\n")
            exception.add(line)

def delete_exception(filename):
    with open(filename, 'rb') as input, open("new-"+filename, 'wb') as out:
        writer = csv.writer(out)
        for row in csv.reader(input):
            if row[0] not in exception:
                writer.writerow(row)

def main( ):
    os.chdir("/Users/andy/TbrainGame")
    build_exception_set(os.getcwd()+exception_train)
    delete_exception("testing-set.csv")

if __name__ == "__main__":
    main()