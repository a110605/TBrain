import csv
import os
from os import walk

# global variables
training_set = "training-set.csv"
#training_data = "0301.csv"
training_dir = "/training_data/"
new_training_dir = "/new_training_data/"
malware = set() # from line 1 to 5647 is malware (1), otherwise is not (0)


def build_malware_set(file_name):
    f = open(file_name, 'r')
    reader = csv.reader(f)
    i = 0
    for row in reader:
        malware.add(row[0])
        i += 1
        if i == 5647:
            break
    f.close()


def tag_the_malware(filename, new_filename):
    print "Processing " + filename + " to " + new_filename + ", please wait..."

    file = open (filename, 'r')
    reader = csv.reader(file)

    output = open(new_filename, 'w')
    writer = csv.writer(output)

    for row in reader:
        if row[0] in malware:
            writer.writerow(row + [1])
        else:
            writer.writerow(row + [0])
    file.close()
    output.close()
    print "Done.\n"


def main( ):
    mypath = os.getcwd() + training_dir # /root/training_data/
    newpath = os.getcwd() + new_training_dir # /root/new_training_data/

    build_malware_set(training_set)

    for root, dirs, files in walk(mypath):
        for f in files:
            print f
            if f != ".DS_Store":
                mypathfile = mypath + f
                newpathfile = newpath + f
                print mypathfile +"\n"+ newpathfile
                #tag_the_malware(mypathfile, newpathfile)


if __name__ == "__main__":
    main()

