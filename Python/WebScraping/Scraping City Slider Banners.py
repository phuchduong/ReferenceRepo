Python 3.5.0 |Anaconda 2.4.0 (64-bit)| (default, Oct 20 2015, 07:26:33) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from bs4 import BeautifulSoup
>>> from urllib import request as ulReq
>>> ulClient = ulReq.urlopen('http://datasciencedojo.com/pricing/dc/')
>>> pageSoup = BeautifulSoup
>>> pageSoup = BeautifulSoup(ulClient.read(), 'html.parser')
>>> pageSoup.h1
<h1 class="ls-l" data-ls="fadeout:false;" style="top:222px;left:52px;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;font-size:55px;color:#ffffff;background:rgba(117, 117, 117, 0.65);white-space: nowrap;">Hands-On Data Science &amp; Engineering</h1>
>>> pageSoup.div['ls-slide ls-animating']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Anaconda3\lib\site-packages\bs4\element.py", line 958, in __getitem__
    return self.attrs[key]
KeyError: 'ls-slide ls-animating'
>>> pageSoup.findall['ls-slide ls-animating']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'NoneType' object is not subscriptable
>>> pageSoup.findall('ls-slide ls-animating')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'NoneType' object is not callable
>>> pageSoup.find_all('ls-slide ls-animating')
[]
>>> pageSoup.find_all('ls-slide')
[]
>>> pageSoup.h1
<h1 class="ls-l" data-ls="fadeout:false;" style="top:222px;left:52px;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;font-size:55px;color:#ffffff;background:rgba(117, 117, 117, 0.65);white-space: nowrap;">Hands-On Data Science &amp; Engineering</h1>
>>> pageSoup.find_all("div","ls-slide")
[<div class="ls-slide" data-ls="slidedelay:8000;transition2d:5;"><img alt="dc-1200×500" class="ls-bg" data-src="http://datasciencedojo.com/wp-content/uploads/2015/10/dc-1200x500.jpg" src="http://datasciencedojo.com/wp-content/plugins/LayerSlider/static/img/blank.gif"/><h1 class="ls-l" data-ls="fadeout:false;" style="top:222px;left:52px;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;font-size:55px;color:#ffffff;background:rgba(117, 117, 117, 0.65);white-space: nowrap;">Hands-On Data Science &amp; Engineering</h1><h1 class="ls-l" data-ls="fadeout:false;" style="top:312px;left:53px;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;font-size:40px;color:#ffffff;background:rgba(117, 117, 117, 0.65);white-space: nowrap;">DC - December 7th - 11th</h1></div>]
>>> pageSoup.find_all("div","ls-slide").img
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'ResultSet' object has no attribute 'img'
>>> pageSoup.find_all("div","ls-slide")[img]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'img' is not defined
>>> pageSoup.find_all("div","ls-slide")
[<div class="ls-slide" data-ls="slidedelay:8000;transition2d:5;"><img alt="dc-1200×500" class="ls-bg" data-src="http://datasciencedojo.com/wp-content/uploads/2015/10/dc-1200x500.jpg" src="http://datasciencedojo.com/wp-content/plugins/LayerSlider/static/img/blank.gif"/><h1 class="ls-l" data-ls="fadeout:false;" style="top:222px;left:52px;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;font-size:55px;color:#ffffff;background:rgba(117, 117, 117, 0.65);white-space: nowrap;">Hands-On Data Science &amp; Engineering</h1><h1 class="ls-l" data-ls="fadeout:false;" style="top:312px;left:53px;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;font-size:40px;color:#ffffff;background:rgba(117, 117, 117, 0.65);white-space: nowrap;">DC - December 7th - 11th</h1></div>]
>>> pageSoup.find_all("div","ls-slide")[0].img
<img alt="dc-1200×500" class="ls-bg" data-src="http://datasciencedojo.com/wp-content/uploads/2015/10/dc-1200x500.jpg" src="http://datasciencedojo.com/wp-content/plugins/LayerSlider/static/img/blank.gif"/>
>>> pageSoup.find_all("div","ls-slide")[0].img["data-src"]
'http://datasciencedojo.com/wp-content/uploads/2015/10/dc-1200x500.jpg'
>>> pageSoup.retrieve("div","ls-slide")[0].img["data-src"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'NoneType' object is not callable
>>> imgURL =pageSoup.find_all("div","ls-slide")[0].img["data-src"]
>>> ulReq.urlretrieve(imgURL, "toronto.jpg")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Anaconda3\lib\urllib\request.py", line 197, in urlretrieve
    tfp = open(filename, 'wb')
PermissionError: [Errno 13] Permission denied: 'toronto.jpg'
>>> ulReq.urlretrieve(imgURL, "C:\GitRepos\ReferenceRepo\Python\WebScraping\toronto.jpg")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Anaconda3\lib\urllib\request.py", line 197, in urlretrieve
    tfp = open(filename, 'wb')
OSError: [Errno 22] Invalid argument: 'C:\\GitRepos\\ReferenceRepo\\Python\\WebScraping\toronto.jpg'
>>> ulReq.urlretrieve(imgURL, "C:\\GitRepos\\ReferenceRepo\\Python\WebScraping\\toronto.jpg")
('C:\\GitRepos\\ReferenceRepo\\Python\\WebScraping\\toronto.jpg', <http.client.HTTPMessage object at 0x0000003B0017F9E8>)
>>> 