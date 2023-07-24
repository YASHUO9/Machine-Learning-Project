import pandas as pd
import numpy as np 
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import  LogisticRegression
from sklearn.model_selection import train_test_split 
from sklearn.metrics import  confusion_matrix
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt
import seaborn as sns
import os

def cleaning_and_prediction():
    location = os.path.abspath(os.path.dirname(__file__)) + "//Output.csv"
    df  = pd.read_csv(location)
    df.drop(columns=(['Unnamed: 0']),inplace = True)
    remove_index= []
    for i in range(0,42717):
        try:
            int(df[['# Columns: time'][0]][i])
        except:
            remove_index.append(i)

    # df.drop(index = remove_index,inplace = True)
    for i in remove_index:
        try:
           df.drop( df.index[i],inplace = True)
        except:
            pass
    # df.index[i]
    df.reset_index(drop=True, inplace=True)
    ProfileReport(df)
    df.drop_duplicates(inplace = True)
    df['# Columns: time'] = df['# Columns: time'].astype(str)





    q = df['avg_rss23'].quantile(.60) # taking the (98%) data set
    df_new = df[df['avg_rss23']<q]
    q = df['avg_rss13'].quantile(.70) # taking the (98%) data set
    df_new = df[df['avg_rss13']<q]
    q = df['var_rss12'].quantile(.66) # taking the (98%) data set
    df_new = df[df['var_rss12']<q]
    q = df['var_rss13'].quantile(.76) # taking the (98%) data set
    df_new = df[df['var_rss13']<q]
    q = df['avg_rss13'].quantile(.76) # taking the (98%) data set
    df_new = df[df['avg_rss13']<q]
    q = df['avg_rss12'].quantile(.75) # taking the (98%) data set
    df_new = df[df['avg_rss12']<q]

    fig , ax = plt.subplots(figsize = (20,20))
    sns.boxplot(data= df_new , ax = ax)






    y =  df_new['label']

    X = df_new.drop(columns  = ['label'])



    scaler = StandardScaler()
    profile = ProfileReport(pd.DataFrame(scaler.fit_transform(X)))
    # basedir = "index2.html"
    # profile.to_html(basedir)
    basedir = os.path.abspath(os.path.dirname(__file__)) + "\\templates\\index2.html"
    profile.to_file (basedir)


    df_new_scalar = pd.DataFrame(scaler.fit_transform(X))
    fig , ax = plt.subplots(figsize = (20,20))
    sns.boxplot(data= df_new_scalar ,ax = ax)





    X_scale = scaler.fit_transform(X)
    x_train, x_test, y_train , y_test = train_test_split(X_scale , y , test_size = .20 ,  random_state =144)

    logr_liblinear1 = LogisticRegression(verbose =1 , solver = 'newton-cg')
    logr_liblinear2 = LogisticRegression(verbose =1 , solver = 'saga')
    logr_liblinear3 = LogisticRegression(verbose =1 , solver = 'sag')


    logr_liblinear1.fit(x_train,y_train)
    logr_liblinear2.fit(x_train,y_train)
    logr_liblinear3.fit(x_train,y_train)


    y_predict1 = logr_liblinear1.predict(x_test)
    y_predict2 = logr_liblinear2.predict(x_test)
    y_predict3 = logr_liblinear3.predict(x_test)

    if y_test.iloc[0] ==logr_liblinear1.predict([x_test[0]]):
        print("Prediction is right! using newton-cg")
    if y_test.iloc[0] ==logr_liblinear2.predict([x_test[0]]):
        print("Prediction is right! using saga")
    if y_test.iloc[0] ==logr_liblinear3.predict([x_test[0]]):
        print("Prediction is right! using sag")

        
    confusion_matrix(y_test , y_predict1)   
    confusion_matrix(y_test , y_predict2)
    confusion_matrix(y_test , y_predict3)

