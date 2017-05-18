import datetime
import pandas as pd


start_date = datetime.date(2016,1,1)
end_date = datetime.date(2016,9,30)

read_path = '/Users/Miao/Documents/code/sec/factor/'
result_f = '/Users/Miao/Documents/code/sec/bps_cik.csv'
def file_name_generate(start, end):
	days = [start + datetime.timedelta(days=x) for x in xrange((end-start).days + 1)]
	#days = [d1 + datetime.timedelta(days = x) for x in xrange(num_days)]
	res = []
	for d in days:
		res.append('log'+d.strftime('%Y%m%d')+'.csv')
	return res


def load_cik():
	f = open('/Users/Miao/Documents/code/sec/cik.csv', 'r')
	f.readline()
	cik = {}
	while (1):
		try:
			line = f.readline().strip()
			if len(line) == 0:
				break
			data = line.split(',')
			cik[data[-1]] = data[0]
		except:
			pass
	f.close()
	return cik



file_name = file_name_generate(start_date, end_date)
saf_dict = {}
cik_dict = load_cik()
for f_n in file_name:
	print f_n
	rf = open(read_path+f_n,'r')
	while (1):
		try:
			line = rf.readline().strip()
			if len(line) == 0:
				break
			data = line.split(',')
			data[0] = cik_dict[data[0][:-2]]
			data[1] = cik_dict[data[1][:-2]]
			if data[0] in saf_dict.keys():
				if data[1] in saf_dict[data[0]].keys():
					saf_dict[data[0]][data[1]] += int(data[2])
					#saf_dict[data[0]][data[1]][1] += int(data[3])
				else:
					saf_dict[data[0]][data[1]] = int(data[2])
			else:
				saf_dict[data[0]] = dict()
				saf_dict[data[0]][data[1]] = int(data[2])
		except:
			pass
	rf.close()

'''for i in saf_dict.keys():
	for j in saf_dict[i].keys():
		saf_dict[i][j] = float(saf_dict[i][j][0])/float(saf_dict[i][j][1])'''



# column i 
# row j
col = saf_dict.keys()
for i in col:
	s = 0
	for j in saf_dict[i].keys():
		s += saf_dict[i][j]
	for j in saf_dict[i].keys():
		saf_dict[i][j] = float(saf_dict[i][j]) / float(s)

x = pd.DataFrame(saf_dict)
f = open(result_f, 'w')

for c in col:
	x = x.sort_values(by=c, axis=0, ascending=False)
	cik = list(x.index[0:10])
	f.write(c+',')
	for i in cik:
		f.write(i+','+str(x.loc[i,c])+',')
	f.write('\r\n')
f.close()
print x.head(20)
x.to_csv('/Users/Miao/Documents/code/sec/bps_dataframe.csv')





