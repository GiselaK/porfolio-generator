from bs4 import BeautifulSoup
from selenium import webdriver

def getUserData ():
	driver = webdriver.Chrome('/usr/local/Cellar/chromedriver/2.26/bin/chromedriver') #I actually used the chromedriver and did not test firefox, but it should work.
	profile_link = "https://www.linkedin.com/in/giselakottmeier"
	driver.get(profile_link)
	html = driver.page_source
	soup = BeautifulSoup(html) #specify parser or it will auto-select for you
	userData = {}
	userData["summary"] = soup.find('section', { "id" : "summary" })
	userData["name"] = soup.find('h1', { "id" : "name" })
	userData["title"] = soup.find('section', {"id" : "topcard"})
	userData["demographics"] = soup.find('dl', {"id" : "demographics"})
	userData["projects"] = soup.find('section', { "id" : "projects" })
	userData["skills"] = soup.find('section', { "id" : "skills" })
	userData["education"] = soup.find('section', { "id" : "education" })
	userData["experience"] = soup.find('section', { "id" : "experience" })
	userData["volunteering"] = soup.find('section', { "id" : "volunteering" })
	return userData

getUserData()
