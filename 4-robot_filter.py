# only hold the cik with ip per day <= 50


import csv
import os
import datetime
import gc


start_date = datetime.date(2016,9,26)
end_date = datetime.date(2016,9,30)

read_dir = '/Users/Miao/Documents/code/sec/sp500/'
write_dir = '/Users/Miao/Documents/code/sec/ip/'

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

	res = {}
	for i in xrange(len(cik)):
		res[cik[i]] = i
	return res

def pre_step1(source, dest):
	ip_dict = pre_step2(source)
	rf = open(source, 'r')
	wf = open(dest, 'wb')
	rf.readline()
	while (1):
		line = rf.readline()
		if len(line.strip()) == 0:
			break
		data = line.strip().split(',')
		ip = data[0].split('.')
		if ip_dict[ip[0]][ip[1]][ip[2]][ip[3]] <= 50:
			wf.write(line)
	del ip_dict
	gc.collect()
	rf.close()
	wf.close()

def pre_step2(file_dir):
	print 'step2' + file_dir
	cik = load_cik()
	f = open(file_dir, 'r')
	f.readline()
	ip_dict = dict()
	while (1):
		line = f.readline().strip()
		if len(line) == 0:
			break
		data = line.split(',')
		ip = data[0].split('.')
		data[4] = data[4][:-2]
		if ip[0] in ip_dict.keys():
			if ip[1] in ip_dict[ip[0]].keys():
				if ip[2] in ip_dict[ip[0]][ip[1]].keys():
					if ip[3] in ip_dict[ip[0]][ip[1]][ip[2]].keys():
						ip_dict[ip[0]][ip[1]][ip[2]][ip[3]].add(cik[data[4]])
					else:
						ip_dict[ip[0]][ip[1]][ip[2]][ip[3]] = set([cik[data[4]]])
				else:
					ip_dict[ip[0]][ip[1]][ip[2]] = dict()
					ip_dict[ip[0]][ip[1]][ip[2]][ip[3]] = set([cik[data[4]]])
			else:
				ip_dict[ip[0]][ip[1]] = dict()
				ip_dict[ip[0]][ip[1]][ip[2]] = dict()
				ip_dict[ip[0]][ip[1]][ip[2]][ip[3]] = set([cik[data[4]]])
		else:
			ip_dict[ip[0]] = dict()
			ip_dict[ip[0]][ip[1]] = dict()
			ip_dict[ip[0]][ip[1]][ip[2]] = dict()
			ip_dict[ip[0]][ip[1]][ip[2]][ip[3]] = set([cik[data[4]]])
	f.close()
	for k0 in ip_dict.keys():
		for k1 in ip_dict[k0].keys():
			for k2 in ip_dict[k0][k1].keys():
				for k3 in ip_dict[k0][k1][k2].keys():
					ip_dict[k0][k1][k2][k3] = len(ip_dict[k0][k1][k2][k3])
	return ip_dict


def file_name_generate(start, end):
	days = [start + datetime.timedelta(days=x) for x in xrange((end-start).days + 1)]
	#days = [d1 + datetime.timedelta(days = x) for x in xrange(num_days)]
	res = []
	for d in days:
		res.append('log'+d.strftime('%Y%m%d')+'.csv')
	return res




#for f in os.listdir(path1)[1:3]:
	#pre_step1(path1+f, path
file_name = file_name_generate(start_date, end_date)
for f in file_name:
	print f
	pre_step1(read_dir+f, write_dir+f)
