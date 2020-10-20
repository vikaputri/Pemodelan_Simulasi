print("Mixed Congruential Generator")
print("=====================================\n")

Xo = int(input("Masukkan Nilai Xo      : "))
a = int(input("Masukkan Nilai a       : "))
c = int(input("Masukkan Nilai c       : "))
m = int(input("Masukkan Nilai m       : "))
jmlRandom = int(input("Masukkan Jumlah Random : "))
Nums = [0] * (jmlRandom) 
Nums[0] = Xo 

print("\nJadi, dengan nilai Xo =", Xo,"Nilai a =", a,"Nilai c =", c,"dan Nilai m =", m)
print("\nHasil Random adalah :")

for i in range(1, jmlRandom): 
    Nums[i] = ((Nums[i - 1] * a) + c) % m 
    print(Nums[i], end = " ") 
