print("Multiplicative Congruential Generator")
print("=====================================\n")

Xo = int(input("Masukkan Nilai Xo      : "))
a = int(input("Masukkan Nilai a       : "))
m = int(input("Masukkan Nilai m       : "))
jmlRandom = int(input("Masukkan Jumlah Random : "))
Nums = [0] * (jmlRandom) 
Nums[0] = Xo 

print("\nJadi, dengan nilai Xo =", Xo,"Nilai a =", a,"dan Nilai m =", m)
print("maka Hasil Random adalah :")

for i in range(1, jmlRandom): 
    Nums[i] = (Nums[i - 1] * a) % m 
    print(Nums[i], end = " ") 
