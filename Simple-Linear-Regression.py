# Apply the Simple Linear Regression 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,accuracy_score
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet
data=pd.read_csv('housingData.csv')
data=data.fillna(data.mean())
print(data.head())
#EDA
plt.figure(figsize=(12, 6))
sns.heatmap(data.corr(),cmap = 'BrBG', fmt = '.2f',linewidths = 2,annot = True)
x=data.drop(columns='MEDV')
y=data['MEDV']
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=42)
linear_maodel=LinearRegression()
linear_model.fit(xtrain,ytrain)
predict=linear_model.predict(xtest)
rmse=mean_squared_error(ytest,predict,squared=False)
print(rmse)
#linear Regression
plt.scatter(ytest,lp,color='blue',label='Predict')
plt.plot([min(ytest),max(ytest)],[min(ytest),max(ytest)],color='red',label='Actual')
plt.title("Linear Regression")
plt.xlabel("Actul")
plt.ylabel("Predict")
plt.legend()
plt.show()
