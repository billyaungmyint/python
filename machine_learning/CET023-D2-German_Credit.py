import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import linear_model
from sklearn import tree
from sklearn import ensemble
from sklearn import neural_network
from sklearn.feature_selection import SelectKBest,f_regression
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV

# continuous - rmse
# categorical - accuracy

df = pd.read_csv(r'D:\Google Drive\Colab Notebooks\german_credit.csv')
print(df.keys())

# y is Credibility
X = df.drop(columns = 'Creditability')
Y = df['Creditability']

# Choose best features for regression
f = SelectKBest(score_func=f_regression,k=10).fit(X,Y)
f = f.get_support()
print(f)
print(X.columns[f])

# get the column names from X.columns[f]) and select only those columns in df
df = df.loc[:,['Creditability','Account Balance', 'Duration of Credit Mths',
       'Payment Status of Previous Credit', 'Credit Amount',
       'Value of Savings and Stocks', 'Length of current employment',
       'Sex and Marital Status', 'Most valuable available asset', 'Age',
       'Concurrent Credits']]

df['Sex and Marital Status'].value_counts()
# https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html
d = pd.get_dummies(df["Sex and Marital Status"])
df = df.merge(d,left_index=True,right_index=True)
print(df)
df = df.drop(columns = 'Sex and Marital Status')

# data visualisation
print(df.describe())  # usually to check the mean if normalisation is required

df.boxplot(figsize=(30,20))
df.hist(figsize=(20,20))

# seaborn string for categorical
sns.heatmap(df.corr())
sns.catplot(data = df , x = 'Account Balance' , y = 'Creditability', kind = 'violin')

# matplotlib strong for continuous
plt.scatter(df.Creditability, df["Credit Amount"])
plt.title('Creditability vs Credit Amount')

X = df.drop(columns = 'Creditability')
Y = df['Creditability']

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=511)

# to check if data is balanced
print(df['Creditability'].value_counts())
print(Y_train.value_counts())

# https://machinelearningmastery.com/smote-oversampling-for-imbalanced-classification/
X_train , Y_train = SMOTE(random_state=511).fit_resample(X_train,Y_train)

# normalize the credit amount
# df.describe() - see the mean value of credit amount here
X_train['Credit Amount'] = stats.zscore(X_train['Credit Amount'])
X_test['Credit Amount'] = stats.zscore(X_test['Credit Amount'])
print(X_train) # see the credit amount

# logistic regression
model = linear_model.LogisticRegression(max_iter = 500 ,random_state=511)
model.fit(X_train,Y_train)
pred = model.predict(X_test)
cm = confusion_matrix(Y_test,pred)
print(cm)
print('accuracy is ',(cm[0,0] + cm[1,1])/(sum(sum(cm))))

# tree
# min_sample_split value comes from optimisation below - originally just the random_state
model = tree.DecisionTreeClassifier(min_samples_split=86,random_state=511)
model.fit(X_train,Y_train)
pred = model.predict(X_test)
cm = confusion_matrix(Y_test,pred)
print(cm)
print('accuracy is ',(cm[0,0] + cm[1,1])/(sum(sum(cm))))

# ensemble learning - randomforest
# max_depth value comes from optimisation below - originally just the random_state
model = ensemble.RandomForestClassifier(max_depth=15,random_state=511)
model.fit(X_train,Y_train)
pred = model.predict(X_test)
cm = confusion_matrix(Y_test,pred)
print(cm)
print('accuracy is ',(cm[0,0] + cm[1,1])/(sum(sum(cm))))

# Feature Ranking
imp = list(zip(model.feature_importances_,X.columns))
imp.sort(reverse=True)
print(imp)

# Boosting!!!
model = ensemble.GradientBoostingClassifier(random_state=511)
model.fit(X_train,Y_train)
pred = model.predict(X_test)
cm = confusion_matrix(Y_test,pred)
print(cm)
print('accuracy is ',(cm[0,0] + cm[1,1])/(sum(sum(cm))))

#Neural Network
# https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
model = neural_network.MLPClassifier(random_state=511)
model.fit(X_train,Y_train)
pred = model.predict(X_test)
cm = confusion_matrix(Y_test,pred)
print(cm)
print('accuracy is ',(cm[0,0] + cm[1,1])/(sum(sum(cm))))

# check if overfitting
pred = model.predict(X_train)
cm = confusion_matrix(Y_train,pred)
print(cm)
print('accuracy is ',(cm[0,0] + cm[1,1])/(sum(sum(cm))))

# Optimisation -- all the models with overfitting
# using max_depth
model = tree.DecisionTreeClassifier()
grid = GridSearchCV(estimator=model , param_grid = dict(max_depth=[i for i in range(1,20)]),cv = 10)
grid = grid.fit(X_train , Y_train)
print(grid.best_params_)
print(grid.best_score_)

model = tree.DecisionTreeClassifier()
grid = GridSearchCV(estimator=model , param_grid = dict(min_samples_split=[i for i in range(3,300)]),cv = 5)
grid = grid.fit(X_train , Y_train)
print(grid.best_params_)
print(grid.best_score_)

model = ensemble.RandomForestClassifier()
grid = GridSearchCV(estimator=model , param_grid = dict(min_samples_split=[i for i in range(3,300)]),cv = 5)
grid = grid.fit(X_train , Y_train)
print(grid.best_params_)

model = ensemble.RandomForestClassifier()
grid = GridSearchCV(estimator=model , param_grid = dict(max_depth=[i for i in range(2,20)]),cv = 5)
grid = grid.fit(X_train , Y_train)
print(grid.best_params_)