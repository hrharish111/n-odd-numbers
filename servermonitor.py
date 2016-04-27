n = 10

i = []
count = 1

while len(i) <n:
	if count%2 != 0:
		i.append(count)
		count+=1
	count+=1

print i