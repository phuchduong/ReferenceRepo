# if python 3.XX
from sys import version_info as python_version
if python_version >= (3,0):
    from urllib.request import urlopen
else:
    from urllib2 import urlopen