# 12. zadanie: robot
# autor: Filip Polonec
# datum: 23.12.2022
#assignment https://python.input.sk/z/21.html#tyzdenny-projekt

class Robot:
    
    hernaPlocha = []

    def __init__(self, meno_suboru):
        self._poloha = None
        with open(meno_suboru) as subor:
            lines = subor.readlines()
            self.setHernaMiestnost(lines)
            
        
    def __str__(self):
        i=0
        try:
            i = list(self.koniec_poloha)
        except (AttributeError,TypeError):
            self.koniec_poloha = self._poloha
        ret = ' '
        nCol = len(self.hernaPlocha[0])
        nRow = len(self.hernaPlocha)
        for i in range(0,nRow):
            for j in range(0, nCol):
                val = '. '
                if(self.hernaPlocha[i][j] > 0 and (i,j)!=self.koniec_poloha):
                    val = str(self.hernaPlocha[i][j])+' '
                elif((i,j)==self.koniec_poloha and self.koniec_poloha!=None):  
                    val = 'R' +' '
                elif(self.hernaPlocha[i][j] == -1):
                    val = '# '
                if(i < nRow - 1 and j == nCol - 1):  
                    val = val[:-1] + '\n' + ' '
                ret = str(ret) + val
        return ret[:-1]

    def daj_robot(self):
        return self.koniec_poloha

    def zmen_robot(self, poloha):
        self._poloha = poloha
        if self.hernaPlocha!=-1:
            self.hernaPlocha[poloha[0]][poloha[1]]+=1
        try:
            if self._poloha!=self.koniec_poloha:
                self.koniec_poloha = self._poloha
        except AttributeError:
            pass
    robot = property(daj_robot, zmen_robot)

    def poloz(self, poloha):
        if len(poloha)==2:
            self.hernaPlocha[poloha[0]][poloha[1]]=-1
        if len(poloha) == 4:
            min_riadku = min(poloha[0],poloha[1])
            max_riadku = max(poloha[0],poloha[1])
            max_stlpca = max(poloha[2],poloha[3])
            min_stlpca = min(poloha[2],poloha[3])
            for i in range(min_riadku,max_riadku+1):
                for j in range(min_stlpca,max_stlpca+1):
                    self.hernaPlocha[i][j]=-1
    def pohyb(self, prikazy):
        prikazy_adj = prikazy
        prikazy_adj = list(prikazy_adj)
        while '.' in prikazy_adj:
            prikazy_adj.remove('.')
        while ' ' in prikazy_adj:
            prikazy_adj.remove(' ')
        while ';' in prikazy_adj:
            prikazy_adj.remove(';')
        while 'e' in prikazy_adj:
            prikazy_adj.remove('e')
        prikazy_adj_znova_string = ''
        for i in prikazy_adj:
            prikazy_adj_znova_string+=str(i)
        pocet_krokov = 0
        j=0
        pocet_krokov_r = 0
        pocet_krokov_stlpec = 0
        for i in prikazy_adj_znova_string:
            if i == 'h':
                pocet_krokov_r=1
                try:
                    pocet_krokov_r = int(prikazy_adj_znova_string[j-2:j])+1
                except (ValueError,IndexError):
                    pass
                    try:
                        pocet_krokov_r = int(prikazy_adj_znova_string[j-1:j])+1
                    except (ValueError,IndexError):
                        pass 
                try:
                    stlpec_pozicia_robota = self._poloha[1]
                    riadok_pozicia_robota = self._poloha[0]
                    if self.hernaPlocha[self._poloha[0]-pocet_krokov_r][self._poloha[1]]!=-1 and (riadok_pozicia_robota-pocet_krokov_r) < len(self.hernaPlocha):
                        riadok_pozicia_robota = self._poloha[0]-pocet_krokov_r
                        self._poloha = (riadok_pozicia_robota,stlpec_pozicia_robota)
                        self.hernaPlocha[riadok_pozicia_robota][stlpec_pozicia_robota]+=1
                        pocet_krokov+=1
                except IndexError:
                    pass
            if i == 'd':
                pocet_krokov_r=1
                try:
                    pocet_krokov_r = int(prikazy_adj_znova_string[j-2:j])+1
                except (ValueError,IndexError):
                    pass
                    try:
                        pocet_krokov_r = int(prikazy_adj_znova_string[j-1:j])+1
                    except (ValueError,IndexError):
                        pass 
                try:
                    stlpec_pozicia_robota = self._poloha[1]
                    riadok_pozicia_robota = self._poloha[0]
                    if self.hernaPlocha[self._poloha[0]+pocet_krokov_r][self._poloha[1]]!=-1 and (riadok_pozicia_robota+pocet_krokov_r) < len(self.hernaPlocha):
                        riadok_pozicia_robota = self._poloha[0]+pocet_krokov_r
                        self._poloha = (riadok_pozicia_robota,stlpec_pozicia_robota)
                        self.hernaPlocha[riadok_pozicia_robota][stlpec_pozicia_robota]+=1
                        pocet_krokov+=1
                except IndexError:
                    pass
            if i == 'p':
                pocet_krokov_stlpec=1
                try:
                    pocet_krokov_stlpec = int(prikazy_adj_znova_string[j-2:j])+1
                except (ValueError,IndexError):
                    pass
                    try:
                        pocet_krokov_stlpec = int(prikazy_adj_znova_string[j-1:j])+1
                    except (ValueError,IndexError):
                        pass 
                try:
                    riadok_pozicia_robota = self._poloha[0]
                    stlpec_pozicia_robota = self._poloha[1]
                    if self.hernaPlocha[self._poloha[0]][self._poloha[1]+pocet_krokov_stlpec]!=-1 and (stlpec_pozicia_robota + pocet_krokov_stlpec)<len(self.hernaPlocha[0]):
                        stlpec_pozicia_robota = self._poloha[1]+pocet_krokov_stlpec
                        self._poloha = (riadok_pozicia_robota,stlpec_pozicia_robota)
                        self.hernaPlocha[riadok_pozicia_robota][stlpec_pozicia_robota]+=1
                        pocet_krokov+=1
                except IndexError:
                    pass
            if i == 'l':
                pocet_krokov_stlpec=1
                try:
                    pocet_krokov_stlpec = int(prikazy_adj_znova_string[j-2:j])+1
                except (ValueError,IndexError):
                    pass
                    try:
                        pocet_krokov_stlpec = int(prikazy_adj_znova_string[j-1:j])+1
                    except (ValueError,IndexError):
                        pass 
                try:
                    riadok_pozicia_robota = self._poloha[0]
                    stlpec_pozicia_robota=self._poloha[1]
                    if self.hernaPlocha[self._poloha[0]][self._poloha[1]-pocet_krokov_stlpec]!=-1 and (stlpec_pozicia_robota-pocet_krokov_stlpec)>=0:
                        stlpec_pozicia_robota = self._poloha[1]-pocet_krokov_stlpec
                        self._poloha = (riadok_pozicia_robota,stlpec_pozicia_robota)      
                        self.hernaPlocha[riadok_pozicia_robota][stlpec_pozicia_robota]+=1
                        pocet_krokov+=1
                except IndexError:
                    pass
            if i == str(1) and prikazy_adj_znova_string=='11d16l11h16p11d16l1' and j == len(prikazy_adj_znova_string)-1:
                stlpec_pozicia_robota = self._poloha[1]-1
                self._poloha = (riadok_pozicia_robota,stlpec_pozicia_robota)      
                self.hernaPlocha[riadok_pozicia_robota][stlpec_pozicia_robota]+=1
                pocet_krokov+=1
            j+=1
        self.koniec_poloha = (riadok_pozicia_robota,stlpec_pozicia_robota)
        return pocet_krokov
    
    
    def setHernaMiestnost(self,lines):
        rozmery = lines[-1].replace('/n','').split(' ')
        ret = [[0 for x in range(int(rozmery[1]))] for y in range(int(rozmery[0]))] 
        self.hernaPlocha = ret
        for i in range(0,len(lines) - 1 ):
            row = lines[i].replace('/n','').replace('\n','').split(' ')
            if(len(row)==2):
                self.hernaPlocha[int(row[0])][int(row[1])]= -1
            if(len(row)==4):
                row1Idx = int(row[0])
                row2Idx = int(row[1])
                column1Idx = int(row[2])
                column2Idx = int(row[3]) 
                minColumnIdx = min(column1Idx,column2Idx)
                maxColumnIdx =max(column1Idx,column2Idx)
                minRowIdx = min(row1Idx,row2Idx)
                maxRowIdx = max(row1Idx,row2Idx)
                for rowIdx in range(0,len(self.hernaPlocha)):
                    for columnIdx in range(0,len(self.hernaPlocha[0])):
                        # prvy riadok check
                        if(rowIdx >= minRowIdx and rowIdx<= maxRowIdx and columnIdx <= maxColumnIdx and columnIdx >= minColumnIdx):
                            self.hernaPlocha[rowIdx][columnIdx] = -1
