#use to trim form, from idx to csv with only type and name

file_type = ['10-K', '10-Q','8-K','S-1', '14A']

path = '/Users/Miao/Documents/code/form/'
target = '/Users/Miao/Documents/code/form_csv/'
year = []
for i in range(2000,2017):
	year.append(str(i))
season = ['QTR1','QTR2','QTR3','QTR4']

file_name = []
for y in year:
	for s in season:
		file_name.append(s+y)

for f_n in file_name:
	print f_n
	rf = open(path+f_n+'.idx', 'r')
	wf = open(target+'recode'+f_n[4:]+'.csv', 'a')

	l = rf.readline()
	while(l[0]!='-'):
		l = rf.readline()
	while(1):
		try:
			l = rf.readline()
			if len(l) == 0:
				break
			data = l.split(' ')
			if data[0] in file_type:
				for x in data:
					if len(x)>20:
						code = x.split('/')[-1]
						code = code.split('.')[0]
						wf.write(code.strip()+'\r\n')
		except:
			print line
			pass
	rf.close()
	wf.close()




	#wf = open(target+f_n+'.csv', 'w')
