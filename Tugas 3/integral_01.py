def f(x) :
    return x

def integral(f, n):
    h = 1 / float(n)
    hasil = 0.5 * h * (f(0) + f(1))
    for i in range(1, int(n)):
        hasil = hasil + h * f(i * h)
    return hasil
 
print("Integral dari X dengan batas 0 dan 1 dan n = 10 adalah",integral(f, 10))
print("Integral dari X dengan batas 0 dan 1 dan n = 100 adalah",integral(f, 100))
print("Integral dari X dengan batas 0 dan 1 dan n = 1000 adalah",integral(f, 1000))
