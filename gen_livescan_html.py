#usage: python gen_highlight_page.py #task_id

import sys
from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Attachment, Comment, Task

##########################
#Helper Functions
##########################

def strip_underscores(string):
    return " ".join([f.capitalize() for f in string.split("_")])

def comments_from_task_id(t_id):
    try:
        comments = api.get_comments(task_id=t_id)
        return [c.content for c in comments]
    except Exception as error:
        print(error)

def task_content_from_task_id(t_id):
    try:
        task = api.get_task(task_id=t_id)
        return task.content
    except Exception as error:
        print(error)

def description_from_task_id(t_id):
    try:
        task = api.get_task(task_id=t_id)
        return task.description
    except Exception as error:
        print(error)

##########################
#Html Generation
##########################

def gen_head(title):
    return f'''<html><head>
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="../include/main.css"/>
    </head>'''

def gen_header(title, ref_info):
    mtitle = strip_underscores(title)
    return f'''
    <body>
    <div class="content">
        <h1>{mtitle}</h1>
        <p>{ref_info}</p>
    </div>
    <div class="content" id="content">
    '''

def gen_p(content):
    return f'''
    <p>{content}</p>
    '''

def gen_tail():
    return f'''
    </div>
    </body>
    </html>
    '''

##########################
#INFORMATION SETUP
##########################

#Gather the input from user
task_id = sys.argv[1]

#access api token
with open("api.token", "r") as key_in:
    api = TodoistAPI(str(key_in.readlines()[0].split("\n")[0]))

##########################
#Extract Data from todoist
##########################
x_title = task_content_from_task_id(task_id)
ref_info = description_from_task_id(task_id)
x_comments = comments_from_task_id(task_id)

##########################
#Build html string
##########################
html_payload = ""
html_payload += gen_head(x_title)
html_payload += gen_header(x_title, ref_info)
for x_comment in x_comments:
    html_payload += gen_p(x_comment)
html_payload += gen_tail()

with open("livescans/" + x_title + ".html", "w") as html_out:
    html_out.write(html_payload)