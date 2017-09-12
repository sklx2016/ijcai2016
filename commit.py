import csv

def main():
	#read file
	LMNum_file = open("LMnum","r")
	LMNum = LMNum_file.readlines()
	LMNum_file.close()
	#store LMNum list
	LMN_list = []
	for line in LMNum:
		line = line.strip("\n")
		line = line.split(" ")
		LMN_list.append(line)
	# print LMN_list
	#unicue Location
	max_lmn = []
	#pointer
	i = 0
	j = 0
	max_ = int(LMN_list[0][2])
	while i<(len(LMN_list)-1):
		if LMN_list[i][0] != LMN_list[i+1][0]:
			max_lmn.append([LMN_list[j][0], LMN_list[j][1]])
			j = i+1
			i = j
			max_ = int(LMN_list[j][2])
		else:
			if int(LMN_list[i+1][2]) > max_:
				max_ = int(LMN_list[i+1][2])
				j = i+1
			i += 1
		
	#read koubei_test
	koubei_test_file = open("ijcai2016_koubei_test","r")
	koubei_test = koubei_test_file.readlines()
	koubei_test_file.close()
	koubei_test_list = []
	#store koubei_test_list
	for line in koubei_test:
		line = line.strip("\n")
		line = line.split(",")
		line.append(0)
		koubei_test_list.append(line)
	# print koubei_test_list
	#read submission_origin file
	subm_list = []
	subm_file = open("submission.csv","r")
	subm = csv.reader(subm_file)
	for line in subm:
		subm_list.append(line)
	subm_file.close()
	# print subm_list
	csvfile = open("submission_add.csv","wb")
	writer = csv.writer(csvfile)

	for line in koubei_test_list:
		i = 0
		j = 0
		while i<len(max_lmn):
			if line[1] == max_lmn[i][0]:
				line[2] =max_lmn[i][1]
				break
			i += 1
		while j<len(subm_list):
			flag = (line[0]==subm_list[j][0]) and (line[1]==subm_list[j][1])
			if(flag):
				line[2] = subm_list[j][2]
				subm_list.pop(j)
				break
			j += 1
		writer.writerow(line)
	# print koubei_test_list
	
	csvfile.close()
	print "finish"

if __name__ == '__main__':
    main()
