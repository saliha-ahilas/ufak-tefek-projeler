def asal(a):
    for i in range(2,a):
        if a%i==0:
            return False
        else:
            return True
while True:
    a=int(input("asal mı değil mi öğrenmek istiyosan bi sayı gir, sen bilirsin: "))
    if (a==0):
        print("bunu sormaya utanmıyor musun tabi ki asal değil, başka sor")
    elif (a==1):
        print("bunu sormaya utanmıyor musun tabi ki asal değil, başka sor")
    elif a==2:
            print("2 en küçük ve aynı zamanda tekk çift asal sayıdır. Bunu bilmeyen de ne bileyim yani")
    elif asal(a):
        print("asal evet")
    else:
        print("sıradakiiii")
