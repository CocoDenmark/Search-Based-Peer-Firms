# download the log files and unzip
import datetime
import os, urllib2, urllib
import zipfile



start_date = datetime.date(2016,10,1)
end_date = datetime.date(2016,10,5)


def date_generate(start = datetime.date(2016,1,1), end = datetime.date(2016,9,30)):
	#d1 = 
	#d2 = 
	days = [start + datetime.timedelta(days=x) for x in xrange((end-start).days + 1)]
	#days = [d1 + datetime.timedelta(days = x) for x in xrange(num_days)]

	return days

def season_generate(d):
	month = d.month
	if month%3 == 0:
		s = month/3
	else:
		s = month/3 + 1
	return 'Qtr' + str(s)


def unzip(source_zip, target_dir):
	myzip = zipfile.ZipFile(source_zip)
	for f in myzip.namelist():
		if f[-3:] == 'csv':
			print 'unzip' + f
			myzip.extract(f, target_dir)
	myzip.close()




path = '/Users/Miao/Documents/code/data/'
url_fixed = 'http://www.sec.gov/dera/data/Public-EDGAR-log-file-data/'
target_dir = '/Users/Miao/Documents/code/sec/csv/'
#2016/Qtr3/log20160930.zip
days = date_generate(start_date, end_date)


for d in days:
	url = url_fixed + str(d.year) + '/' + season_generate(d) + '/log' + d.strftime('%Y%m%d') + '.zip'
	file_name = 'log' + d.strftime('%Y%m%d') + '.zip'
	dest_dir = os.path.join(path, file_name)

	try:
		print d.strftime('%Y%m%d') + ' started'
		urllib.urlretrieve(url, dest_dir)
		print d.strftime('%Y%m%d') + ' success'
		unzip(path+file_name, target_dir)
		print d.strftime('%Y%m%d') + ' unzipped'
	except:
		print d.strftime('%Y%m%d')





