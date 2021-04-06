print("Hello Gohil")
import requests
import csv

from bs4 import BeautifulSoup
url = "https://www.flipkart.com/clothing-and-accessories/topwear/tshirt/men-tshirt/pr?sid=clo,ash,ank,edy&otracker=categorytree&otracker=nmenu_sub_Men_0_T-Shirts"
r = requests.get(url)
htmldata = r.content
soupdata = BeautifulSoup(htmldata,'html.parser')
divData = soupdata.find_all("div", attrs={"style":"width:25%"})
head = "Product Name, price\n"
with open("data1.csv","w") as f:
    f.write(head)
    f.close()
for item in divData:
    Childdiv = item.findChild("div",class_="_1xHGtK _373qXS")
    priceTag = Childdiv.findChild("div",class_="_30jeq3").text
    nameTag = Childdiv.findChild("div",class_="_2WkVRV").text
    with open("data1.csv","a",encoding='UTF-8') as f:
        f.write(nameTag+","+priceTag.replace(',','')+"\n")
        f.close()










