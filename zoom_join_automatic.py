"""
Version 1.1
- Added a print statement for health check
"""
import schedule
import time
import webbrowser

main_link = 'https://us02web.zoom.us/j/2751012834'

def open_link(link):
    webbrowser.open(link)

def church_meeting():
    open_link(main_link)

print("Program initiated, Device Healthy!")
schedule.every().tuesday.at("20:45").do(church_meeting)
schedule.every().thursday.at("20:45").do(church_meeting)
schedule.every().friday.at("20:45").do(church_meeting)
schedule.every().sunday.at("11:10").do(church_meeting)

while 1:
    schedule.run_pending()
    time.sleep(1)
