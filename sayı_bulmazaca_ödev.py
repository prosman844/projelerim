import random

sayi = random.randint(1, 100)
hak = 5

for deneme_sayisi in range(1, hak + 1):
    alinan_sayi = int(input("Sayı giriniz: "))

    if alinan_sayi == sayi:
        print(f"Doğru bildin! {deneme_sayisi}. denemede.")
        break
    elif alinan_sayi < sayi:
        if hak - deneme_sayisi != 0:
            print(f"Yanlış, sayı daha büyük. Kalan hakkın: {hak - deneme_sayisi}")
    else:
        if hak - deneme_sayisi != 0:
            print(f"Yanlış, sayı daha küçük. Kalan hakkın: {hak - deneme_sayisi}")

else:
    print(f"Maalesef kaybettin. Doğru sayı: {sayi}")
