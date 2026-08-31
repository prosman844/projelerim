dongu = True
while dongu:
    try:
        sayi = int(input("sayı gir: "))
        dongu = False
    except ValueError:
        print("sayi giriniz!")
def tek_çift(sayi):
    toplam = 0
    if sayi % 2 == 0:
        print(sayi)
    else:
        for i in range(sayi):
            toplam += i
        print(toplam)
tek_çift(sayi)
