import time
hesap = 8080
while True:
    print("""
    1. para çekme
    2. para yatırma
    3. bakiye bilgisi
    4. çıkış
    """)
    while True:
        try:
            secim = int(input("seçiminizi giriniz: "))
            break
        except:
            print("Lütfen sayı değer giriniz")

    if secim == 1:
        döngü = True
        while döngü:
            try:
                çekme_miktar = input("çekeceğiniz miktarı giriniz (iptal için x yazınız): ")
                if çekme_miktar == "x":
                    döngü = False
                    break
                çekme_miktar = int(çekme_miktar)
                if çekme_miktar > hesap:
                    print("hesabınızda yeterli bakiye yok")
                    continue

                elif çekme_miktar <= 0:
                    print("negatif veya 0 giremezsin!")
                    continue

                hesap -= çekme_miktar
                break

            except ValueError:
                print("Lütfen sayı değer giriniz (yada x yazınız)")

    elif secim == 2:
        döngü = True
        while True:
            try:
                yatırma_miktar = input("yatıracağınız miktarını giriniz (iptal için x yazınız): ")
                if yatırma_miktar == "x":
                    döngü = False
                    break
                yatırma_miktar = int(yatırma_miktar)
                if yatırma_miktar <= 0:
                    print("negatif veya 0 giremezsin!")
                hesap += yatırma_miktar
                break
            except ValueError:
                print("Lütfen sayı değer giriniz (yada x yazınız)")


    elif secim == 3:
        print("bakiyeniz %s"%hesap)
        continue

    elif secim == 4:
        print("çıkış yapılıyor...")
        time.sleep(4)
        print("çıkış yapıldı")
        break

    else:
        print("seçiminiz 1-4 arasında olmalı")
        continue
