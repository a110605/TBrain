import csv
import os
from os import walk

testing_set = set()

def build_test_set(file_name):
    f = open(file_name, 'r')
    reader = csv.reader(f)
    for row in reader:
        testing_set.add(row[0])
        #print row[0]
    f.close()


def split_test_train(query_path):
    for root, dirs, files in walk(query_path):
        for f in files:
            if f != ".DS_Store":
                print "Getting training data from "+ f + " ,please wait.."

                with open(query_path+"/"+f, 'rb') as input, open(os.getcwd()+"/training-data/"+f, 'wb') as out:
                    writer = csv.writer(out)
                    for row in csv.reader(input):
                       if row[0] not in testing_set:
                            #print "Write "+ row[0] + " in " + f + " to testing-data.csv"
                            writer.writerow(row)

                print "Done.\n"

def main( ):
    os.chdir("/Users/andy/TbrainGame")

    build_test_set("new-testing-set.csv")
    split_test_train(os.getcwd()+"/query_log")

if __name__ == "__main__":
    main()

