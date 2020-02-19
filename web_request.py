import sys,requests,datetime
from colorama import Fore, Back, Style

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

url = ''
keyword = 'Missing Authentication Token'

def now(TimeFormat):
  return datetime.datetime.today().strftime(TimeFormat)
path = "./Requests_result-"+now("%Y-%b-%d-%H-%I-%S")

def format_text(title,item):
  cr = '\r\n'
  section_break = cr + "*" * 20 + cr
  item = str(item)
  text = Style.BRIGHT + Fore.RED + title + Fore.RESET + section_break + item + section_break
  return text;

def ParseURL():
  with open(sys.argv[1],'r') as folders:
    for folder in folders.readlines():
      full_url = url + folder.strip('\n') # strip \n for correct url
      #print full_url
      r = requests.get(full_url,verify=False)
      folders.close()
      if keyword in r.text:
        with open(path,'a') as outfile:
          outfile.write(now("%x")+',')			
          outfile.write(r.url+',')			
          outfile.write(r.text+'\n')			
        outfile.close()
        print format_text('URL is: ',r.url)
        print format_text('TEXT is: ',r.text)

ParseURL()
