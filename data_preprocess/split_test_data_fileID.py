import csv
import os
from os import walk

testing_dict = {}

def build_test_set(file_name):
    f = open(file_name, 'r')
    reader = csv.reader(f)
    for row in reader:
        testing_dict[row[0]] = ""
    f.close()

def split_fileid(query_path):
    for root, dirs, files in walk(query_path):
        for f in files:
            if f != ".DS_Store":
                print "Processing " + f + " , please wait.."
                with open(query_path+"/"+f, 'rb') as input:
                    for row in csv.reader(input):
                        if row[0] in testing_dict:
                            str_row = ','.join(map(str,row))
                            if testing_dict[row[0]] == "": # first append
                                value = str_row
                            else:
                                value = testing_dict[row[0]] + "\n" + str_row
                            #print value
                            testing_dict[row[0]] = value
    print "Done.\n"

def save_to_file():
    # debug use
    for i in testing_dict:
        if testing_dict[i] != "":
            print i + " of " + testing_dict[i]

    print "Saving testing_dict to file..."
    for key in testing_dict:
        if testing_dict[key] != "":
            file = open(os.getcwd() + "/testing-data-fileid/" + key + ".csv", "wb")
            file.write(testing_dict[key])
            file.close()
    print "Done."

def main():
    os.chdir("/Users/andy/TbrainGame")
    build_test_set("new-testing-set.csv")
    split_fileid(os.getcwd()+"/test-testing-data")
    save_to_file()

if __name__ == "__main__":
    main()

