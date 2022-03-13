import threading, requests, time
from termcolor import colored
import os
os.system('color')

print('   ********************')
print('   *   LOAD TESTING   *')
print('   ********************')
 
#-----TEST URL-----#
status_code = {'100':'Continue','101':'Switching Protocols','102':'Processing (WebDAV)','103':'Early Hints','200':'OK','201':'Created','202':'Accepted','203':'Non-Authoritative Information','204':'No Content','205':'Reset Content','206':'Partial Content','207':'Multi-Status (WebDAV)','208':'Already Reported (WebDAV)','226':'IM Used (HTTP Delta Encoding','300':'Multiple Choice','301':'Moved Permanently','302':'Found','303':'See Other','304':'Not Modified','307':'Temporary Redirect','308':'Permanent Redirect','400':'Bad Request','401':'Unauthorized','402':'Payment Required','403':'Forbidden','404':'Not Found','405':'Method Not Allowed','406':'Not Acceptable','407':'Proxy Authentication Required','408':'Request Timeout','409':'Conflict','410':'Gone','411':'Length Required','412':'Precondition Failed','413':'Payload Too Large','414':'URI Too Long','415':'Unsupported Media Type','416':'Range Not Satisfiable','417':'Expectation Failed','418':'I am a teapot','421':'Misdirected Request','422':'Unprocessable Entity (WebDAV)','423':'Locked (WebDAV)','424':'Failed Dependency (WebDAV)','425':'Too Early','426':'Upgrade Required','428':'Precondition Required','429':'Too Many Requests','431':'Request Header Fields Too Large','451':'Unavailable For Legal Reasons','500':'Internal Server Error','501':'Not Implemented','502':'Bad Gateway','503':'Service Unavailable','504':'Gateway Timeout','505':'HTTP Version Not Supported','506':'Variant Also Negotiates','507':'Insufficient Storage (WebDAV)','508':'Loop Detected (WebDAV)','509':'Bandwidth Limit Exceeded (Apache)','510':'Not Extended','511':'Network Authentication Required','598':'Network Read Timeout Error','599':'Network Connect Timeout Error'}

def test_url(url,count,method):
    if method == 'get':
        req_res = requests.get(url_link)
        res = req_res.status_code
        result(url,count,res)
    elif method == 'post':
        req_res = requests.post(url_link)
        res = req_res.status_code
        result(url,count,res)

passed = 0
failed = 0
def result(url,count,res):
    global passed, failed
    try:
        if res == requests.codes.ok:
            print('User'+str(count)+' : '+colored(str(res)+' ('+str(status_code[str(res)])+')','green')+' - '+str(url)+colored(' >> ','cyan')+colored('Success','green'))
            passed+=1
        else:
            print('User'+str(count)+' : '+colored(str(res)+' ('+str(status_code[str(res)])+')','red')+' - '+str(url)+colored(' >> ','cyan')+colored('Failed','red'))
            failed+=1
    except:
        print('User'+str(count)+' : '+colored(str("This site can't be reached"),'red'))
        failed+=1
#**************#

#--------LOAD TESTING--------#
def start_load_test(url,method):
    start_time = time.perf_counter()
    threads = []
    for usr in range(int(number_of_times_the_test_execute)):
        t = threading.Thread(target=test_url ,args=[url,usr+1,method])
        t.start()
        threads.append(t)
    for n in threads: 
        n.join()
    end_time = time.perf_counter()
    print('\n'+colored('Time Taken: '+str(end_time-start_time)+' seconds','yellow'))
    print('Passed Test: '+colored(str(passed),'green'))
    print('Failed Test: '+colored(str(failed),'red'))
#********************************#


"""---EXECUTE---"""
status = True
while status:
    print('[eg: https://www.google.com]\n')
    lnk = True
    while lnk:
        url_link = str(input('Enter url: '))
        if 'https://' in url_link or 'http://' in url_link:
            lnk = False
        else:
            print('URL Incorrect! Try again..')
            lnk = True
    mthd = True
    while mthd:
        method = input('Method (GET/POST): ').lower()
        if method == 'get':
            mthd = False
        elif method == 'post':
            mthd = False
        else:
            mthd = True
    num = True
    while num:
        number_of_times_the_test_execute = input('Number of users: ')
        if number_of_times_the_test_execute.isdigit():
            start_load_test(url_link,method)
            xit = True
            while xit:
                nxt = str(input('\nDo you want to continue?(Y or N): ')).lower()
                if nxt == 'y':
                    xit = False
                    num = False
                    status = True
                    passed = 0
                    failed = 0
                elif nxt == 'n':
                    xit = False
                    num = False
                    status = False
                else:
                    print('Option Incorrect! Try again..')
                    xit = True
                    num = False
                    status = False
            print('\n')
        else:
            print('Not a number! Try again..')
            num = True




