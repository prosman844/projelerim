import time
def sayibolenleri():
    while True:
        try:
            sayi = int(input("sayı giriniz: "))
            if sayi <= 0:
                print("sayınız 0 veya daha küçük olamaz")
                continue
            if sayi > 0:
                break
        except ValueError:
            print("sayı değer giriniz")
            continue
    print("analiz ediliyor...")
    time.sleep(0.7)
    print("sonuçlar bulundu!")
    time.sleep(0.7)
    for i in range(1, sayi + 1):
        if sayi % i == 0:
            print(i)
sayibolenleri()
