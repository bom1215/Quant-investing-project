import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class" :"class="VfPpkd-EScbFb-JIbuQc MxsXJd""})
print(len(movies))