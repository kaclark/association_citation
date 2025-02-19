from pathlib import Path
import os
from simple_term_menu import TerminalMenu
from datetime import date
from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Attachment, Comment, Task

class Concept:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.citations = []
        self.propositions = {}
        self.deployed = False
        self.img_path = ""
        self.html_path = "concepts/" + self.name + ".html"

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description
    
    def get_citations(self):
        return self.citations

    def add_citation(self, citation):
        self.citations.append(citation)

    def get_propositions(self):
        return self.propositions

    def add_proposition(self, prop, citation):
        if prop in self.propositions:
            self.propositions[prop].append(citation)
        else:
            self.propositions[prop] = [citation]

    def get_deploy_status(self):
        return self.deployed

    def set_img_path(self, i_path):
        self.img_path = i_path

    def get_img_path(self):
        return self.img_path

    def get_html_path(self):
        return self.html_path

    def as_string(self):
        out_string_raw = [
            "&N\n", self.get_name(), 
            "\n&D\n", self.get_description(),
            "\n&C\n", '\n'.join(self.get_citations()),
            "\n&P\n", '\n'.join([k + "," + ','.join(v) for k,v in self.get_propositions().items()]),
            "\n&I\n", self.get_img_path(),
            "\n&H\n", self.get_html_path(),
            "\n&S\n", str(self.get_deploy_status())
        ]
        return ''.join(out_string_raw)

def load_todoist():
    #access api token
    with open("api.token", "r") as key_in:
        api = TodoistAPI(str(key_in.readlines()[0].split("\n")[0]))
    return api

def get_section(s_id):
    try:
        titles = xapi.get_tasks(section_id=s_id)
        return titles
        #title = api.get_task(task_id=7480248679)
    except Exception as error:                        
        print(error)

def format_citation(c_info):
    #c_info dict with citation comment obj text, id, parent task id, and comment time
    #after the @@@@ oddly formatted string features can exist. We can only guarantee homogeneity for the info prefix
    f_string = c_info['t_id'] + ":" + c_info['c_id'] + "," + c_info['c_time'] + "@@@@" + c_info["text"]
    return f_string

def get_comments_indexed_by_c_id(t_id):
    x_comments = comments_from_task_id(t_id)
    scan_select = {}
    for x_comment in x_comments:
        c_info = {
                "text": x_comment.content,
                "c_id": x_comment.id,
                "t_id": t_id,
                "c_time": x_comment.posted_at.split(".")[0]
                }
        scan_select[x_comment.content] = (format_citation, c_info)
    return set_menu(list(scan_select.keys()), scan_select)

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

def prompt_citation_association(section_id):
    return lvs_select(get_section(section_id))

def Samkhya_Testing():
    samkhya = Concept("Samkhya", "Rationalistic School of Hindu Philosophy")
    cit_1 = prompt_citation_association(140213544)
    samkhya.add_citation(cit_1)
    samkhya.add_proposition("Samkhya* ~=(Suffering Foundational for Soteriology)= Buddhism**", cit_1)
    samkhya.set_img_path("include/img/samkhya.png")
    print(samkhya.as_string())
    #titles = get_section(140213544)
    #lvs_select(titles)

#=========RUNS==========
xapi = load_todoist()
Samkhya_Testing()
