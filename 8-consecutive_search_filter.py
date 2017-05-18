# only hold the first click per user per company per day
import datetime


start_date = datetime.date(2016,9,1)
end_date = datetime.date(2016,9,30)
source_path = '/Users/Miao/Documents/code/sec/fundamental/'
dest_path = '/Users/Miao/Documents/code/sec/final/'



def file_name_generate(start, end):
	days = [start + datetime.timedelta(days=x) for x in xrange((end-start).days + 1)]
	#days = [d1 + datetime.timedelta(days = x) for x in xrange(num_days)]
	res = []
	for d in days:
		res.append('log'+d.strftime('%Y%m%d')+'.csv')
	return res




file_name = file_name_generate(start_date, end_date)
user_dict = {}
for f_n in file_name:
	log_f = open(source_path+f_n, 'r')
	dest = open(dest_path+f_n, 'w')
	ip_dict = {}
	print f_n

	while(1):
		try:
			l = log_f.readline().strip()
			if len(l) == 0:
				break
			data = l.split(',')
			cik = data[4]
			ip = data[0].split('.')			
			if ip[0] in ip_dict.keys():
				if ip[1] in ip_dict[ip[0]].keys():
					if ip[2] in ip_dict[ip[0]][ip[1]].keys():
						if ip[3] in ip_dict[ip[0]][ip[1]][ip[2]].keys():
							if cik in ip_dict[ip[0]][ip[1]][ip[2]][ip[3]]:
								continue
							else:
								ip_dict[ip[0]][ip[1]][ip[2]][ip[3]].add(cik)
						else:
							ip_dict[ip[0]][ip[1]][ip[2]][ip[3]] = set([cik])
					else:
						ip_dict[ip[0]][ip[1]][ip[2]] = dict()
						ip_dict[ip[0]][ip[1]][ip[2]][ip[3]] = set([cik])
				else:
					ip_dict[ip[0]][ip[1]] = dict()
					ip_dict[ip[0]][ip[1]][ip[2]] = dict()
					ip_dict[ip[0]][ip[1]][ip[2]][ip[3]] = set([cik])
			else:
				ip_dict[ip[0]] = dict()
				ip_dict[ip[0]][ip[1]] = dict()
				ip_dict[ip[0]][ip[1]][ip[2]] = dict()
				ip_dict[ip[0]][ip[1]][ip[2]][ip[3]] = set([cik])
			dest.write(l+'\r\n')
		except:
			pass
	log_f.close()
	dest.close()


