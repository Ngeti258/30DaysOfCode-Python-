import requests
import json
from bs4 import BeautifulSoup

url='http://www.bu.edu/president/boston-university-facts-stats/'
response=requests.get(url)
paragraph=response.content
soup=BeautifulSoup(paragraph,'html.parser')
content=soup.body
with open('sample.json','w') as outline:
    json.dumps(soup,outline)

print(outline)
