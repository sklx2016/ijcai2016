import csv

def main():
	wholetext = []
	ulm = []	
	data = open("sub_gmcsdy3")
	for line in data:
		lines = line.split(' ')
		wholetext.append(lines)
	data.close()
	i = 0
	j = 1
	merchant = wholetext[0][2]
	# print (merchant + ':' + wholetext[1][2])
	while j < len(wholetext):
		tag = (wholetext[i][0] == wholetext[j][0]) and (wholetext[i][1] == wholetext[j][1])
		if tag:
			merchant = merchant + ':' + wholetext[j][2]
			j += 1
		else:
			ulm.append([wholetext[i][0], wholetext[i][1], merchant])
			i = j
			merchant = wholetext[i][2]
			j += 1
		if i == len(wholetext) - 1:
			ulm.append([wholetext[i][0], wholetext[i][1], merchant])
	print ulm
	
	csvfile = file('submission.csv','wb')
	writer = csv.writer(csvfile)
	writer.writerows(ulm)
	csvfile.close()

if __name__ == '__main__':
	main()
