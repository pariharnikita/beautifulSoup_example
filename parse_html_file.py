import requests
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com/"

page = requests.get(URL)

soup = BeautifulSoup(page.content,'html.parser')

link = soup.find("a", {"class": "hnuser"})

nextpage = requests.get(URL+link.get('href'))

nextsoup = BeautifulSoup(nextpage.content,'html.parser')

tr_list = nextsoup.findAll("tr")[-5].findAll('td')[-1].text

print(tr_list)



