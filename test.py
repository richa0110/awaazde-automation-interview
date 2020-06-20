
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

driver = webdriver.Chrome('./chromedriver')
driver.get("https://Weathershopper.pythonanywhere.com")


#Get Temperature Parent Element
temperatureParent = driver.find_element_by_id("temperature")


if temperatureParent.is_displayed():
	#If displayed get value 
	temperature = temperatureParent.text
	print(temperature)
	r = re.search("\d+", temperature)
	result = r.group(0)
	temperatureVal =int(result)
	print(temperatureVal)
# compare
	if temperatureVal < 1 : #for testing should be 19
		#driver.find_element_by_tag_name("button").find_element_by_text("Buy moisturizers")
		element =driver.find_element_by_xpath("//button[contains(text(),'Buy moisturizer')]")
		print("moisturizer")
		element.click()
		driver.implicitly_wait(10)
		print (element)

		
	elif temperatureVal > 1: #for testing should be 34
		element =driver.find_element_by_xpath("//button[contains(text(),'Buy sunscreens')]")
		#element = driver.find_element_by_tag_name("button").find_element_by_text("Buy sunscreens") 
		print("sunscreens")
		element.click()
		driver.implicitly_wait(10)
		print (element)

		spf30Items =driver.find_elements_by_xpath("//p[contains(text(),' SPF-30')]")
		print (spf30Items)
		attrs={}
		dictionary = {}
		

		print ("items spf")
		for spf30Item in spf30Items:
			print (spf30Item.text)
			print (spf30Item.id);

			parent_el = spf30Item.find_element_by_xpath("..")

			nameEl = parent_el.find_element_by_xpath("(.//p)[1]")
			print (nameEl.text)
			priceEl = parent_el.find_element_by_xpath("(.//p)[2]")
			print (priceEl.text)
			buttonEl = parent_el.find_element_by_xpath("(.//button)[1]")
			print (buttonEl.text)

			#get price
			r = re.search("\d+$", priceEl.text)
			result = r.group(0)
			priceVal =int(result)
			print (priceVal)
			print (buttonEl)
			print ("===================")
			dictionary[priceVal] =buttonEl;


		lst = dictionary.keys()
		# Sorted by key

		sortedDict = sorted(lst)
		print("Sorted by key: ", sortedDict)
		leastSpf = dictionary[sortedDict[0]];
		print("Sorted by key: ", leastSpf.text)
		leastSpf.click()


		driver.implicitly_wait(15)





driver.close()