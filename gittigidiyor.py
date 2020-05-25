from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
my_url = "https://www.gittigidiyor.com/bilgisayar-bilesenleri/ekran-grafik-karti?k=ekran%20kart%C4%B1&qm=1"
uClient = req(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")


containers = page_soup.findAll("li",{"class":"gg-uw-6 gg-w-8 gg-d-8 gg-t-8 gg-m-24 gg-mw-12 catalog-seem-cell"})

for container in containers:

    urunadi = container.a.div.div.div.div.h3.span.text
    fiyat = container.a.div.div.select("div")[2].p.text.replace("\n","")
    fiyat = fiyat.replace("                    "," ")
    fiyat = fiyat.rstrip()
    fiyat = fiyat.lstrip()

    print("fiyat: " + fiyat + "  Urunadı: " + urunadi + "\n")

