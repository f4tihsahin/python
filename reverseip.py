import requests
from bs4 import BeautifulSoup
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
site=input("Site giriniz(ex:google.com): ")
r = requests.get(f'https://viewdns.info/reverseip/?host={site}&t=1',headers={'User-Agent': user_agent})
source = BeautifulSoup(r.content,"lxml")
td=source.find('table',{'border': '1'})
with open(site+".txt","w") as f:
    for i in td.findAll('tr')[1:]:
        for a in i.findAll('td')[0]:
            print("Site adı ile txt dosyası oluşturuldu.")
            f.write(a+"\n")
