from plyer import notification
import time

def reminder():
    notification.notify(title = "Break reminder",message= "Hello sir please take some break from work",timeout = 1)

while True:
    reminder()
    time.sleep(10)