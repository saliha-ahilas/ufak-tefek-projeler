import random
sayi=random.randint(1,100)
deneme_sayisi=0
while True:
    try:
        a=int(input("bir ile yüz arasında bir sayı seçiniz"))
        deneme_sayisi+=1
        if a==sayi:
            print("bu seferlik bildin. ama bir dahakine daha zor olacak.")
            break
        elif a<sayi:
            print("çııık")
        elif a>sayi:
            print("iiinn")
        
    except ValueError:
        print("düzgün bir sayı gir be")
print(deneme_sayisi, "denemede  bildin")
