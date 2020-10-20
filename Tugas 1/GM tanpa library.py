inputan = input("Masukkan Nilai : ")
y = x.split(' ')
n = len(masukan)

nilai = 1
for i in y:
	nilai = nilai * float(i)
gm = round(nilai ** (1/n))
print("Geometri Average : ",gm)