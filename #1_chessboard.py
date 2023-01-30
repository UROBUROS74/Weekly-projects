# 1. zadanie: retazec
# autor: Filip Polonec
# datum: 25.9. 2022

retazec = input("zadaj retazec: ")
dlzka = 0
for i in retazec:
    dlzka+=1
print(f"dlzka = {dlzka}")
prevrat = ""
for i in reversed(retazec):
    prevrat+=i
print(f"prevrat = {prevrat}")

for i in range(0,dlzka):
    for i in retazec:
        print(i,end=" ")
        print("*",end = " ")
    print()
    for j in retazec:
        print("*",end=" ")
        print(j,end = " ")
    print()

