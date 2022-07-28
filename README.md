# Zoom-Auto-Join-Program
This contains a Python Program that allows the user to automatically join a Zoom Meeting at any time. Days of the week are used through schedule library which allows for the function "every" to automatically prompt a browser to open at a specified time.
 -- IMAGE OF DAYS OF WEEK GOES HERE

During use, you would notice that this program has one disadvantage, which is that it requires the user to actively run it **every single time** prior to the start of their meeting. This, fortunately, is solved by Window's "Task Scheduler" program, which can set this program as a background process to be activated daily at a set time **without** user intervention. In order to do this, the user would have to first 
1. Create Task
2. Name the Task
3. To go to Actions, Click New, Make sure "Action" is set as "Start a Program".
4. Open Command (CMD) and type "where python" followed by enter, which should show the location of the Python exe. Copy and paste that in the "Program/script" section.
5. To put the name of the python program inside "Add arguments"
6. To put the location of the folder where the Zoom auto join program is; this goes in "Start in". Press OK after all of that.
7. Go to Trigger, set start date to whenever and manually adjust the trigger points to whatever you want to do.

-- Image of ZOOOM SCHEDULE
After that, press OK to confirm and let the Task Scheduler to its magic for you.