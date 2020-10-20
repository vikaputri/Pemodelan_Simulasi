def GeometriAverage(x):
	y = x.split(' ')
	n = len(y)

	nilai = 1
	for i in y:
		nilai = nilai * float(i)
	gm = nilai ** (1/n)
	return gm
