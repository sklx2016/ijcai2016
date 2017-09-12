import csv

def transfor_data_format():

	sum_t = []

	for x in xrange(1,4):
		table_name = "table_"+str(x)
		name 	   = "dataset/"+table_name+".csv"
		table_1    = open(name)
		
		t = []
		for line in table_1:
			line = line.strip('\n')
		 	line = line.split(',')
		 	t.append(line)
		sum_t.append(t)
	
	return sum_t
	
def fun(data = []):
	result = []
	for line in data:
		merchant_id_list = line[2]
		merchant_id_list = merchant_id_list.split(':')
		
		for id_sigle in merchant_id_list:
			result.append([line[0], line[1], id_sigle])
	
	return result

def main():
	return_data = transfor_data_format()
	#save the result in corresponding table
	table_true 		 = return_data[0]
	table_merchant	 = return_data[1]
	table_submission = return_data[2]
	# print table_merchant
	#save true data
	s1  = fun(table_true)
	#sort by third columns
	s1.sort(key=lambda x:x[2])
	# print s1
	#save submission data
	s1_ = fun(table_submission)
	#sort by third columns
	s1_.sort(key=lambda x:x[2])
	# print s1_
	#save position
	i1 		= 0
	i2 		= 0
	j1 		= 0
	j2 		= 0
	#X value
	sum_min = 0
	#Y value
	sum_s_ 	= 0
	#Z value
	sum_b 	= 0
	#
	b 		= 0
	while i2<len(s1) or j2<len(s1_):
		while i2<len(s1) and (s1[i2][2] == s1[i1][2]):
			i2 += 1
		while j2<len(s1_) and (s1_[j2][2] == s1_[j1][2]):
			j2 += 1			
		comp = 0
		#compute the Y value
		sum_s_ += j2-j1

		if s1[i1][2] == s1_[j1][2]:
			i =i1
			j =j1
			for x in table_merchant:
				if x[0] == s1[i1][2]:
					b = int(x[1])
					break
			num = 0
			while i<i2:
				j = j1
				while j<j2:
					if s1[i]==s1_[j]:
						num += 1
					j += 1
				i += 1
			value = min(num, b)
			sum_b += min(b,(i2-i1))
			i1 = i2
			j1 = j2
		elif s1[i1][2] < s1_[j1][2]:
			num = j2-j1
			for x in table_merchant:
				if x[0] == s1[i1][2]:
					b = int(x[1])
					break
			value = min(num, b)
			sum_b += value
			i1 = i2

		else:
			num = j2-j1
			for x in table_merchant:
				if x[0] == s1[i1][2]:
					b = int(x[1])
					break
			value = min(num, b)
			j1 = j2


		sum_min += value
		# j1 = j2
		# i1 = i2
	F1 = 2.0*sum_min/(sum_s_+sum_b)
	print sum_min, sum_s_, sum_b, F1

def hahaha():
	print True & False
if __name__ == '__main__':
	main()