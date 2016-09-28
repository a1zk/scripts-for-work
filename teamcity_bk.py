#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import requests
"""
Data Backup
+++++++++++
"""
url = "http://domain:8111/httpAuth/app/rest/server/backup"

# === EDITED code = now working (see my answer below) ===
url = "http://domain:8111/httpAuth/app/rest/server/backup?includeConfigs=true&includeDatabase=true&includeBuildLogs=false&fileName=TCbackup"
# === /EDITED code (see my answer below) ===

params = {
        'fileName':'TCbackup',
        'includeBuildLogs':'false',
        'includeDatabase':'true',
        'includeConfigs':'true'
        }

post_data = urllib.urlencode(params)

req = urllib2.Request(url, post_data, headers={'Content-Type': 'application/xml'})

password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, url, 'user', 'pass')

auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)
opener = urllib2.build_opener(auth_manager)

urllib2.install_opener(opener)

handler = urllib2.urlopen(req)
handler.close()

#Backup status check
s = "Running"
while True:
    r = requests.get('http://domain:8111/httpAuth/app/rest/server/backup', auth=('user','pass'))
    s = r.text
    if s == "Idle" :
            break
