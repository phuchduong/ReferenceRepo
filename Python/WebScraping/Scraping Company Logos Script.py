from bs4 import BeautifulSoup
from urllib import request as ulReq
import os.path

soupClient = BeautifulSoup

# parent url
baseURL = "http://datasciencedojo.com/bootcamp/alumni/"

element = 'div'
selector = 'avia-content-slider-inner'

# summary lists
allLogos = []
failedLogos = []
skippedLogos = []
parsedLogos = []

#where do you want to save your images?
baseDir = 'C:\\GitRepos\\DSDLegacyCode\\WordPress\\v1\\Company Logos'

print("Scraping... " + baseURL)
ulClient = ulReq.urlopen(baseURL)
pageSoup = BeautifulSoup(ulClient.read(), 'html.parser')
selectedElements = pageSoup.find_all(element,selector)
if len(selectedElements) > 0 :
	logoImgURL = sliderDivs[0].img['data-src']
	logoImgURLSplit = logoImgURL.split('/')
	imgNameOrg = logoImgURLSplit[-1]
	imgSplit = imgNameOrg.split('.')
	imgFormat = imgSplit[-1]
	imgNameNew = logo + "-banner" + "." + imgFormat
	if os.path.isfile(imgNameNew) is not True:
		print("saving image for..." + logo + "... as..." + imgNameNew)
		localDir = baseDir + imgNameNew
		ulReq.urlretrieve(logoImgURL, localDir)
		parsedLogos.append(logo)
	else:
		print(imgName + " already exists... skipping...")
		skippedLogos.append(logo)
else:
	print("Failed to grab logo. Skipping...")
	failedLogos.append(logo)

print("Summary report")
print("parsedLogos: " + ', '.join(parsedLogos))
print("skippedLogos: " + ', '.join(skippedLogos))
print("failedLogos: " + ', '.join(failedLogos))