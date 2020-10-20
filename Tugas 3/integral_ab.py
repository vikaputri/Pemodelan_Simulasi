a = int(input("Masukkan Batas Awal     : "))
b = int(input("Masukkan Batas Akhir    : "))

def f(x) :
    return x

def integer(f, n):
    lebar = (float(b)-float(a)) /(float(n))
    hasil = 0
    for i in range(n):
        tinggi = f(a + i*lebar)
        luas = lebar * tinggi
        hasil += luas
    return hasil

 
print("Integral dari X dengan batas",a,"dan",b,"dan n = 10 adalah",integer(f,10))
print("Integral dari X dengan batas",a,"dan",b,"dan n = 100 adalah",integer(f,100))
print("Integral dari X dengan batas",a,"dan",b,"dan n = 1000 adalah",integer(f,1000))
