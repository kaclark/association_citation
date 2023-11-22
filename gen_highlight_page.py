import sys
from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Attachment, Comment, Task
from simple_term_menu import TerminalMenu

#access api token
with open("api.token", "r") as key_in:
    api = TodoistAPI(str(key_in.readlines()[0].split("\n")[0]))

#usage: python gen_highlight_page.py #task_id
task_id = sys.argv[1]

def get_comment_json_by_id(t_id):
    try:
        comments = api.get_comments(task_id=t_id)
        return comments
    except Exception as error:
        print(error)

for x_comment in get_comment_json_by_id(task_id):
    print(x_comment.content)
