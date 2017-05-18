# count the daily searchs between firm i and firm j
import datetime
import pandas as pd


start_date = datetime.date(2016,9,1)
end_date = datetime.date(2016,9,30)
#source_path = '/Users/Miao/Documents/code/sec/fundamental/'
source_path = '/Users/Miao/Documents/code/sec/final/'
dest_path = '/Users/Miao/Documents/code/sec/factor/'



def file_name_generate(start, end):
	days = [start + datetime.timedelta(days=x) for x in xrange((end-start).days + 1)]
	#days = [d1 + datetime.timedelta(days = x) for x in xrange(num_days)]
	res = []
	for d in days:
		res.append('log'+d.strftime('%Y%m%d')+'.csv')
	return res


file_name = file_name_generate(start_date, end_date)

col = [1,3,5,6,7,8,9,10,11,12,13,14]
for f_n in file_name:
	print f_n
	pair = {}
	df = pd.read_csv(source_path+f_n, header=None)
	wf = open(dest_path+f_n, 'wb')
	for c in col:
		del df[c]
	x = df.sort(0)
	x = x.sort(2)
	n = len(x)
	pre_ip = 'x'
	cik = []
	for row in xrange(n):
		if x.iloc[row][0] != pre_ip:
			if len(cik)>1:
				for i in xrange(len(cik)-1):
					j = i+1
					while j<len(cik):
						if cik[i] in pair.keys():
							if cik[j] in pair[cik[i]].keys():
								pair[cik[i]][cik[j]] += 1
							else:
								pair[cik[i]][cik[j]] = 1
						else:
							pair[cik[i]] = {}
							pair[cik[i]][cik[j]] = 1
						j += 1
			pre_ip = x.iloc[row][0]
			cik = [str(x.iloc[row][4])]
		else:
			cik.append(str(x.iloc[row][4]))

	for i in pair.keys():
		sum_i = 0
		for j in pair[i].keys():
			sum_i += pair[i][j]
		for j in pair[i].keys():
			wf.write(i+','+j+','+str(pair[i][j])+','+str(sum_i)+','+str(float(pair[i][j])/sum_i)+'\r\n')
	wf.close()
	del df




