"""
Version 1.12
- Added lists for conditional statement to assess if the day the program is activated on is the correct day. Task Scheduler runs program everyday so this counteracts wasted processes.
- Added variables for the date and hour
- Added datetime
- Added exit clause to close program when not in use.
"""
import schedule
import time
import webbrowser
from datetime import datetime

main_link = 'https://us02web.zoom.us/j/2751012834'
today = datetime.today()
day = today.strftime("%A")
hour = time.strftime("%H")

nondays = ['Monday', 'Wednesday', 'Saturday']
activationhour = [11, 20]

def open_link(link):
    webbrowser.open(link)

def church_meeting():
    open_link(main_link)


print(f'Today is {day}. The program has been initiated, Device Healthy!')
schedule.every().tuesday.at("20:50").do(church_meeting)
schedule.every().thursday.at("20:50").do(church_meeting)
schedule.every().friday.at("20:50").do(church_meeting)
schedule.every().sunday.at("11:20").do(church_meeting)

while 1:
    if day in nondays or hour not in activationhour:
        print(f'The day {day} and time {hour} is not a part of the schedule! Exiting program now!')
        time.sleep(1)
        exit()
    else:
        schedule.run_pending()
        time.sleep(600)
        exit()
