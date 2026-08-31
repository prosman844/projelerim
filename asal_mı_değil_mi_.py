sayi = int(input("sayı giriniz: "))
asal_degil = False

if sayi < 2:
    print("asal değil")
else:
    for i in range(2, sayi):
        if sayi % i == 0:
            asal_degil = True
            break

    if asal_degil:
        print("bu sayı asal değil")
    else:
        print("bu sayı asal")
