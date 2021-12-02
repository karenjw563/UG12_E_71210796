max = int(input("Masukkan Angka : "));
limit=max;
for star in range (0, max):
    for pola in range (-2, limit+1):
        print(" ", end="")

    for shape in range (0, star+1):
        print("* ", end="")
    limit-=1
    print("")

limit=max;
for star in range (1, max):
    for pola in range (-4, star):
        print(" ", end="")

    for shape in range (1, limit):
        print("* ", end="")
    limit-=1
    print("")