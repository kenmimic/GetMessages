import sys,os
import requests
import json
import urllib2#,urllib2,urllib3,re

url = ''

#with open('/usr/share/secLists/Discovery/Web-Content/common.txt','r') as folders:
with open(sys.argv[1],'r') as folders:
  for folder in folders.readlines():
    enumerate_url = url+folder
    response = os.popen('curl -i %s' %(enumerate_url)).read()
    
    if "Token" in response:
	    with open('./Missing_Token_path','a') as outfile:
	        outfile.write(enumerate_url)
	        #outfile.write(response)
	        print enumerate_url
	        print response
	        outfile.close()
folders.close()
