import sys
from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Attachment, Comment, Task
import pyperclip

##########################
#Helper Functions
##########################

def add_comment(x_task_id, pg_num):
    try:
        message = pyperclip.paste()
        newline_strike = message.replace("\n", "")
        mod_message = newline_strike + " pg " + pg_num
        api.add_comment(task_id=x_task_id, content=mod_message)
    except Exception as error:
        print(error)

##########################
#INFORMATION SETUP
##########################
x_pg_num =input("pg. ")

#Gather the input from user
x_task_id = sys.argv[1]

#access api token
with open("api.token", "r") as key_in:
    api = TodoistAPI(str(key_in.readlines()[0].split("\n")[0]))

##########################
#Send Data from todoist
##########################
add_comment(x_task_id, x_pg_num)