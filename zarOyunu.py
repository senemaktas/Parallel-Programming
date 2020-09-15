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
b=250

#fonksiyonumuzu olusturuyoruz.
def zarOyunu(a,b):
    # iki degerli listemizi numpy ile olusturuyoruz.
    dizi = np.array([[1], [1]])
    #i degeri herbiri icin 250 degerine sayiyor
    i = 1
    # j degeri ise kac kere kosulun meydana geldiginin degerini tutuyor.
    j = 1
    #hangi degerler icerebilecegini  listemize yaziyoruz.
    rakamlar = [1, 2, 3, 4, 5, 6]
    #rakamlari karistiriyoruz.
    random.shuffle(rakamlar)

    #kac kere tekrarlamasini istiyorsak donguyu kosulluyoruz,b ye yukarida 250 degerini atadik.
    while i <= b:

        #dizimizin 1. ve 2. elemanina rakamlar dizisinden rastgele degerler atiyoruz.
        dizi[0] = random.choice(rakamlar)
        dizi[1] = random.choice(rakamlar)
        #(3,2) kosul geldigi zaman bunu ekrana yazdirip ,kosulun kacinci kere saglandigini bildirir.
        if dizi[0] == 3 and dizi[1] == 2:
            printf("""Deneme {}:\t({},{}) {} *** """.format(i, dizi[0], dizi[1], j))
            #her saglanan kosul icin j degeri 1 arttirilir.
            j += 1
        #kosul saglanmazsa deneme + kacinci deneme oldugu ve gelen deger yazdilir.
        else:
            printf("""Deneme {}:\t({},{}) """.format(i, dizi[0], dizi[1]))
        #i sayisi 1 arttirilir.
        i += 1

    #her birinden kac kere (3,2) kosulunun saglandigi ekrana yazilir.
    printf("""\n*** rank {} dan {} kere (3,2) geldi ***""".format(rank,(j - 1)))
    #bu toplam deger geri dondurulur fonksiyona.
    return (j-1)

#rank 0 ile fonksiyonu zar degiskenine atadik.
if rank==0:
    zar=zarOyunu(a,b)
else:
    zar=None
#root yani rank 0 dan diger core lara dagitim yapiriz.
zar=comm.send(zar,root=0)  #send ile cunku 250 ser gidicek herbirine
toplam=0
#herbirinden donen degeri topluyoruz.
for i in range(size):
        toplam+=(j-1)
#islem yapildiktan sonra root a degerler donus yapiliyor.
veriTopla=comm.gather(zar,root=0)
#alinan degerler ekrana cikti olarak yaziliyor.
if rank==0:
    printf("""\n*** toplam {} kere (3,2) geldi ***""".format(toplam))
    printf(""" veriler {} """.format(veriTopla))
