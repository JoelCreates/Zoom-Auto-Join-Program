"""
Version 1.0
- Made the Join link into a variable so that other ones can be inserted when different join links are required. This reduces time waste during copy
and paste process.
"""
import schedule
import time
import webbrowser

main_link = 'https://us02web.zoom.us/j/2751012834'

def open_link(link):
    webbrowser.open(link)

def church_meeting():
    open_link(main_link)

schedule.every().tuesday.at("20:45").do(church_meeting)
schedule.every().thursday.at("20:12").do(church_meeting)
schedule.every().friday.at("20:45").do(church_meeting)
schedule.every().sunday.at("11:10").do(church_meeting)

while 1:
    schedule.run_pending()
    time.sleep(1)
