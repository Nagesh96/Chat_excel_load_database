import os
import logging
import datetime
import ftplib
import time

class SecurityDetail:
    def get_data(self):
        filelist = []
        try:
            ftp_host = os.environ.get('FTP_SERVER')
            ftp_pass = os.environ.get('FTP_PASSWORD')
            ftp_user = os.environ.get('FTP_USERNAME')
            f = ftplib.FTP(ftp_host)
            f.login(user=ftp_user, passwd=ftp_pass)
            f.cwd('/ftp-fund/Capacity Model/')
            logging.info('FTP Login Success')

        except ftplib.error_perm as error:
            if error:
                logging.info('FTP Login Failed')
            return

        data = []
        f.dir(data.append)
        current_year_month = datetime.datetime.today().strftime("%Y-%m")
        logging.info('Current Year-Month: ' + current_year_month)

        # Filter files based on the current year, month, and specified patterns
        filtered_files = [line for line in data if current_year_month in line and ('Non-NTAM' in line or 'NTAM' in line)]

        if not filtered_files:
            logging.info('No matching files found')
            f.quit()
            return

        datelist = []
        filelist = []
        
        for line in filtered_files:
            parts = line.split()
            filename = parts[-1]
            datestr = ' '.join(parts[0:2])
            date = time.strptime(datestr, '%m-%d-%y %H:%M%p')
            datelist.append(date)
            filelist.append(filename)

        combo = list(zip(datelist, filelist))
        combo.sort(key=lambda x: x[0], reverse=True)

        latest_files = [file for _, file in combo[:2]]

        for filename in latest_files:
            with open(filename, 'wb') as f_local:
                f.retrbinary(f'RETR {filename}', f_local.write)
            logging.info(f'Downloaded: {filename}')

        f.quit()

if __name__ == "__main__":
    sd = SecurityDetail()
    sd.get_data()
