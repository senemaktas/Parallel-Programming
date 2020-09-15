
from mpi4py import MPI
import sys
import random
import numpy as np

#MPI kümedeki tüm process lerin arasindaki baglantiyi saglar.
comm=MPI.COMM_WORLD
#rank simdiki yani suan calisan process i bildirir.
rank=comm.Get_rank()
#kümedeki calisan process lerin toplam sayisini verir.
size=comm.Get_size()

a=0
#herbir core esit gondermek icin boluyoruz core sayisina.
bol=10000/size

#Diziler size da belirtilen boyutta ve icindeki degerler 0 veya 1 random olarak olusturulur.
dizi1=np.random.randint(2,size=10000)
dizi2=np.random.randint(2,size=10000)

#hamming mesafesini bulup degeri donduren fonksiyon.
def hamming(a,bol):
    #Baslangic arasindaki mesafe 0 olarak baslar.
    mesafe= 0
    # L degeri dizi uzunlugu kadar.(dizilerin uzunlugu esittir/olmalidir.)
    L = len(dizi1)
   #Butun degerlerin karsilastirilabilmesi icin dongu L uzunlugu kadar surer.
    for i in range(L):
        #Her bir deger tek tek karsilastirilir.
        #Eger degerler birbirine esit degilse mesafe degiskenine +1 eklenir.
        if dizi1[i] != dizi2[i]:
            mesafe += 1
    #Son karsilastirmayi da yaptiktan sonra mesafe degiskeni degeri geri dondurulur.
    return mesafe

#fonksiyonu bir degiskene atiyoruz.
paylas=hamming(a,bol)
#her core dan gelen/return eden mesafe degerini atamak icin olusturduk degiskeni.
topla=0

#ilk core fonksiyonu kullanmaya baslayacagi icin ayri tuttuk digerlerinden .
if rank==0:
    paylas=hamming(a,bol)
    #toplaya ilk deger olarak fonksiyon ilk calistigi zaman donen deger atandi rank 0 dan.
    topla=paylas
    #rank 0 dan rank 1 e topla degerini gonderiliyor.
    comm.send(topla,dest=1)

#rank 1 den son ranka kadar dongu olusturuyoruz.
for i in range(1,size):
 #her core (rank 0 haricti) bir onceki core dan gonderilenler aliniyor.
 veri = comm.recv(souce=(rank - 1) % size)
 #fonksiyona devam ediliyor.
 paylas=hamming(a,bol)
 #gelen ve donen degerler degiskene ataniyor.
 topla=veri+paylas
 #donen deger bir sonraki core a gonderiliyor.
 comm.send(topla,dest=(rank+1)%size)
 #Deger ve diziler ekrana yaziliyor.
 print("""Hamming mesafesi = {}:\n Dizi1={}  \n \n Dizi2={}""".format(topla,dizi1,dizi2))
