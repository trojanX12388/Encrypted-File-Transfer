import os.path

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


gauth = GoogleAuth()
gauth.LoadCredentialsFile(os.path.dirname(__file__) + '/../bin/gauth/credentials.json') 
gauth.LoadClientConfigFile(os.path.dirname(__file__) + '/../bin/gauth/client_secrets.json')

drive = GoogleDrive(gauth)
folder = '1Z3t-FckIlQUTT-KnYsDVbveZQqduc1of' 

file_list = drive.ListFile({'q': "'%s' in parents and trashed=false"%(folder)}).GetList()

took = False
i = 1
for file1 in file_list:
    print('%s: %s | id: %s | Size(Bytes): %s ' % (i , file1['title'] , file1['id'], file1['quotaBytesUsed']))
    i += 1