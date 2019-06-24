import requests
file = open('s.txt').readlines()
dosya = open("liste.txt", "a")
for i in file:
    r = requests.get(i)
    r=str(r)
    if r=='<Response [200]>':
        dosya.write(i)
dosya.close()
