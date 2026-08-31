import random

butonlar = ["kırmızı", "mavi", "yeşil"]

while True:
    dogru_buton = random.choice(butonlar)
    secilen_buton = input("butonlardan birini seç (kırmızı, mavi, yeşil): ").strip().lower()

    if secilen_buton not in butonlar:
        print("geçersiz")
        continue
    else:
        if secilen_buton == dogru_buton:
            print("doğru bildin!")
        else:
            print("yanlış bildin")

    dongu = input("bir daha denemek ister misin? (E/H): ").strip().upper()
    if dongu not in ("E", "H"):
        print("geçersiz")
        continue

    if dongu == "H":
        print("görüşürüz")
        break
    else:
        print("öyle ise yeniden oynayalım")
