from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# 1️⃣ Model Declaration
# Load the Iris dataset
iris  = datasets.load_iris()
# print(iris.DESCR)

# 2️⃣ Model Fitting (Training)
features = iris.data   #features (inputs)
labels = iris.target #labels (output)

# print(features)
# print(lables)

# Initialize and train the classifier
clf = KNeighborsClassifier()
clf.fit(features, labels)

# 3️⃣ Model Prediction
preads = clf.predict([[31,1,1,1]])
print(preads)