from cmath import log
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def login():
    client_confiq= 'client_secret20221005.json'
    GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = client_confiq
    gauth = GoogleAuth()
    #gauth.LocalWebserverAuth()
    
    gauth.LoadCredentialsFile(client_confiq)
    
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()

    gauth.SaveCredentialsFile(client_confiq) 
    
    return gauth

def toGoogleDrive(file_name):
    '''
    client_confiq= 'client_secrets.json'
    GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = client_confiq
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(client_confiq)
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile(client_confiq)
    '''
    gauth = login()
    drive = GoogleDrive(gauth) 
    gfile = drive.CreateFile({'parents': [{'id': '1CraRBPUj_6ndKkQcIsodn4SvS-v-E5Sy'}]})
	# Read file and set it as the content of this instance.
    gfile.SetContentFile(file_name)
    gfile.Upload() # Upload the file.


#toGoogleDrive("usbmicro.wav")
#login()