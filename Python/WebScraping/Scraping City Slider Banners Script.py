from bs4 import BeautifulSoup
from urllib import request as ulReq
import os.path

soupClient = BeautifulSoup

# parent url
baseURL = "http://datasciencedojo.com/pricing/"

# child url
citiesAr = ["amsterdam","austin","bangalore","barcelona","chicago","copenhagen","dc","dubai","dublin","hong-kong","luxembourg","new york","oulu","paris","seattle","singapore","stockholm","sv","sydney","toronto","zurich"]

# summary lists
failedCities = []
skippedCities = []
parsedCities = []

#where do you want to save your images?
baseDir = 'C:\\GitRepos\\DSDLegacyCode\\WordPress\\v1\\Bootcamps\\CityPages\\'

for city in citiesAr:
	print("Scraping... " + city)
	cityPageURL = baseURL + city
	ulClient = ulReq.urlopen(cityPageURL)
	cityPageSoup = BeautifulSoup(ulClient.read(), 'html.parser')
	sliderDivs = cityPageSoup.find_all('div','ls-slide')
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
			parsedCities.append(city)
		else:
			print(imgName + " already exists... skipping...")
			skippedCities.append(city)
	else:
		print("Failed to grab city. Skipping...")
		failedCities.append(city)

print("Summary report")
print("parsedCities: " + ', '.join(parsedCities))
print("skippedCities: " + ', '.join(skippedCities))
print("failedCities: " + ', '.join(failedCities))