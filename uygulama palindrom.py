print("Palindrom, tersten okunuşu da aynı olan cümle, sözcük ve sayılara denilmektedir.")
while True:
    a=input("palindrom olduğunu düşündüğün bir sayı, kelime ya da cümle gir bir kontrol edeyim: ")
    print(a,"kelimesinin tersi",a[::-1])
    if a == a[::-1]:
        print("evet, bu bir palindrom")
    else:
        print("tekrar dene")
        print("basit bir örnek vereyim belki yardımcı olur: \nAl kazık çak karaya kayarak kaç kızaklA.\neheheh fazla basit bir örnek oldu sanki\n\n")
