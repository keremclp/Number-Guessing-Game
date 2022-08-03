import time
import random

print("""
Oyuna hoşgeldiniz

-----------------------

İyi Eğlenceler.....
""")


rastgele_sayı = random.randint(1,100)
tahmin_hakkı = 10

while True :
    tahmin = int(input("Bir sayı giriniz: "))
    if tahmin < rastgele_sayı:
        time.sleep(1)

        print("Daha yüksek sayı giriniz")

        tahmin_hakkı -= 1

    elif tahmin > rastgele_sayı:
        time.sleep(1)

        print("Daha düşük bir sayı giriniz")

        tahmin_hakkı -= 1
    else:
        print("Bilgiler sorgulanıyor.....")
        time.sleep(1)
        print("Tebrikler, bildiniz!!")
        break
    if tahmin_hakkı == 1:
        time.sleep(1)
        print("----Son hakkınız kaldı!!!-----")
    elif tahmin_hakkı == 0:
        print("Tahmin hakkınız bitti, Yenildiniz!!")
        print("Bilmeniz gereken sayı: ",rastgele_sayı)
        break


