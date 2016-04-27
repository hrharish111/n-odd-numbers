n = 5

i = []
count = 1

while len(i) <n:
	if count%2 == 0:
		count+=1
	else:
		i.append(count)
		count+=1
print i