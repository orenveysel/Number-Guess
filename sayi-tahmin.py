'''
    1-100 arasında rasgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
    buldurmaya çalışın.
    **  "random modülü" için "python random" şeklinde arama yapın.
    **  100 üzerinden puanlama yapın. Her soru 20 puan.
    **  Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı
        üzerinden hesaplansın.
'''

import random

x = random.randint(1,100)

print("***** SAYI TAHMİN OYUNUNA HOŞGELDİNİZ *****")

hak = int(input("Kaç canla oynamak istersin: "))
puanlama = 100/hak

i = 0
score = 100
while i < hak:
    a = int(input("Tahmin et: "))
    
    if i + 1 == hak:
        print("Hakkınız bitti!")
        print(f"Sayı {x} idi :( ")
        print("Puanınız 0")
        break
    if a == x:
        print(f"Tebrikler, sayıyı {i+1}. denemede buldunuz!")
        print(f"Puanınız {score:1.4}")
        break
    elif a < x:
        print("Yukarı!!")
    elif a > x:
        print("Aşağı!!")   
    i += 1
    score -= puanlama
    
