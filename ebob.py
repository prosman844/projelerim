def ebob():
    bolen_sayılar1 = []
    bolen_sayılar2 = []
    ebobsayiadaylari = []
    dongu = True
    while dongu:
        try:
            sayi = int(input("sayı gir: "))
            sayi2 = int(input("sayi gir: "))
            if sayi < 1 or sayi2 < 1:
                print("1 den küçük girmeyiniz!")
                continue
            dongu = False
        except ValueError:
            print("sayı değer giriniz!")
    for i in range (1 , sayi + 1):
        if sayi % i == 0:
            bolen_sayılar1.append(i)

    for i in range (1,sayi2 + 1):
        if sayi2 % i == 0:
            bolen_sayılar2.append(i)
    for k in bolen_sayılar1:
        for l in bolen_sayılar2:
            if k == l:
                ebobsayiadaylari.append(k)
    print(f"iki sayının ebobu: {ebobsayiadaylari[-1]}")
ebob()
