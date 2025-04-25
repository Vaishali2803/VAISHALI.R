SUPPORT VECTOR MACHINE

import pandas as pd
import numpy as np
import sklearn
from sklearn import svm
data=pd.read_csv('C:/Users/QHAMAR/Downloads/iris (1).csv')
X=data.iloc[:,:-1]
y = data.iloc[:,-1]
from sklearn.preprocessing import StandardScaler
scale=StandardScaler()
X=scale.fit_transform(X)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.25)
df=svm.SVC(kernel="rbf")
df.fit(x_train,y_train)
y_pred=df.predict(x_test)
from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test,y_pred)
print("Accuracy of SVM=", accuracy)
