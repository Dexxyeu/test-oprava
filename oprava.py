zbozi = ["jablko", "hruška", "švestka", "meloun", "pomeranč"]
kosik =[]

def kupovani(koupe):
    for x in range(len(koupe)):
        print(f"{x+1}: {koupe[x]}")
kupovani(zbozi)
while(True):
    kosik_plus = input("Zadejte ovoce kterou chcete přidat:")
    
    if kosik_plus == "jablko":
        kosik.append(kosik_plus)
        kosik.remove("jablko")
    
    elif kosik_plus == "hruška":
        kosik.append(kosik_plus)
        kosik.remove("hruška")

    elif kosik_plus == "švestka":
        kosik.append(kosik_plus)
        kosik.remove("švestka")

    elif kosik_plus == "meloun":
        kosik.append(kosik_plus)
        kosik.remove("meloun")

    elif kosik_plus == "pomeranč":
        kosik.append(kosik_plus)
        kosik.remove("pomeranč")

    elif kosik_plus == "1":
        kosik.append(kosik_plus)
        kosik.remove("1")

    elif kosik_plus == "2":
        kosik.append(kosik_plus)
        kosik.remove("2")

    elif kosik_plus == "3":
        kosik.append(kosik_plus)
        kosik.remove("3")

    elif kosik_plus == "4":
        kosik.append(kosik_plus)
        kosik.remove("4")

    elif kosik_plus == "stop":
        kosik.append(kosik_plus)
        kosik.remove("5")

    else:
        print("proč to děláš")

    kupovani(zbozi)
    print(kosik)
