AwalDeret = int(input("Masukkan awal deret: "))
AkhirDeret = int(input("Masukkan akhir deret: "))

K = []

if (AwalDeret + 1) % 2 == 0:
    for i in range (AwalDeret+1, AkhirDeret, 2) :
        if i % 5 == 0 or i % 9 == 0 : continue
        print (i, end = " ")

else:
    for i in range (AwalDeret, AkhirDeret, 2):
        if i % 5 == 0 or i % 9 == 0 : continue
        print (i, end = " ")