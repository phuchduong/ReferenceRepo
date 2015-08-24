from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pandas
import numpy as numpy

iris = load_iris()
df = pandas.DataFrame(iris.data, columns=iris.feature_names)
df['is_train'] = numpy.random.uniform(0, 1, len(df)) <= .75
df['species'] = pandas.Categorical.from_codes(iris.target, iris.target_names)
df.head()

train, test = df[df['is_train']==True], df[df['is_train']==False]

features = df.columnsn[:4]
clf = RandomForestClassifier(n_jobs=2)
y, _ = pandas.factorize(train['species'])
clf.fit(train[features], y)

preds = iris.target_names[clf.predict(test[features])]
pandas.crosstab(test['species'], preds, rownames=['actual'], colnames=['preds'])