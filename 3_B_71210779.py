a = ""
print('~~ Selamat Datang di Program Pengurutan Bilangan ~~')
print("Tentukan pilihan Anda!!! [1/2]\n\n1. Ascending\n2. Descending\n")
pilihan = int(input('Masukkan pilihan yang Anda Inginkan: '))
if pilihan == 1:
    bilangan1 = int(input('Masukkan bilangan pertama : '))
    bilangan2 = int(input('Masukkan bilangan kedua : '))
    bilangan3 = int(input('Masukkan bilangan ketiga : '))
    bilangan4 = int(input('Masukkan bilangan keempat : '))
    ascending = [bilangan1, bilangan2, bilangan3, bilangan4]
    # print(''.join(sorted(ascending, reverse=True)))
    # b = sorted(ascending, reverse=True)
    # print("".join(b))
    # a += str(sorted(ascending, reverse=True))
    for x in sorted(ascending):
        a += str(f"{x} ")
    print("Urutan bilangan dari yang terkecil adalah",a)
elif pilihan == 2:
    bilangan1 = int(input('Masukkan bilangan pertama : '))
    bilangan2 = int(input('Masukkan bilangan kedua : '))
    bilangan3 = int(input('Masukkan bilangan ketiga : '))
    bilangan4 = int(input('Masukkan bilangan keempat : '))
    descending = [bilangan1, bilangan2, bilangan3, bilangan4]
    for x in sorted(descending, reverse=True):
        a += str(f"{x} ")
    print("Urutan bilangan dari yang terbesar adalah",a)
else:
    print('Menu tidak terdaftar dalam pilihan')
