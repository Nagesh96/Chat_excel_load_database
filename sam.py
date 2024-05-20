try:

Tanzu Kuber test

ftp_host = os.environ.get('FTP_SERVER')

ftp_pass os.environ.get('FTP_PASSWORD')

ftp_user= os.environ.get('FTP USERNAME')

f=ftplib.FTP(ftp_host)

f.login(user=ftp_user, passwd=ftp_pass)

f.cwd('/ftp-fund/Capacity Model/')

logging.info('Audit Parse FTP Login Success')

except ftplib.error_perm as error:

if error:

logging.info('Audit Parse FTP Login Failed')

data = []

f.dir(data.append)

datelist[]

currentYear str(datetime.datetime.today().year)

logging.info('Audit Parse pull_files method currentYear+ str(currentYear))

Weekly meet DAL Daily

To install py python pack

DAE Daily try

data [file for file in data if currentYear in file and 'Audit_Sum in file and 'AU' not in file and 'SO' not in file]

for line in data:

col line.split()

datestr''.join(line.split() [0:2])

date time.strptime(datestr, '%m-%d-%y %H:%M%p')

datelist.append(date) filelist.append(col[3])

combo zip(datelist, filelist)

who dict(combo)

logging.info('Audit Parse who+ str(who))
f.retrbinary('RETR %s' % who [sorted (who, reverse=True) [0]], open (who [sorted (who, reverse=True) [0]], 'wb').write)

f.retrbinary('RETR %s' % who [sorted (who, reverse=True) [1]], f.retrbinary('RETR %s' % who [sorted (who, reverse=True) [2]], open (who [sorted (who, reverse=True) [1]], 'wb').write) open (who [sorted (who, reverse=True) [2]], 'wb').write)

f.retrbinary('RETR %s' % who [sorted (who, reverse=True) [3]], f.retrbinary('RETR %s' % who [sorted (who, reverse=True) [4]], open (who [sorted (who, reverse=True) [3]], 'wb').write) open (who [sorted (who, reverse=True) [4]], 'wb').write)

f.quit()

try:

files_path = os.path.join(os.getcwd(), '*Sum*.txt')

files sorted(

glob.iglob(files_path), key=os.path.getctime, reverse=True) except Exception as e:

logging.info('Audit Parse e: '+ str(e)) logging.info('Exception occurred on downloading audit trail files')
