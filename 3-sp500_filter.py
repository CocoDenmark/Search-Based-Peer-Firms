# only hold the sp500 cik
import os
import datetime

start_date = datetime.date(2016,9,26)
end_date = datetime.date(2016,9,30)
read_dir = '/Users/Miao/Documents/code/sec/csv/'
write_dir = '/Users/Miao/Documents/code/sec/sp500/'
def pre_step2(filename, cik):
	f = open(read_dir+filename, 'r')
	wf = open(write_dir+filename, 'wb')
	f.readline()
	i = 0
	while (1):
		line = f.readline().strip()
		if len(line) == 0:
			break
		data = line.split(',')
		data[4] = data[4][:-2]
		if data[4] in cik:
			wf.write(line+'\r\n')
	f.close()
	wf.close()

def load_cik():
	f = open('/Users/Miao/Documents/code/sec/cik.csv', 'r')
	f.readline()
	cik = set()
	while (1):
		line = f.readline().strip()
		if len(line) == 0:
			break
		cik.add(line.split(',')[-1])
	f.close()

	return cik

def file_name_generate(start, end):
	days = [start + datetime.timedelta(days=x) for x in xrange((end-start).days + 1)]
	#days = [d1 + datetime.timedelta(days = x) for x in xrange(num_days)]
	res = []
	for d in days:
		res.append('log'+d.strftime('%Y%m%d')+'.csv')
	return res


cik = load_cik()
file_name = file_name_generate(start_date, end_date)
for f in file_name:
	print f
	pre_step2(f,cik)




