
a=[38,21,53,62,19]
for i in a:
	print(i)

a.append(213)
for i in a:
	print(i)
for i in range(len(a)):
	print(a[i])
for index, value in enumerate(a):
	print(index,value)
