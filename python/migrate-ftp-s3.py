# Import Module
# pip install boto3
import ftplib
import argparse
import boto3
from io import BytesIO

def transfer(ftpcon, filePath):
    print("Transfer Started " + filePath)
    r = BytesIO()
    ftpcon.retrbinary('RETR '+filePath, r.write)
    r.seek(0)
    s3 = boto3.resource('s3')
    boto3.client('s3').upload_fileobj(r, 'ftppoc', filePath)
    print("Transfer Completed ")


def list_recursive(ftp, remotedir):
    ftp.cwd(remotedir)
    for entry in ftp.mlsd():
        if entry[1]['type'] == 'dir':
            remotepath = remotedir + "/" + entry[0]
            list_recursive(ftp, remotepath)
        else:
            print(f'{remotedir}/{entry[0]}')
            transfer(ftp,f'{remotedir}/{entry[0]}')

parser = argparse.ArgumentParser()
parser.add_argument('--HOSTNAME', dest='HOSTNAME', type=str, help='HOSTNAME')
parser.add_argument('--USERNAME', dest='USERNAME', type=str, help='USERNAME')
parser.add_argument('--PASSWORD', dest='PASSWORD', type=str, help='PASSWORD')
args = parser.parse_args()

# Fill Required Information
HOSTNAME = args.HOSTNAME
USERNAME = args.USERNAME
PASSWORD = args.PASSWORD

# Connect FTP Server
ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

# force UTF-8 encoding
ftp_server.encoding = "utf-8"

list_recursive(ftp_server,"")

# Close the Connection
ftp_server.quit()
