from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Attachment, Comment, Task
import numpy as np
import sys
import argparse

parser = argparse.ArgumentParser(
                    prog='todo',
                    description='todoist cli',
                    epilog='Further API Documentation: https://developer.todoist.com/rest/v2/?python#overview')

parser.add_argument('-t', '--taskid')
parser.add_argument('-a', '--action')  

args = parser.parse_args()

def comments_from_task_id(t_id):
    try:
        comments = api.get_comments(task_id=t_id)
        return np.array([c.content for c in comments])
    except Exception as error:
        print(error)

#access api token
with open("api.token", "r") as key_in:
    api = TodoistAPI(str(key_in.readlines()[0].split("\n")[0]))

if args.action == "getComments":
    t_comments = comments_from_task_id(args.taskid)
    logval = str(args.action) + ":" + str(args.taskid) + " --> Array"
    print(t_comments, "\n", logval)


######################
###EXAMPLES
#####################
#Spandakarika
#python todo.py --taskid 7456224352 --action getComments

