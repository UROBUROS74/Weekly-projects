# 3. zadanie: kalendár
# autor: Filip Polonec
# datum: 17.10.2022
# check out the assignment here https://python.input.sk/z/06.html#tyzdenny-projekt

def pocet_dni_v_mesiaci(mesiac,priestupny=False):
    if mesiac[:3]== "jan":
        return 31
    elif mesiac[:3]== "feb":
        if priestupny == True:
            return 29
        else:
            return 28
    elif mesiac[:3]== "mar":
        return 31
    elif mesiac[:3]== "apr":
        return 30
    elif mesiac[:3]== "maj":
        return 31
    elif mesiac[:3]== "jun":
        return 30
    elif mesiac[:3]== "jul":
        return 31
    elif mesiac[:3]== "aug":
        return 31
    elif mesiac[:3]== "sep":
        return 30
    elif mesiac[:3]== "okt":
        return 31
    elif mesiac[:3]== "nov":
        return 30
    elif mesiac[:3]== "dec":
        return 31
    
    
# podla datumu jedna spocitaj pre n-1 rokov, cize napr pre zadany mesiac februar to spocitaj po datum2.(rok-1)   
    
def pocet_dni_medzi(datum1,datum2):
    datum_2rok = int(datum2[-4:])
    datum_1rok = int(datum1[-4:])
    m=""
    n=""
    suma = 0
    prve_tri_pismena1 = datum1[:3] 
    vsetky_mesiace = "janfebmaraprmajjunjulaugsepoktnovdec"
    p1 = vsetky_mesiace.find(prve_tri_pismena1)
    dlzka=len(vsetky_mesiace)
    dlzka_vybrane_mesiace = len(vsetky_mesiace[p1:])
    vybrane_mesiace = vsetky_mesiace[p1:]
    k=3
    #ak pocitame dni v ramci jedneho rok
        
    if datum_1rok!=datum_2rok:
        #vypcoet prveho roku ked sa nerovnaju
        for i in range(0,dlzka_vybrane_mesiace,3):
            m = vybrane_mesiace[i:k]
            suma+=pocet_dni_v_mesiaci(mesiac=m,priestupny = datum_1rok%4==0)
            k+=3
    
        # vypocet druheho roku ked sa nerovnaju
        prve_tri_pismena2 = datum2[:3]
        p2= vsetky_mesiace.find(prve_tri_pismena2) #pozicia 2 pre konecny datum
        k = 3
        dlzka_vybrane_mesiace2 = len(vsetky_mesiace[0:p2])
        vybrane_mesiace2 = vsetky_mesiace[0:p2]
        for i in range(0,dlzka_vybrane_mesiace2,3):
            n = vybrane_mesiace2[i:k]
            suma+=pocet_dni_v_mesiaci(mesiac=n,priestupny = datum_2rok%4==0)
            k+=3
    if datum_1rok==datum_2rok:
        prvy_mesiac_poz = vsetky_mesiace.find(datum1[:3])
        posledny_mesiac_poz = vsetky_mesiace.find(datum2[:3])
        mesiace = vsetky_mesiace[prvy_mesiac_poz:posledny_mesiac_poz]
        dlzka_pre = len(mesiace)
        x = ""
        k=3
        for i in range(0,dlzka_pre,3):
            x = mesiace[i:k]
            suma+=pocet_dni_v_mesiaci(mesiac=x,priestupny = datum_2rok%4==0)
            k+=3
    for i in range(datum_1rok+1,datum_2rok):
        if i%4==0:
            suma+=366
        else:
            suma+=365
    return suma

def den_v_tyzdni(datum):
    bodka_pozicia = datum.find(".")+1
    mesiac_rok = datum[bodka_pozicia:]
    rok = int(datum[-4:])
    pocet_dni_celkovo =  pocet_dni_medzi('januar.1901',mesiac_rok)
    pocet = pocet_dni_celkovo + int(datum[:bodka_pozicia-1])
    if pocet<0:
        pocet = int(datum[:bodka_pozicia-1])
    if pocet%7==1:
        return "uto"
    if pocet%7==2:
        return "str"
    if pocet%7 == 3:
        return "stv"
    if pocet%7==4:
        return "pia"
    if pocet%7==5:
        return "sob"
    if pocet%7==6:
        return "ned"
    if pocet%7==0:
        return "pon"


def kalendar(datum):
    dni = "pon uto str stv pia sob ned"
    dlzka_riadka = len(dni)
    rok = int(datum[-4:])
    den =den_v_tyzdni(str(1)+"."+datum)
    pozicia_dna = dni.find(den)+1
    for i in dni:
        print(i,end="")
    print()
    print(" "*pozicia_dna,end="")
    print(" ",end="")
    rozdielova_dlzka = dlzka_riadka-len(" "*pozicia_dna)
    j=1
    pocet_dni_v_m = pocet_dni_v_mesiaci(datum[:3],rok%4==0)
    pocet_znakov = 0
    for k in range(1,6):
        for i in range(0,rozdielova_dlzka,4):
            if j ==pocet_dni_v_m:
                break
            if j<10:
                if j == 9:  
                    print(j,end="")
                    print(" ",end="")
                    print(" ",end="")
                    pocet_znakov+=3
                else:
                    print(j,end="")
                    print(" ",end="")
                    print(" ",end="")
                    print(" ",end="")
                    pocet_znakov+=4
            if j>9:
                print(j,end="")
                print(" ",end="")
                print(" ",end="")
                pocet_znakov+=3
            j+=1
        if j!=pocet_dni_v_m:
            print()
            pocet_znakov = 0
        if j<10:
            print(" ",end="")
            print(" ",end="")
            pocet_znakov+=2
        if j>=10 and j!=pocet_dni_v_m:
            print(" ",end="")
            pocet_znakov+=1
        else:
            pocet_znakov+=1
        rozdielova_dlzka=dlzka_riadka
    if pocet_znakov+4>=dlzka_riadka:
        print()
        print(" ",end="")
    print(j,end="")
    j+=1
    if pocet_dni_v_m>=j:
        print(" ",end="")
        print(" ",end="")
        print(j,end="")
