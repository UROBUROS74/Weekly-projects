# 2. zadanie: spirala
# autor: Filip Polonec
# datum: 7.10.2022
# for drawing the spiral please enter the three numbers in this romat
# 20 3 2950 they must be separated with a one space and have no space at
# the end or at the beginning. For more info you can check out this page
# with assignment
import tkinter 

ahoj = input("zadaj")
i = 0
štartová_dĺžka= " "
inkrement = " "
súčet_dĺžok = " "
for element in ahoj:
    if element ==" ":
        i+=1
    if i==0:
        štartová_dĺžka = štartová_dĺžka+element
    if i == 1 and element!=" ":
        inkrement=inkrement+element
    if i ==2 and element!=" ":
        súčet_dĺžok = súčet_dĺžok+element
štartová_dĺžka=int(štartová_dĺžka)
inkrement=int(inkrement)
súčet_dĺžok=int(súčet_dĺžok)
posun = štartová_dĺžka/((2)**(1/2))
x = 200
y = 150
canvas = tkinter.Canvas(width=400,height=400)
canvas.pack()
sucet = 0
while True:
    if sucet+štartová_dĺžka<súčet_dĺžok:
        canvas.create_line(x,y,x-posun,y-posun)
        y-=posun
        x-=posun
        sucet+=štartová_dĺžka
        štartová_dĺžka=štartová_dĺžka + inkrement
        posun = štartová_dĺžka/((2)**(1/2))
    elif sucet+štartová_dĺžka>súčet_dĺžok:
        posun = abs(sucet-súčet_dĺžok)/((2)**(1/2))
        canvas.create_line(x,y,x-posun,y-posun)
        break
    if sucet+štartová_dĺžka<súčet_dĺžok:
        canvas.create_line(x,y,x-posun,y+posun)
        sucet+=štartová_dĺžka
        x-=posun
        y+=posun
        štartová_dĺžka=štartová_dĺžka + inkrement
        posun = štartová_dĺžka/((2)**(1/2))
    elif sucet+štartová_dĺžka>súčet_dĺžok:
        posun = abs(sucet-súčet_dĺžok)/((2)**(1/2))
        canvas.create_line(x,y,x-posun,y+posun)
        break
    if sucet+štartová_dĺžka<súčet_dĺžok:
        canvas.create_line(x,y,x+posun,y+posun)
        sucet+=štartová_dĺžka
        y+=posun
        x+=posun
        štartová_dĺžka=štartová_dĺžka + inkrement
        posun = štartová_dĺžka/((2)**(1/2))
    elif sucet+štartová_dĺžka>súčet_dĺžok:
        posun = abs(sucet-súčet_dĺžok)/((2)**(1/2))
        canvas.create_line(x,y,x+posun,y+posun)
        break
    if sucet+štartová_dĺžka<súčet_dĺžok:
        canvas.create_line(x,y,x+posun,y-posun)
        sucet+=štartová_dĺžka
        x+=posun
        y-=posun
        štartová_dĺžka=štartová_dĺžka+inkrement
        posun = štartová_dĺžka/((2)**(1/2))
    elif sucet+štartová_dĺžka>súčet_dĺžok:
        posun = abs(sucet-súčet_dĺžok)/((2)**(1/2))
        canvas.create_line(x,y,x+posun,y-posun)
        break
tkinter.mainloop()
