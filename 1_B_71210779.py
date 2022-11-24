print("~"*10, "/('v')", "~"*10)
print("PROGRAM PENGHITUNG VOLUME BANGUN RUANG")
print("~"*10, "\('v')/", "~"*10)
print()
print("Pilihlah salah satu bangun ruang yang ingin dihitung volumenya:")
print("1. Limas")
print("2. Bola")
print("3. Prisma")
print("4. Kerucut")
print()
pilihan = int(input('Masukkan pilihan anda: '))
if pilihan == 1:
    alas = int(input('Masukkan panjang sisi alas limas: '))
    tinggi = int(input('Masukkan tinggi limas: '))
    penjumlahan = (1/3) * tinggi * alas**2
    print('Volume limas tersebut adalah ', penjumlahan)

elif pilihan == 2:
    panjangjari = int(input('Masukkan panjang jari-jari bola: '))
    volumebola = (4/3)* 3.14 * panjangjari**3
    print('Volume bola tersebut adalah ', volumebola)

elif pilihan == 3:
    print('Pilihlah salah satu dari pilihan di bawah')
    print('1. Prisma Segitiga\n2. Prisma Segiempat\n3. Prisma Segilima')
    inputan = int(input('Tentukan pilihan Anda: '))
    if inputan == 1:
        alas = int(input('Masukkan panjang sisi alas prisma: '))
        tinggialasprisma = int(input('Masukkan tinggi alas prisma: '))
        tinggiprisma = int(input('Masukkan tinggi prisma segitiga: '))
        rumus = (1/2)* alas * tinggialasprisma * tinggiprisma
        print('Volume prisma segitiga tersebut adalah ', rumus)

    elif inputan == 2:
        sisialasprisma = int(input('Masukkan panjang sisi alas prisma: '))
        tinggialasprisma = int(input('Masukkan tinggi alas prisma: '))
        tinggiprisma = int(input('Masukkan tinggi prisma segitiga: '))
        rumus = sisialasprisma * tinggialasprisma * tinggiprisma
        print('Volume prisma segitiga tersebut adalah ', rumus)
    
    elif inputan == 3:
        sisialasprisma = int(input('Masukkan panjang sisi alas prisma: '))
        tinggialasprisma = int(input('Masukkan tinggi alas prisma: '))
        tinggiprisma = int(input('Masukkan tinggi prisma segitiga: '))
        rumus = 2.5*sisialasprisma * tinggialasprisma*tinggiprisma
        print('Volume prisma segitiga tersebut adalah ', rumus)
    else:
        print('Prisma yang Anda cari belum tersedia di Kalkulator ini')

elif pilihan == 4:
    jarikerucut = int(input('Masukkan jari-jari kerucut: '))
    tinggikerucut = int(input('Masukkan tinggi kerucut: '))
    rumus = round((1/3)*3.14*(jarikerucut**2)*tinggikerucut, ndigits=1)
    print('Volume kerucut tersebut adalah ', rumus)
else:
    print('nomor tidak terdaftar dalam menu pilihan\nUlangi program dan pilih nomor 1 sampai 4')
