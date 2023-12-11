from pathlib import Path
import os
from simple_term_menu import TerminalMenu
from datetime import date
from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Attachment, Comment, Task

def load_todoist():
    #access api token
    with open("api.token", "r") as key_in:
        api = TodoistAPI(str(key_in.readlines()[0].split("\n")[0]))
    return api

def get_section(s_id):
    try:
        titles = xapi.get_tasks(section_id=s_id)
        return titles
        #title = api.get_task(task_id=7480248679)                                                   #return title
    except Exception as error:                        print(error)

def get_comments_indexed_by_c_id(t_id):
    x_comments = comments_from_task_id(t_id)
    scan_select = {}
    for x_comment in x_comments:
        c_info = {
                "text": x_comment.content,
                "c_id": x_comment.id,
                "t_id": t_id
                }
        #TODO: write function to associate chosen comment generative data with concept
        scan_select[x_comment.content] = c_info
        print(c_text, c_id)
    return "works"

def comments_from_task_id(t_id):
    try:
        comments = xapi.get_comments(task_id=t_id)
        return comments
    except Exception as error:
        print(error)

def lvs_select(lvs):
    #livescan names with task ids as input
    #lvs: [(lvs_name, lvs_t_id) | for all lv in lvs]
    lvs_names = [e.content for e in lvs]
    ########lvs_t_ids = [e.id for e in lvs]
    #TODO: Section Tasks => Livescan Titles
    menu_choices = lvs_names

    #to make a menu we need choices
    #and functions these choices map to
    #functions are stored with their parameters
    #that way they don't run until selected
    
    lvs_map = {lv.content: (get_comments_indexed_by_c_id, lv.id) for lv in lvs}
    #TODO: Add Create Livescan here like so
    #choice_outcome_map = {**{"[Custom]": (get_pseud_elt, ""), "[break]": (str, "break")}, **elt_map}

    #set_menu(elt_names, elt_map, actualize_function)
    return set_menu(menu_choices, lvs_map)

def set_menu(options, options_hash_table):

    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    return actualize_function(options_hash_table[options[menu_entry_index]])

def actualize_function(func_param_pair):
    #func_param_pair: (function, paramters)
    func, params = func_param_pair
    return func(params)

def main_loop():
    titles = get_section(140213544)
    lvs_select(titles)

#=========RUNS==========
xapi = load_todoist()
main_loop()
