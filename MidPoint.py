
from mpi4py import MPI
#MPI kümedeki tüm process lerin arasindaki baglantiyi saglar.
comm= MPI.COMM_WORLD
#rank simdiki yani suan calisan process i bildirir.
rank = comm.Get_rank()
#kümedeki calisan process lerin toplam sayisini verir.
size = comm.Get_size()

#midpoint integral fonksiyonlari
def f(x):
    return x * x

def midpoint(a,b):
    baslangic =0
    bitis =1
    tekrar =10000
    adim = (bitis - baslangic) / tekrar
    deger = 0
    for i in range(a,b):
        deger += adim*f(baslangic + (i - 1) * adim)
    return deger

#fonksiyonu bir degiskene atiyoruz.
paylas=midpoint(a,b)
#her core dan gelen/return eden degeri atamak icin olusturduk degiskeni.
topla=0

#ilk core fonksiyonu kullanmaya baslayacagi icin ayri tuttuk digerlerinden .
if rank==0:
    paylas=midpoint(a,b)
    #toplaya ilk deger olarak fonksiyon ilk calistigi zaman donen deger atandi rank 0 dan.
    topla=paylas
    #rank 0 dan rank 1 e topla degerini gonderiliyor.
    comm.send(topla,dest=1)

#rank 1 den son ranka kadar dongu olusturuyoruz.
for i in range(1,size):
 #her core (rank 0 haricti) bir onceki core dan gonderilenler aliniyor.
 veri = comm.recv(souce=(rank - 1) % size)
 #fonksiyona devam ediliyor.
 paylas=midpoint(a,b)
 #gelen ve donen degerler degiskene ataniyor.
 topla=veri+paylas
 #donen deger bir sonraki core a gonderiliyor.
 comm.send(topla,dest=(rank+1)%size)
 #Deger ekrana yaziliyor.
 print(topla)
