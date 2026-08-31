secilen_sayi = int(input("sayı giriniz: "))

for i in range(1, secilen_sayi + 1):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
