target_dir = '/Users/Miao/Documents/code/sec/csv/log20160101.csv'
def pre_step2(cik):
	f = open('/Users/Miao/Documents/code/sec/csv/log20160101.csv', 'r')
	wf = open('/Users/Miao/Documents/code/sec/csv/log20160101-1.csv', 'wb')
	f.readline()
	i = 0
	while (1):
		line = f.readline().strip()
		if len(line) == 0:
			break
		data = line.split(',')
		data[4] = data[4][:-2]
		#print data[4]
		if data[4] in cik:
			#print data[4]
			wf.write(line+'\r\n')
	f.close()
	wf.close()

def load_cik():
	f = open('/Users/Miao/Documents/code/sec/cik.csv', 'r')
	f.readline()
	cik = []
	while (1):
		line = f.readline().strip()
		if len(line) == 0:
			break
		cik.append(line.split(',')[-1])
	f.close()
	f = open('/Users/Miao/Documents/code/sec/cik11.csv', 'wb')
	for i in cik:
		f.write(i+'\r\n')
	f.close()

	return cik


cik = load_cik()
pre_step2(cik)
