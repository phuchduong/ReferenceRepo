# Python 2.7 - Machine Learning On Windows 7

## Packages

### Python 2.7
https://www.python.org/download/releases/2.7/

### Scipy with Windows Binaries for Python 2.7
http://www.lfd.uci.edu/~gohlke/pythonlibs/ </br>
file: scipy-0.16.0-cp27-none‑win_amd64.whl </br>
<code>pip install C:\MyLocation\scipy-0.16.0-cp27-none‑win_amd64.whl</code>

### Numpy MKL with Windows Binaries for Python 2.7
http://www.lfd.uci.edu/~gohlke/pythonlibs/  </br>
file: numpy-1.9.2+mkl-cp27-none-win_amd64.whl </br>
<code>pip install C:\MyLocation\numpy-1.9.2+mkl-cp27-none-win_amd64.whl</code>

### sklearn
<code>pip install sklearn</code>

# Machine Learning

## Intro to Python for Data Science
[Source: Kaggle](https://www.kaggle.com/c/titanic/details/getting-started-with-python "Kaggle Intro to Python")

## Random Forest
[Source: Kaggle](https://www.kaggle.com/c/titanic/details/getting-started-with-random-forests "Kaggle Random Forest") <br>
<pre><code>
# Import the random forest package
from sklearn.ensemble import RandomForestClassifier 

# Create the random forest object which will include all the parameters
# for the fit
forest = RandomForestClassifier(n_estimators = 100)

# Fit the training data to the Survived labels and create the decision trees
forest = forest.fit(train_data[0::,1::],train_data[0::,0])

# Take the same decision trees and run it on the test data
output = forest.predict(test_data)
</code></pre>
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
df.head()

train, test = df[df['is_train']==True], df[df['is_train']==False]

features = df.columns[:4]
clf = RandomForestClassifier(n_jobs=2)
y, _ = pd.factorize(train['species'])
clf.fit(train[features], y)

preds = iris.target_names[clf.predict(test[features])]
pd.crosstab(test['species'], preds, rownames=['actual'], colnames=['preds'])
<pre><code>
	
</code></pre>