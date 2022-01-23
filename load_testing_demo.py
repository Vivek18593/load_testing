import threading, requests, time
from termcolor import colored

#-----API LINK--(REPLACED THE VALUE OF 'name' AND 'id' WITH 'data1' and 'data2')-----#
test_url = 'https://w3schools.com/python/demopage.htm?name=data1&id=data2'
#******************#

#----NUMBER OF USERS----#
number_of_times_the_test_execute = 1000
#********************#

#-----TEST-----#
response_code = [200,201,202,204]
def api_params(url,i,count):
    #---ADD OR REMOVE THE PARAMETERS ACCORDING TO THE URL---#
    url = url.replace('data1', 'name'+str(i))
    url = url.replace('data2', 'id'+str(i))
    
    try:
        #---CHANGE THE REQUEST METHOD CORRESPONDING TO THE URL---#
        result = requests.get(url)

        if result.status_code in response_code:
            print(str(count)+' '+colored(str(result.status_code),'green')+' '+str(url)+colored(' -Success','green'))
        else:
            print(str(count)+' '+colored(str(result.status_code),'red')+' '+str(url)+colored(' -Failed','red'))
    except:
        print('Request Failed!')
#**************#

#--------LOAD TESTING--------#
counter = 1
def start_load_testing(url):
    global counter
    start_time = time.perf_counter()
    threads = []
    for i in range(number_of_times_the_test_execute):
        t = threading.Thread(target=api_params, args=[url,i+1,counter])
        t.start()
        threads.append(t)
        counter+=1
    end_time = time.perf_counter()
    print(end_time-start_time,'second(s)')
#****************************#


#-----RUN-----#
start_load_testing(test_url)





