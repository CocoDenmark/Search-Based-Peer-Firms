# download the form information for all filings and unzip
import os, urllib2, urllib
import zipfile


path = '/Users/Miao/Documents/code/form_data/'
url_fixed = 'http://www.sec.gov/dera/data/Public-EDGAR-log-file-data/'
target_dir = '/Users/Miao/Documents/code/form/'

def unzip(source_zip, target_dir, file_name):
	myzip = zipfile.ZipFile(source_zip)
	for f in myzip.namelist():
		myzip.extract(f, target_dir)
	myzip.close()
	os.rename(target_dir+'form.idx', target_dir+file_name[0:8]+'.idx')

year = []
for i in range(2000,2017):
	year.append(str(i))
season = ['QTR1','QTR2','QTR3','QTR4']

for y in year:
	for s in season:
		print s+y
		file_name = s+y+'form.zip'
		url = 'https://www.sec.gov/Archives/edgar/full-index/'+y+'/'+s+'/form.zip'
		dest_dir = os.path.join(path, file_name)

		urllib.urlretrieve(url, dest_dir)
		unzip(path+file_name, target_dir, file_name)
