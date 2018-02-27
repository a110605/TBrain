import csv
import os
from os import walk

user_id = set()
product_id = set()

def build_known_set(query_dir):
    i = 1
    for root, dirs, files in walk(query_dir):
        for f in files:
            print "Processing training data " + f + " , please wait...  " + str(i) + "/66"
            i = i + 1
            if f != ".DS_Store":
                with open(query_dir+"/"+f, 'rb') as input:
                    for row in csv.reader(input):
                        product_id.add(row[3])
                        user_id.add(row[1])

def delete_unknown_test_data(query_path):
    i = 1
    for root, dirs, files in walk(query_path):
        for f in files:
            if f != ".DS_Store":
                print "Processing testing data " + f + " , please wait...  " +  str(i)
                i = i + 1
                #print f
                with open(query_path + "/" + f, 'rb') as input, open(os.getcwd() + "/testing-data-delete-unknown/" + f,'wb') as out:
                        writer = csv.writer(out)
                        for row in csv.reader(input):
                            if row[1] in user_id and row[3] in product_id:
                                writer.writerow(row)


                        #         # print "Write "+ row[0] + " in " + f + " to testing-data.csv"
                        #         writer.writerow(row)
                        #  if row[0] in user_id :
                    #         str_row = ','.join(map(str,row))
                    #         if testing_dict[row[0]] == "": # first append
                    #             value = str_row
                    #         else:
                    #             value = testing_dict[row[0]] + "\n" + str_row
                    #         #print value
                    #         testing_dict[row[0]] = value
                    #print "Done.\n"

def print_set():
    print "product_id set size = "+ str(len(product_id))
    print "user_id set size = " + str(len(user_id))

def main():
    os.chdir("/Users/andy/TbrainGame")
    build_known_set(os.getcwd()+"/training-data/")
    print_set()
    delete_unknown_test_data(os.getcwd()+"/testing-data-fileid")

    #split_fileid(os.getcwd()+"/training-data")
    #save_to_file()

if __name__ == "__main__":
    main()

