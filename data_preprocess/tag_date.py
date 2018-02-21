import csv
import os
from os import walk


def tag_date(query_path):
    for root, dirs, files in walk(query_path):
        for f in files:
            if f != ".DS_Store":
                print "tagging date in "+ f + " , please wait.."

                with open(query_path+"/"+f, 'rb') as input, open(os.getcwd()+"/date-testing-data/"+f, 'wb') as out:
                    writer = csv.writer(out)
                    for row in csv.reader(input):
                            writer.writerow(row + [f.split(".")[0]])

                print "Done.\n"

def main( ):
    os.chdir("/Users/andy/TbrainGame")
    tag_date(os.getcwd()+"/testing-data")

if __name__ == "__main__":
    main()

