dongu = True
while dongu:
    try:
        sayi = int(input("sayı giriniz: "))
        dongu = False
    except ValueError:
        print("sayı gir sayı metin değil")
        dongu = True
def fibonacci(sayi):
    onceki_sayi = 0
    fibonacci_sayi = 1
    for i in range(sayi):
        print(onceki_sayi)
        onceki_sayi, fibonacci_sayi = fibonacci_sayi, fibonacci_sayi + onceki_sayi


fibonacci(sayi)
# ssssssssss
