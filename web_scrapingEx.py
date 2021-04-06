import requests
from bs4 import BeautifulSoup
url = "https://freetool.website/"
r = requests.get(url)
htmldata = r.content
soupdata = BeautifulSoup(htmldata,'html.parser')
# print(soupdata.prettify())

#Find Title website title
Title = soupdata.title
print(Title)

#Find One Title with Html Tags
Title1 = soupdata.find('h4')
# print(Title1)

#Find One Title with only Text
Title1_onlytext = soupdata.find('h4').get_text()
# print(Title1_onlytext)

#Find All h4 Tags
Title_allTags = soupdata.find_all('h4')
# print(Title_allTags)

# Class name find of elemets
# print(soupdata.find('p')['class'])

# Find tag using Class
# print(soupdata.find_all('p',class_='card-text'))

#Find All anchor Tags
anchor_tags = soupdata.find_all('a')
# print(anchor_tags)
all_link = set() #Create set
for link in anchor_tags:
    if(link.get('href')[0] != '/'):
        all_link.add(link.get('href'))
        # print(link.get('href'))
print(all_link)
print(len(all_link))

#Class or ID through Get Data
divMain = soupdata.find(class_='col-md-10 col-sm-8 col-xl-10 col-xxl-10')
# for ele in divMain.children:
    # print(ele)

#string formate data display
for ele in divMain.stripped_strings:
    print(ele)