#!C:/Python36/python.exe

import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn import metrics
from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split

import cgi

form = cgi.FieldStorage()

a = form.getvalue('a1')
b = form.getvalue('a2')
c = form.getvalue('a3')
d = form.getvalue('a4')
e = form.getvalue('a5')
f = form.getvalue('a6')
g = form.getvalue('a7')


##a = 78
##b = 88
##c = 2
##d = 76
##e = 567
##f = 767
##g = 456

dataset = pd.read_excel('data/train.xlsx')
dataset.head()

dataset.tail()

dataset.columns.values

def featureSelection():
    features = []
    target = []
    
    for per_10, per_12, clgTier, colgGpa, eng, log, quant, salary in zip(dataset['10percentage'],
                                                                               dataset['12percentage'],
                                                                               dataset['CollegeTier'],
                                                                               dataset['collegeGPA'],
                                                                               dataset['English'],
                                                                               dataset['Logical'],
                                                                               dataset['Quant'],
                                                                               dataset['Salary']):
        features.append([per_10, per_12, clgTier, colgGpa, eng, log, quant])
        target.append(salary)
        
    return features, target

X, Y = featureSelection()

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.4)

regr = LinearRegression()
regr.fit(x_train, y_train)


print(regr.predict([81.29, 90.79, 3, 86.0, 615, 685, 625]))

##pred = regr.predict([81.29, 90.79, 3, 86.0, 615, 685, 625])

pred = regr.predict([int(a), int(b), int(c), int(d), int(e), int(f), int(g)])

regr.score(x_train, y_train)

classifier = LogisticRegression()
classifier.fit(x_train, y_train)

train_acc = classifier.score(x_train, y_train)
print(train_acc)

model = classifier.predict(x_test)
metrics.accuracy_score(y_test, model)



print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <h1>Your Salary must be {}</h1>
</body>
</html>
""".format(pred))
