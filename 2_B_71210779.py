print ("="*10, "PROGRAM PENGHITUNG PYTHAGORAS", "="*10)
bilangan1 = int(input("Masukkan bilangan bulat pertama: "))
bilangan2 = int(input("Masukkan bilangan bulat kedua: "))
bilangan3 = int(input("Masukkan bilangan bulat ketiga: "))
penjumlahan = ((bilangan1**2) + (bilangan2**2))
if penjumlahan == (bilangan3**2):
    print ("Merupakan Pythagoras.")
else:
    print("Bukan merupakan Pythagoras.")
