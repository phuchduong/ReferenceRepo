# Python 2.7 - Machine Learning On Windows 7

## Packages

### Python 2.7
https://www.python.org/download/releases/2.7/

### Scipy with Windows Binaries for Python 2.7
http://www.lfd.uci.edu/~gohlke/pythonlibs/ </br>
file: scipy-0.16.0-cp27-none‑win_amd64.whl
<code>pip install C:\MyLocation\scipy-0.16.0-cp27-none‑win_amd64.whl</code>

### Numpy MKL with Windows Binaries for Python 2.7
http://www.lfd.uci.edu/~gohlke/pythonlibs/  </br>
file: numpy-1.9.2+mkl-cp27-none-win_amd64.whl
<code>pip install C:\MyLocation\numpy-1.9.2+mkl-cp27-none-win_amd64.whl/code>

### sklearn
<code>pip install sklearn</code>

## Random Forest
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