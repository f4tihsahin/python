import requests
from bs4 import BeautifulSoup
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
r = requests.get('https://viewdns.info/reverseip/?host=194.27.43.67&t=1',headers={'User-Agent': user_agent})
source = BeautifulSoup(r.content,"lxml")
td=source.find('table',{'border': '1'})
for i in td.findAll('tr')[1:]:
    for a in i.findAll('td')[0]:
        print(a)