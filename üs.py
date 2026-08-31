def us(taban,kuvvet):
    toplam = 1
    for i in range(1,kuvvet + 1):
        toplam *= taban
    print(toplam)
taban = int(input("sayı giriniz: "))
kuvvet = int(input("bir sayı daha giriniz: "))
us(taban,kuvvet)
