from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Attachment, Comment, Task
import numpy as np
import sys

def comments_from_task_id(t_id):
    try:
        comments = api.get_comments(task_id=t_id)
        return np.array([c.content for c in comments])
    except Exception as error:
        print(error)

#access api token
with open("api.token", "r") as key_in:
    api = TodoistAPI(str(key_in.readlines()[0].split("\n")[0]))

print(comments_from_task_id(sys.argv[1]))
