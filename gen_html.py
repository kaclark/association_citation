from PyPDF2 import PdfReader
import tempfile
import urllib.request
import PyPDF2
import io
import os

import sys
from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Attachment, Comment, Task

def gen_head(title, wtype="main"): 
    if wtype == "main":
        return f'''<html><head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>{title}</title>
        <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="include/main.css"/>
        <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
        </head>
        <body>
        '''
    elif wtype == "wiki" or wtype == "readable":
        return f'''<html><head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>{title}</title>
        <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="../include/main.css"/>
        </head>
        <body>
        '''

def gen_banner():
    return f''' <div class="content">
    <h1>Association Citation</h1>
	<div class='teaser-box'>
	<img class='teaser-img' src='include/img/pixel_book.jpg'></img>
	</div>
	<h2>Stage 3: Dynamic ScanHub<h2>
    </div>
    '''

def gen_p(text):
    return f'<div class="content" id="content"><p id="entry">{text}</p></div>'

def gen_readp(text):
    return f'''<p id="page">{text}</p>'''

def gen_pagenum(pagenum):
    return f'''<div id="pagenum"><p>{pagenum}</p></div>'''

def gen_tail():
    return f'''</div>
    </body>
    </html>
    '''

def gen_download_p(displayname, link, codename):
    nlink = "routes/" + codename + ".html"
    rlink = "readable/" + codename + ".html"
    return f'''<a href={link} download={displayname}>{displayname}</a>
        <a href={nlink}><p style="text-align:right">Highlight Stream</p></a>
        <a href={rlink}><p style="text-align:right">Read Online</p></a>
        <br>'''

def strip_underscores(blurb):
    return " ".join(blurb.split("_"))

def gen_readable(pageout, URL):
    print(URL)
    def remove_newlines(raw_text):
        split_lines = raw_text.split("\n")
        return (split_lines[0]," ".join(split_lines[1:-1]), split_lines[-1])
                
    req = urllib.request.Request(URL, headers={'User-Agent' : "Magic Browser"})
    remote_file = urllib.request.urlopen(req).read()
    remote_file_bytes = io.BytesIO(remote_file)
    pdfdoc = PyPDF2.PdfReader(remote_file_bytes)

    output_html = ""
    output_html += gen_head(strip_underscores(pageout), wtype="readable")
    output_html += "<div class='content' id='content'>"
    for i in range(len(pdfdoc.pages)):
        page_data = remove_newlines(pdfdoc.pages[i].extract_text())
        output_html += gen_pagenum(str(page_data[0]))
        output_html += gen_readp(str(page_data[1]))
        output_html += gen_pagenum(str(page_data[2]))

    output_html += "</div>"
    output_html += gen_tail()

    with open("readable/" + pageout + ".html", "w") as html_out:
        html_out.write(output_html)


def gen_wiki_page(codename):
    wiki = ""
    wiki += gen_head(codename, wtype="wiki")
    wiki += gen_p(strip_underscores(codename))
    try:
        with open("include/notes/" + codename + ".note", "r") as note_in:
            for line in [l.split("\n")[0] for l in note_in.readlines()]:
                pg_num = line.split(",")[-1]
                quote = ",".join(line.split(",")[:-1])
                if "??" in pg_num:
                    wiki += gen_p(quote)
                else:
                    wiki += gen_p(quote + " (pg " + pg_num + ")")
    except FileNotFoundError:
        with open("include/notes/" + codename + ".note", "w") as note_out:
            note_out.write("")
        wiki += gen_p("coming soon")
    wiki += gen_tail()

    with open("routes/" + codename + ".html", "w") as wiki_out:
        wiki_out.write(wiki)


def gen_book_table():
    #creates the html for the main body of the index and all supporting pages that link from there
    table = f'<div class="content" id="content">'
    #for each book, add gen p with a href
    table_content = {"paper": [], "dissertation":[], "book": []}
    with open("include/main_table_data.csv", "r") as table_data:
        for line in [l.split("\n")[0] for l in table_data.readlines()]:
            name, link, text_type, codename = line.split(",")
            table_content[text_type].append((name, link, codename))
            gen_wiki_page(codename)
            if not os.path.isfile("readable/" + codename + ".html"):
                gen_readable(codename, link)
    table += "<h1>Phase 2: Digital Library</h1>" 
    table += "<h1>Papers</h1>"
    for paper_data in table_content["paper"]:
        table += gen_download_p(paper_data[0], paper_data[1], paper_data[2])
    table += "<h1>Dissertations</h1>"
    for dissertation_data in table_content["dissertation"]:
        table += gen_download_p(dissertation_data[0], dissertation_data[1], dissertation_data[2])
    table += "<h1>Books</h1>"
    for book_data in table_content["book"]:
        table += gen_download_p(book_data[0], book_data[1], book_data[2])
    table += "</div>"
    return table
            

    table += f'</div>'

def gen_index():
    index = ""
    index += gen_head("Association Citation", wtype="main")
    index += gen_banner()
    index += create_link_table(get_section(140213544, load_todoist()))
    index += gen_book_table()
    index += gen_tail()

    with open("index.html", "w") as index_out:
        index_out.write(index)

def refresh():
    gen_index()

def load_todoist():
    #access api token
    with open("api.token", "r") as key_in:
        api = TodoistAPI(str(key_in.readlines()[0].split("\n")[0]))
    return api

def get_section(s_id, api):
    try:
        titles = api.get_tasks(section_id=s_id)
        return titles
        #title = api.get_task(task_id=7480248679)
        #return title 
    except Exception as error:
        print(error)

def format_title(title):
    title1 = title.replace("[", "")
    title2 = title1.replace("]", ": ")
    title = title2.replace("_", " ")
    return title

def get_table_row(title_task):
    content = title_task.content
    c_date = title_task.created_at.split("T")[0]
    x_year, x_month, x_day = c_date.split("-")
    cc_date = x_month + "/" + x_day + "/" + x_year[2:]
    clink = "livescans/" + content + ".html"
    p_content = format_title(content)
    return f'''<tr><td>
    <tr><td><a href={clink}>{p_content}</a></td>
    <td>{cc_date}</td>
    </tr>
    '''
def create_link_table(titles):
    #titles should be full task objects
    table_html = "<div class='content' id='content'>"
    table_html += "<h1>Livescans</h1>"
    table_html += "<table class='livescans'>"
    #todo: sort by latest comment and supply that date
    titles.reverse()
    for title in titles:
        table_html += get_table_row(title)
    table_html += "</table></div>"
    return table_html
    
#========RUNS=========#
refresh()
