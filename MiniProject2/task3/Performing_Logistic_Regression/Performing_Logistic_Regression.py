# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 12:57:28 2020

@author: ninjaac
"""


from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_data=pd.read_csv(r'F:\internship2020_kaggle\week2\task1\Data_Exploration_and_Cleaning\cleaned_data.csv').set_index('ID')


# drop any null values
#df[.replace('NaN',0)]
df_data.dropna(how='any',axis=0)
print(df_data.columns)
df1=df_data.drop(['EDUCATION_CAT','EDUCATION'],axis=1)
print(df1.shape)
df1 =df1[~df1.isin([np.nan, np.inf, -np.inf]).any(1)]
print(df1.shape)

# standadize the values
from sklearn.preprocessing import StandardScaler
scale=StandardScaler()



X=df1.drop(['default payment next month'],axis=1)
X_scale=scale.fit_transform(X)
y=df1['default payment next month'].copy()
X_train,X_test,y_train,y_test=train_test_split(X_scale,y,test_size=0.2,random_state=42)

#print(X_train,y_train)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
log=LogisticRegression()
log.fit(X_train,y_train)
predict_y_test=log.predict(X_test)
print(predict_y_test)
print(accuracy_score(y_test,predict_y_test))

#confussion matrix
from sklearn.metrics import confusion_matrix
con=confusion_matrix(y_test,predict_y_test)
print(con)




predict_prob_y_test = log.decision_function(X_test)
# keep probabilities for the positive outcome only (or) both can be used same resukts
#predict_prob_y_test = log.predict_proba(X_test)
#predict_prob_y_test =predict_prob_y_test[:, 1]


#data for the roc curve
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
false_positive_rate,true_positive_rate,threshold=roc_curve(y_test,predict_prob_y_test)
#plot the roc-auc curve
plt.plot(false_positive_rate,true_positive_rate)
plt.plot([0,1],[0,1])
plt.xlabel('Flase positive rate')
plt.ylabel('True pasitive rate')
plt.xlim(0.0,1.0)
plt.ylim(0.0,1.05)
plt.title('ROC_AUC curve using limit_bal')
plt.show()
auc_roc_score=roc_auc_score(y_test,predict_prob_y_test)

#comaprision
df2=df_data.drop(['EDUCATION_CAT','LIMIT_BAL'],axis=1)

df2 =df2[~df2.isin([np.nan, np.inf, -np.inf]).any(1)]


# standadize the values
from sklearn.preprocessing import StandardScaler
scale2=StandardScaler()



X2=df2.drop(['default payment next month'],axis=1)
X2_scale=scale2.fit_transform(X2)
y2=df2['default payment next month'].copy()
X2_train,X2_test,y2_train,y2_test=train_test_split(X2_scale,y2,test_size=0.2,random_state=42)

#print(X_train,y_train)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

log2=LogisticRegression()
log2.fit(X2_train,y2_train)
predict_y2_test=log2.predict(X2_test)
print(predict_y2_test)
print(accuracy_score(y2_test,predict_y2_test))

#confussion matrix
from sklearn.metrics import confusion_matrix
con2=confusion_matrix(y2_test,predict_y2_test)
print(con2)

predict_prob_y2_test = log2.decision_function(X2_test)
false2_positive_rate,true2_positive_rate,threshold=roc_curve(y2_test,predict_prob_y2_test)
#plot the roc-auc curve
plt.plot(false2_positive_rate,true2_positive_rate)
plt.plot([0,1],[0,1])
plt.xlabel('Flase positive rate')
plt.ylabel('True pasitive rate')
plt.xlim(0.0,1.0)
plt.ylim(0.0,1.05)
plt.title('ROC_AUC curve using education')
plt.show()
auc_roc_score2=roc_auc_score(y2_test,predict_prob_y2_test)

#data for the precision-recall curve
from sklearn.metrics import precision_recall_curve
presicion,recall,threshold = precision_recall_curve(y_test,predict_prob_y_test )

#pot the precision-recall curve
# when i am using the xlim and ylim value to 0-1 i can get the area under the curve perfectly
# other wise it will be the curve that may not giving the correct results
plt.plot(recall,presicion)
plt.xlabel('recall')
plt.ylabel('Precision')
plt.xlim(0.0,1.0)
plt.ylim(0.0,1.0)
plt.title('Precision-recall curve')
plt.show()

#area under the curve 
from sklearn.metrics import average_precision_score #area under the curve
area_under_curve=average_precision_score(y_test,predict_prob_y_test)

#ROC_AUC curve for the training data
predic_y_train=log.predict(X_train)
accuracy_score(y_train,predic_y_train)
predict_prob_y_train = log.decision_function(X_train)
fpr,tpr,threshold=roc_curve(y_train,predict_prob_y_train )

#plot the roc-auc curve for trainig
plt.plot(fpr,tpr)
plt.plot([0,1],[0,1])
plt.xlabel('Flase positive rate')
plt.ylabel('True pasitive rate')
plt.xlim(0.0,1.0)
plt.ylim(0.0,1.05)
plt.title('ROC_AUC curve for training data')
plt.show()
auc_roc_score_trainig=roc_auc_score(y_train,predict_prob_y_train)













