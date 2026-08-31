def ekok():
    dongudur2 = False
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
    i = 1
    j = 1
    while True:
        for j in range (1,9999999):
            if sayi * i == sayi2 * j:
                print(sayi * i)
                dongudur2 = True
                break
        if dongudur2:
                break
        i += 1

ekok()
