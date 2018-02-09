import csv
import os
import numpy as np
import pandas as pd

from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
from sklearn import preprocessing
from sklearn.metrics import roc_auc_score

# split csv file into to X(column 0~4) and Y(column 4), Y is the attribute what we want to predict
def split_data(filename):
    print "Split data " + filename
    dataframe = pd.read_csv(filename, low_memory=False)
    array = dataframe.values
    X = array[:,0:4]
    Y = array[:,4]
    return X,Y

#transform orig string to int label using LabelEncoder()
def le(data, kind_data):
    le = preprocessing.LabelEncoder()
    le.fit(kind_data)
    return le.transform(data)

#transform data to sklearn input form
def data2sk(X_,y):
    print "Transform data to sklearn input form, wait.."
    user_id = []
    user_time = []
    product_id = []

    [user_id.append(X_[i][1]) for i in range(0, len(X_))]
    [user_time.append(X_[i][2]) for i in range(0, len(X_))]
    [product_id.append(X_[i][3]) for i in range(0, len(X_))]

    # kind_user : eliminate duplicate user_id
    kind_user = list(set(user_id))
    kind_product = list(set(product_id))

    user_id_trans = le(user_id,kind_user)
    product_id_trans = le(product_id, kind_product)

    X_[:, 1] = user_id_trans
    X_[:, 2] = user_time
    X_[:, 3] = product_id_trans
    y=y.astype(np.float)
    return X_,y

def main():
    current_path = os.getcwd()

    X_,y = split_data(current_path+'/training_data/0301.csv')
    X_2,y_2 = split_data(current_path+'/training_data/0302.csv')

    X__,y = data2sk(X_,y)
    X__2,y_2 = data2sk(X_2,y_2)

    X_train = X__[:,1:2]
    y_train = y


    X_test=X__2[:,1:2]
    #y_test=y_2

    print "\nBuilding DecisionTree Classifier ..."
    #regr_1 = DecisionTreeRegressor(max_depth=2)
    regr_1 = tree.DecisionTreeClassifier()
    regr_1.fit(X_train, y_train)

    prediction = regr_1.predict(X_test)
    probs = regr_1.predict_proba(X_test)

    #print prediction
    print probs
    np.savetxt(current_path+"/resutl.csv", probs, delimiter = ',')
    # print "\nStart Calculate the AUC Score..."
    # y_1 = regr_1.predict(X_test)
    # print "AUC Score is " + str(roc_auc_score(y_test, y_1))

if __name__ == '__main__':
    main()



