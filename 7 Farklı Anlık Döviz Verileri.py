import requests as req
from bs4 import BeautifulSoup
import os

doviz_isimler=["Gram Altın","Dolar","Euro","Sterlin","BIST 100","Bitcoin","Gümüş"]

def veri_cek():
    global doviz_isimler,doviz_deger
    site = req.get("https://doviz.com")
    soup = BeautifulSoup(site.content,"html.parser")

    doviz_deger=[]

    for i in soup.find_all("span", {"class":"value"}):
        doviz_deger.append(i.text)

    doviz_deger.pop(7)
    


veri_cek()
while True:

    for i,j in zip(doviz_isimler,doviz_deger):
        print("Döviz Adı :",i,
              "\nTL'ye Hesaben Değeri:",j,f"\n {'*'*20}")
        
    veri_cek()
    os.system("cls||clear")
    
        
    
