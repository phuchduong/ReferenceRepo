from bs4 import BeautifulSoup
from urllib import request as ulReq
import os.path

soupClient = BeautifulSoup

# parent url
baseURL = "http://datasciencedojo.com/bootcamp/alumni/"

# summary lists
failedLogos = []
skippedLogos = []
parsedLogos = []

#where do you want to save your images?
baseDir = 'C:\\GitRepos\\DSDLegacyCode\\WordPress\\v1\\Company Logos'

print("Begin scraping... " + baseURL)
ulClient = ulReq.urlopen(baseURL)
pageSoup = BeautifulSoup(ulClient.read(), 'html.parser')
sliderDivs = cityPageSoup.find_all('div','avia-content-slider-inner')
if len(sliderDivs) > 0 :
	cityImgURL = sliderDivs[0].img['data-src']
	cityImgURLSplit = cityImgURL.split('/')
	imgNameOrg = cityImgURLSplit[-1]
	imgSplit = imgNameOrg.split('.')
	imgFormat = imgSplit[-1]
	imgNameNew = city + "-banner" + "." + imgFormat
	if os.path.isfile(imgNameNew) is not True:
		print("saving image for..." + city + "... as..." + imgNameNew)
		localDir = baseDir + imgNameNew
		ulReq.urlretrieve(cityImgURL, localDir)
		parsedLogos.append(city)
	else:
		print(imgName + " already exists... skipping...")
		skippedLogos.append(city)
else:
	print("Failed to grab city. Skipping...")
	failedLogos.append(city)

print("Summary report")
print("parsedLogos: " + ', '.join(parsedLogos))
print("skippedLogos: " + ', '.join(skippedLogos))
print("failedLogos: " + ', '.join(failedLogos))