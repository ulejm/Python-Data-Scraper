from bs4 import BeautifulSoup
from selenium import webdriver
import json
import csv


f = open('/Users/sebastiansigg/Desktop/data.csv', 'w')
writer = csv.writer(f)

with open("/Users/sebastiansigg/Desktop/Links2.txt", "r") as file:
    list = []
    for line in file:
        list += [line.strip()]

PATH = "/usr/local/bin/chromedriver"

#with open("/Users/sebastiansigg/Desktop/LinksTest.txt", "r") as file:
#    list = []
#    for line in file:
#        list += [line.strip()]
for link in list:
    driver = webdriver.Chrome(PATH)
    driver.get(link)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    try:
        GTIN = str(soup.find('script', attrs = {'type':'application/ld+json'}))
        #GTIN2 = GTIN.find("meso-data")
        GTIN = GTIN.replace("<script type=\"application/ld+json\">", "", 1).replace("</script>", "", 1)
        SKU = json.loads(GTIN)['sku']
        print SKU
    except Exception as e:
        print "nicht vorhanden"
        SKU = "nicht vorhanden"
    try:
        name = str(soup.find("h1", attrs = {"class":"pdr-QuickInfo__heading"})).split(">")[1].split("<")[0]
        print name
    except Exception as e:
        print "nicht vorhanden"
        name = "nicht vorhanden"

    try:
        desciption = str(soup.find("pre", attrs = {"class":"pdr-Attribute"})).split(">")[1].split("<")[0]
        print desciption
        lander = ["deutschland", "italien", "schweiz", "belgien", "niederlande", "frankreich", "mexiko", "ecuador", "guatemala", "panama", "spanien", "neuseeland", "schweden", "russland", "osterreich", "polen", "brasilien", "bulgarien", "chile", "bolivien", "china", "costa rica", "dominikanische", "finnland", "griechenland", "indien", "irak", "indonesien", "iran", "irland", "israel", "japan", "kanada", "kenia", "korea", "kroatien", "marokko", "nepal", "norwegen", "paraguay", "peru", "portugal", "saudi", "singapur", "slowenien", "sri lanka", "afrika", "thailand", "turkei", "uganda", "ukraine", "tunesien", "ungarn", "uruguay", "emirate", "vereinigtes", "vietnam", "zypern", "usa"]
        herkunft = ""
        for land in lander:
            if desciption.lower().find(land) != -1:
                herkunft += land + "/"
        print herkunft
    except Exception as e:
        print "---"   
        description =  "none"   

    try:
        categorylist = soup.find_all("a", attrs = {"class":"lr-breadcrumbs__link"})

        majorcat = str(categorylist[0]).split("</div> ")[1].split("</a>")[0]
        middlecat = str(categorylist[1]).split("</div> ")[1].split("</a>")[0]
        subcat = str(categorylist[2]).split("</div> ")[1].split("</a>")[0]
        print majorcat
        print middlecat
        print subcat
    except Exception as e:
        print "nicht vorhanden"
        majorcat = "none"
        middlecat = "none"
        subcat = "none"
    #subcategories = ""
    #for category in categorylist:
    #    subcategories += str(category).split("</div> ")[1].split("</a>")[0] + "/"
    #print subcategories

    try:
        eigenschaften = soup.find_all("div", attrs = {"class":"pdr-Attribute"})
        eigenschaftenstring = ""
        for eigenschaft in eigenschaften:
            eigenschaftenstring += str(eigenschaft)
    except Exception as e:
        print "nicht vorhanden"

    try:
        marke = eigenschaftenstring.split("Marke: </h3>")[1].split("<")[0]
        print marke
    except Exception as e:
        print "---"
        marke = "none"

    try:
        eig = eigenschaftenstring.split("Eigenschaften: </h3>")[1].split("<")[0]
        print eig
    except Exception as e:
        print "---"
        eig = "none"

    try:
        Herkunftsland = eigenschaftenstring.split("Ursprungsland: </h3>")[1].split("<")[0]
        print Herkunftsland
    except Exception as e:
        print "---"
        try:
            Herkunftsland = herkunft   
            print Herkunftsland 
        except Exception as e:
            print "kein Land vorhanden"
            Herkunftsland = "nicht vorhanden"

    writer.writerow([SKU, name, majorcat, middlecat, subcat, marke, eig, Herkunftsland])