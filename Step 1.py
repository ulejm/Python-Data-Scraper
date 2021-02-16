import requests
from bs4 import BeautifulSoup
from selenium import webdriver

PATH = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome(PATH)

with open("/Users/sebastiansigg/Desktop/Links.txt", "r") as file:
    list = []
    for line in file:
        list += [line.strip()]

endpoint = open("/Users/sebastiansigg/Desktop/Links2.txt", "a")

for productPage in list:
    driver = webdriver.Chrome(PATH)
    url = productPage
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    data = soup.find_all('div', attrs = {'class':'search-service-productDetailsWrapper'})
    for div in data:
        links = div.find_all('a')
        for a in links:
            endpoint.write("https://shop.rewe.de" + a['href'] + "\n")
            #print a['href']

#for link in soup.find_all('a'):
 #   print(link.get('href'))



#url = "https://shop.rewe.de/p/salatgurke/483303"

#result = requests.get(url)

#print(result.text)
