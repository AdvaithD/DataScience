# Building a 'Decision tree' machine learning model
# Asks each data point that it receives a question which is answered with a 'yes/no'
from sklearn import tree


# [height, weight, shoe size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

# variable to store decision tree model classifier
clf = tree.DecisionTreeClassifier()

# The .fit() method trains the decision tree on our dataset
clf = clf.fit(X, Y)

# Test by classifying the gender of a new person with their body metrics considered
prediction = clf.predict([[190,70,43]])

print(prediction)
