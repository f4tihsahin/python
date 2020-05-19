import os
import requests
from requests.exceptions import HTTPError

os.chdir("C:/Users/root/Documents/python")

file = open('s.txt').readlines()
dosya = open("liste.txt", "a")

for i in file:
    try:
        r = requests.get(i.strip())
        if r.status_code == 200:
            print(str(i)+' eristim.')
        elif r.status_code == 404 or r.status_code == 403 :
            print("Böyle bir dizin yok "+i.strip())
            dosya.write(i+str(r.status_code)+"\n")
        else:
            print(i,r.status_code)
        
            
    except HTTPError as http_err:
        print(str(i)+ f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    except:
        print('erisemedigini yazdirdi')
    finally:
        r.close()
dosya.close()
