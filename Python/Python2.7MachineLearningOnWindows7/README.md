# Python 2.7 - Machine Learning On Windows 7

## Packages

### Python 2.7
https://www.python.org/download/releases/2.7/

### Scipy with Windows Binaries for Python 2.7
http://www.lfd.uci.edu/~gohlke/pythonlibs/
file: scipy-0.16.0-cp27-none‑win_amd64.whl

### Numpy MKL with Windows Binaries for Python 2.7
http://www.lfd.uci.edu/~gohlke/pythonlibs/
file: numpy-1.9.2+mkl-cp27-none-win_amd64.whl

### sklearn
<code>pip install sklearn</code>

## Random Forest
<code>
# Import the random forest package
from sklearn.ensemble import RandomForestClassifier 

# Create the random forest object which will include all the parameters
# for the fit
forest = RandomForestClassifier(n_estimators = 100)

# Fit the training data to the Survived labels and create the decision trees
forest = forest.fit(train_data[0::,1::],train_data[0::,0])

# Take the same decision trees and run it on the test data
output = forest.predict(test_data)
</code>