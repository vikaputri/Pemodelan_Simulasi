print("Multiplicative Congruential Generator")
print("=====================================\n")

def rand(a, m, seed):
	x = []
	x.append(seed)
	for i in range(n):
		rand = (a * x[i]) % m
		x.append(rand)
	return x[1:]

a = int(input('Input a :'))
m = int(input('Input mod :'))
s = int(input('Input seed :'))
n = int(input('Input jumlah acak :'))

rand1 = rand(a, m, s)
rand2 = [i/m for i in rand1]

print()
print('Hasil:')
for i in range(len(rand1)):
	print('X{} = {}; X = {}'.format(i+1, rand1[i], rand2[i]))
