# only hold the logs for the fundamental firms

import datetime


form_path = '/Users/Miao/Documents/code/form_csv/'
log_path = '/Users/Miao/Documents/code/sec/ip/'
dest_path = '/Users/Miao/Documents/code/sec/fundamental/'
start_date = datetime.date(2016,9,1)
end_date = datetime.date(2016,9,30)


def file_name_generate(start, end):
	days = [start + datetime.timedelta(days=x) for x in xrange((end-start).days + 1)]
	#days = [d1 + datetime.timedelta(days = x) for x in xrange(num_days)]
	res = []
	for d in days:
		res.append('log'+d.strftime('%Y%m%d')+'.csv')
	return res



def open_form(year):
	form = set()
	form_f = open(form_path+'recode'+year+'.csv', 'r')
	while(1):
		try:
			l = form_f.readline().strip()
			if len(l) == 0:
				break
			form.add(l)
		except:
			pass
	form_f.close()
	return form



file_name = file_name_generate(start_date, end_date)

form = dict()
form['2015'] = open_form('2015')

for f_n in file_name:
	print f_n
	log_f = open(log_path+f_n, 'r')
	dest = open(dest_path+f_n, 'w')

	while(1):
		try:
			l = log_f.readline().strip()
			if len(l) == 0:
				break
			code = l.split(',')[5]
			year = '20'+code.split('-')[1]
			if '20'+code.split('-')[1] not in form.keys():
				form[year] = open_form(year)
			if code in form[year]:
				dest.write(l+'\r\n')
		except:
			pass
	log_f.close()
	dest.close()


				



