from simple_salesforce import Salesforce
import requests
from io import StringIO
import pandas as pd

USERNAME = 'ntyagi@eightfold.ai.devsb'
USERNAME_PROD = 'ntyagi@eightfold.ai'
PASSWORD = ''
SECURITY_TOKEN_SB = ''
SECURITY_TOKEN_PROD = ''

sf = Salesforce(username = USERNAME_PROD,
                password = PASSWORD,
                security_token = SECURITY_TOKEN_PROD
                )

INSTANCE = 'https://eightfold.lightning.force.com'

print(sf.headers)

custom_headers = {
    'Authorization' : 'Bearer token',
    'X-PrettyPrint' : '1'
}

data = sf.query_all("SELECT Id, EventType, LogFile, LogDate, LogFileLength FROM EventLogFile WHERE LogDate = This_Month Limit 1")
print(len(data['records']))
for i in data['records']:
    print(i['LogFile'])
    URL = INSTANCE + i['LogFile']
    print(URL)
    response = requests.get(URL, headers=sf.headers);
    eachLogFile = response.content
    print(eachLogFile)
    csvfile = open('LogFile3.csv', 'wb')
    csvfile.write(eachLogFile)
    csvfile.close()




"""

sf = Salesforce(username = USERNAME,
                password = PASSWORD,
                security_token = SECURITY_TOKEN,
                domain='test')


data = sf.query_all("SELECT Id, Email FROM Contact WHERE Id IN ('0033m000037dtROAAY','0033m000036Z7nYAAS')")
print(len(data['records']))
for i in data['records']:
    print(i['Email'])

print(data['records'][1]['Email'])
"""

"""
eflog = sf.query_all("SELECT Id, EventType, LogFile, LogDate, LogFileLength FROM EventLogFile WHERE LogDate > Yesterday AND EventType='API'")
print(eflog)

headers = {
    'Authorization' : 'Bearer token',
    'X-PrettyPrint' : '1'
}

for logfile in eflog :
    response = requests.get(sf_instance + i['LogFile'], headers=sf.headers, cookies={'sid': sf.session_id});
    eachLogFile = response.content

"""

