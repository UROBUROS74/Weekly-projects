# 5. zadanie: najcastejsie
# autor: Filip Polonec
# datum: 2.11.2022
#assignment https://python.input.sk/z/10.html#tyzdenny-projekt

tab = []

def citaj(meno_suboru):
    pomoc=[]
    subor = open(meno_suboru,"r",encoding="UTF-8")
    j=0
    text=""
    for riadok in subor:
        if riadok == '\n' or riadok =='\n\n' or riadok=='  \n':
            pass
        else:
        
            if riadok[-1]=='\n' or riadok[-1]=='\n\n':
                text = text + riadok[:-1]
                text = text+ " "
            else:
                text = text + riadok
                text = text+ " " 
    text = text.split(" ")
    pomoc.append(text[0:])
    # vytvorenie unikatneho listu pre pocitanie vyskytov slov
    result = []
    for i in pomoc[0]:
        if i not in result and result!='\n' or result!='\n':
            result.append(i)
    j=0
    for i in pomoc[0]:
        if (result[j],pomoc[0].count(result[j])) not in tab:
            if result[j]!='':
                tab.append((result[j],pomoc[0].count(result[j])))
        if i not in result and result!='\n' or result!='\n':
            j+=1
        if j>=len(result):
            break
    subor.close()
    if tab[-1][0]=='':
        tab.pop()
    else:
        pass

def pocet_vyskytov(slovo):
    j=0
    for i in tab:
        if i[0]==slovo:
            j=i[1]
    return j



def najcastejsie():
    maximum = []
    for i in tab:
        if i[0]!='':
            maximum.append(i[1])
    najcastejsie_int = max(maximum)
    najcastejsie_tuple = ()
    for i in tab:
        if i[1] == najcastejsie_int:
            najcastejsie_tuple = najcastejsie_tuple+(i[0],)
    return najcastejsie_tuple


def s_poctom(n):
    slova = ()
    for i in tab:
        if i[1]==n:
            slova = slova + (i[0],)
    return slova

def najdlhsie():
    najdlhsie_slova = ()
    dlzky =[]
    for i in tab:
        dlzky.append(len(i[0]))
    max_dlzka = max(dlzky)
    for i in tab:
        if len(i[0])==max_dlzka:
            najdlhsie_slova = najdlhsie_slova + (i[0],)
    return najdlhsie_slova

def najkratsie():
    najkratsie_slova = ()
    dlzocky =[]
    for i in tab:
        dlzocky.append(len(i[0]))
    min_dlzka = min(dlzocky)
    for i in tab:
        if len(i[0])==min_dlzka:
            najkratsie_slova = najkratsie_slova + (i[0],)
    return najkratsie_slova

def s_dlzkou(n):
    urcite_slova = ()
    for i in tab:
        if len(i[0])==n:
            urcite_slova = urcite_slova + (i[0],)
    return urcite_slova
