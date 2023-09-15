
import os
import requests
from requests.exceptions import HTTPError

os.chdir("C:/Users/root/Documents/python")

file = open('s.txt').readlines()

liste = list()
for i in file:
    try:
        r = requests.get(i.strip())
        if r.status_code == 200:
            print(str(i)+' eristim.')
        elif r.status_code == 404 or r.status_code == 403 :
            print("Böyle bir dizin yok "+i.strip())
            liste.append(i.strip())
        else:
            print(i,r.status_code)
            
    except requests.exceptions.ConnectionError as err:
        print("Erişemedim ",i)
        

with open("liste.txt", "a") as f:
    for i in liste:
        f.write(i+"\n")
        
