
from mpi4py import MPI
import math

#MPI kümedeki tüm process lerin arasindaki baglantiyi saglar.
comm=MPI.COMM_WORLD
#rank simdiki yani suan calisan process i bildirir.
rank=comm.Get_rank()
#kümedeki calisan process lerin toplam sayisini verir.
size=comm.Get_size()

#fonksiyonumuza baslangic ve bitis degerleri alabilmesi icin parametre giriyoruz.
def piSayisi(a,b):
    #her rank ta bulunan sonucu aktarmak icin degisken atandi.
    deger=0
    #dongu olusturuldu parametre olarak verilen aralik uzunlugu kadar deger buluncak.
    for i in range(a,b):
        deger+=4*(((-1)**i)/(2*i+1))
    #bulunan deger fonksiyona geri donduruluyor.
    return deger

#her rank tan gelen degerleri topla degiskenine aktarmak icin tanimladik.
topla=0
#rank 0 sonucu bulup rank 1 e gonderir.
if rank==0:
    sonuc=piSayisi(0,2500)
    comm.send(sonuc,dest=1)
#rank 1 rank 0 dan gelen sonucu alip fonksiyona devam eder ve kendi buldugu sonuc ile
#rank 0 dan gelen sonucu topla degiskeninde toplayip rank 2 ye gonderir.
if rank==1:
    sonuc=comm.recv(source=0)
    veri=piSayisi(2500,5000)
    topla=sonuc+veri
    comm.send(topla,dest=2)
#rank 2 rank 1 den gelen sonucu alip fonksiyona devam eder ve kendi buldugu sonuc ile
#rank 1 den gelen sonucu topla degiskeninde toplayip rank 3 e gonderir.(rank 1 in yaptigi gibi)
if rank==2:
    sonuc=comm.recv(source=1)
    veri=piSayisi(5000,7500)
    topla=sonuc+veri
    comm.send(topla,dest=3)
#rank 3 rank 2 den gelen degeri ve kendi buldugu sonucu toplayip,en son ekrana yazdirir sonucu.
if rank==3:
    sonuc=comm.recv(source=2)
    veri=piSayisi(7500,10000)
    topla=veri+sonuc
    printf(topla)




