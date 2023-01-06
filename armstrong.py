with open("numbers.txt","r") as file:
    liste=[]
    for line in file:
        srtipped=line.strip()
        liste.append(srtipped)

    asil=[]
    for eleman in liste:
        summ=0
        for sayi in eleman:
            if len(eleman)>1:
                summ+=int(sayi)**len(eleman)
            else:
                asil.append(eleman)
        if summ==int(eleman):
            asil.append(eleman)

    with open("sayilar.txt","w") as dosya:
        for karakter in asil:
            dosya.write(karakter)
            print(karakter)
            dosya.write("\n")
