#Coded By Can Üstün
#Yaşasın Open Source Code :)
#İG : @canustun_software

#içe aktarımlar
import requests as req
from bs4 import BeautifulSoup
from time import sleep
import os

def veri_cek(): #döviz verilerini çekebileceğimiz site ve işlemler
    global veriler
    veriler = []
    try:
        site = req.get("https://uzmanpara.milliyet.com.tr") #Anlık olarak sitenin verilerini aldık
        kaynak = BeautifulSoup(site.content,"html.parser")  #siteyi parçaladık
        for i in kaynak.find_all("div",{"class":"headerBot"}): #siteden dövizlerin olduğu parçalı veriyi aldık
            veriler.append(i.text)
            
    except:pass
        

veri_cek()

while True: #Herzaman en güncel verileri görmek için sonsuz döngü

    temiz_veriler=str(veriler).split("\\n") #karışık gelen verilerde küçük bi temizlik
    for i in temiz_veriler:
        temiz_veriler.remove("")
    temiz_veriler.remove(temiz_veriler[0])
    temiz_veriler.remove(temiz_veriler[-1])

    #Döviz verilerini görmek için print işlemleri
    print(f"Yapımcı : C4n Üstün\n\nİLETİŞİM : \n- İnstagram : @canustun_software\n- Telegram : @canustun_4\n\n! Güncel Döviz Verileri !\n\n")
    for i in range(0,15,3):
        print(f"""Döviz adı : {temiz_veriler[i]}
Anlık değeri : {temiz_veriler[i+1]}
Düne göre değer artış veya azalışı : {temiz_veriler[i+2]}
{'*'*20}

""")

    veri_cek() #Diğer döngü için verileri tekrar çek
    os.system("clear||cls") #Ekran kalabalık olmaması için ekranı temizle 
