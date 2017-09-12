import sets

def main():
	trainUser = set()
	testUser = set()
	file1 = open('trainUser.txt')
	for i1 in file1:
		trainUser.add(i1)
	file1.close()

	file2 = open('testUser.txt')
	for i2 in file2:
		testUser.add(i2)
	file2.close
	newUser = testUser - trainUser
	print len(newUser)
	return 1
if __name__ == '__main__':
	main()