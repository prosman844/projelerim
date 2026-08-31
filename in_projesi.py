kullanici_adlari = ["osman", "ilyas", "nour"]
secilen_kullanici_adi = input("kullanıcı adı giriniz: ")
while True:
    if secilen_kullanici_adi in kullanici_adlari:
        print("hoş geldin")
        break
    else:
        print("böyle bir kullanıcı yok")

    secilen_kullanici_harfi = input("bir harf giriniz: ")

    for i in range(len(kullanici_adlari)):
        var_yada_yok = secilen_kullanici_harfi in kullanici_adlari[i]

        if var_yada_yok:
            print("bu harf, bir kullanıcının isminde geçiyor")
            secilen_kullanici_adi = input("tekrar kullanıcı adı giriniz: ")
            break
        elif i == 2 and not var_yada_yok:
            print("bu bir kullanıcının adında geçmiyor")
            secilen_kullanici_adi = input("tekrar kullanıcı adı giriniz: ")
