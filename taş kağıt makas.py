import random
Liste=["taş","kağıt","makas"]

while True:
    try:
        pc=random.choice(Liste)
        insan=input("taş mı,kağıt mı,makas mı? \n")
        if insan in Liste:
            print("benim seçimim ise",pc)
            if pc==insan:
                print("berabere kaldık, hadi bir el daha oynayalım\n")
            elif pc=="taş":
                if insan=="kağıt":
                    print("bu sefer şanslıydın, bir el daha oynayalım\n")
                elif insan=="makas":
                    print("ben kazandım, bir el daha oynayalım belki bu sefer şansın yaver gider\n")
            elif pc=="kağıt":
                if insan=="makas":
                    print("bu sefer şanslıydın, bir el daha oynayalım\n")
                elif insan=="taş":
                    print("ben kazandım, bir el daha oynayalım belki bu sefer şansın yaver gider\n")
            elif pc=="makas":
                if insan=="taş":
                    print("bu sefer şanslıydın, bir el daha oynayalım\n")
                elif insan=="kağıt":
                    print("ben kazandım, bir el daha oynayalım belki bu sefer şansın yaver gider\n")
        else:
            print("mızıkçılık yapma, geçerli bir değer gir ki oynayabilelim\n")
    except ValueError:
        print("mızıkçılık yapma, geçerli bir değer gir ki oynayabilelim\n")
        
