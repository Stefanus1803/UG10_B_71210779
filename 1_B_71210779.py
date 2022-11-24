print("Pilihlah salah satu bangun ruang yang ingin dihitung volumenya:")
print("1. Limas")
print("2. Bola")
print("3. Prisma")
print("4. Kerucut")
print()
pilihan = int(input("Masukkan pilihan Anda: "))
if pilihan == 1:
    alas = float(input("Masukkan panjang sisi alas limas: "))
    tinggi = float(input("Masukkan tinggi limas: "))
    penjumlahan = 1/3 * alas * tinggi
    print("Volume limas tersebut adalah: ", penjumlahan)

elif pilihan == 2:
    panjangjari = int(input("Masukkan panjang jari-jari bola: "))
    rumusbola = (4/3) * 3.14 * panjangjari ** 3
    print("Volume bola tersebut adalah ",rumusbola)

elif pilihan == 3:
    print("Pilihlah salah satu dari pilihan di bawah:")
    print("1. Prisma Segitiga")
    print("2. Prisma Segiempat")
    print("3. Prisma Segilima")
    inputan = int(input("Tentukan pilihan Anda: "))
    if inputan == 1:
        sisi = int(input("Masukan panjang sisi alas prisma: "))
        alas = int(input("Masukkan tinggi alas prisma: "))
        tinggi = int(input("Masukkan tinggi prisma segitiga: "))
        rumus = 1/2 * alas * tinggi * tinggi
        print("Volume prisma segitiga tersebut adalah ", rumus)
    elif inputan == 2:
        sisi = int(input("Masukan panjang sisi alas prisma: "))
        alas = int(input("Masukkan tinggi alas prisma: "))
        prisma = int(input("Masukkan tinggi prisma segiempat: "))
    else:
        sisi = int(input("Masukan panjang sisi alas prisma: "))
        alas = int(input("Masukkan tinggi alas prisma: "))
        prisma = int(input("Masukkan tinggi prisma segilima: "))

else:
    print()
    
