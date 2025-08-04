from datetime import datetime
import time
import os

dt = datetime.now()

while True:

    # get current local time as structured data
    current_time =  time.localtime()

   
# format the time in 12-hour clock with AM/PM
    formatted_time = time.strftime("%H:%M:%S", current_time)
    print(formatted_time)
    # print('{}:{}:{}'.format(dt.hour, dt.minute, dt.second))
    time.sleep(1)
    os.system('cls')
    
