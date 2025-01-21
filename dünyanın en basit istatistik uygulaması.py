L=[]
L1=[]
L2=[]
topla=0
print("dünyanın en basit istatistik uygulamasına hoş geldiniz")
while True:
    try:
        sayi=int(input("sayı giriniz(sonuçları görmek için x'e basınız): "))
        L.append(sayi)
        topla+=sayi
    except ValueError:
        break
L.sort()
print("listeniz: ",L )
print("girdiğiniz sayıların en küçüğü: ",min(L),)
print("girdiğiniz sayıların en büyüğü: ",max(L),)
print("girdiğiniz sayıların aritmetik ortalaması: ", topla/len(L))
if len(L)%2==1:
    a=int((len(L)+1)/2)
    print("girdiğiniz sayıların medyanı: ",L[a-1])
elif len(L)%2==0:
    b=int(len(L)/2)
    c=int((len(L)/2)+1)
    d=(L[b-1]+L[c-1])/2
    print("girdiğiniz sayıların medyanı: ",d)
for i in L:
    mod=L.count(i)
    L1.append(mod)
if len(set(L1))==1:
    print("girdiğiniz sayıların modu yok")
else:
    for i in L:
        if L.count(i)==max(L1) and i not in L2:
            L2.append(i)
    print("girdiğiniz sayıların modu: ",L2)
       

