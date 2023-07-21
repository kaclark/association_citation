from PyPDF2 import PdfReader
import tempfile
import urllib.request
import PyPDF2
import io

def gen_head(title, wtype="main"): 
    if wtype == "main":
        return f'''<html><head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>{title}</title>
        <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="include/main.css"/>
        </head>
        <body>
        '''
    elif wtype == "wiki":
        return f'''<html><head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>{title}</title>
        <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="../include/main.css"/>
        </head>
        <body>
        '''

    elif wtype == "readable":
        return f'''<html><head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>{title}</title>
        <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="../include/textflow.css"/>
        </head>
        <body>
        '''


def gen_banner():
    return f''' <div class="content">
    <h1>Association Citation</h1>
	<div class='teaser-box'>
	<img class='teaser-img' src='include/img/pixel_book.jpg'></img>
	</div>
	<h2>Stage 1: Digital Library<h2>
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
        <a href={nlink}><p>Highlight Stream📄</p></a>
        <a href={rlink}><p>Read Online📄</p></a>
        <br>'''

def strip_underscores(blurb):
    return " ".join(blurb.split("_"))

def generate_readable(pageout, URL):
    print(URL)
    def remove_newlines(raw_text):
        return " ".join(raw_text.split("\n"))
                
    req = urllib.request.Request(URL, headers={'User-Agent' : "Magic Browser"})
    remote_file = urllib.request.urlopen(req).read()
    remote_file_bytes = io.BytesIO(remote_file)
    pdfdoc = PyPDF2.PdfReader(remote_file_bytes)

    output_html = ""
    output_html += gen_head("PDF VIEWER", wtype="readable")
    for i in range(len(pdfdoc.pages)):
        output_html += gen_readp(remove_newlines(pdfdoc.pages[i].extract_text()))
        output_html += gen_pagenum(str(i))
    output_html += gen_tail()

    with open("readable/" + pageout + ".html", "w") as html_out:
        html_out.write(output_html)


def generate_wiki_page(codename):
    wiki = ""
    wiki += gen_head(codename, wtype="wiki")
    wiki += gen_p(strip_underscores(codename))
    #for each note entry, add a p
    #TODO: lookup codename + ".note"; if fail, gen new
    try:
        with open("include/notes/" + codename + ".note", "r") as note_in:
            for line in [l.split("\n")[0] for l in note_in.readlines()]:
                pg_num = line.split(",")[-1]
                quote = "".join(line.split(",")[:-1])
                wiki += gen_p(quote + " (pg " + pg_num + ")")
    except FileNotFoundError:
        with open("include/notes/" + codename + ".note", "w") as note_out:
            note_out.write("")
        wiki += gen_p("coming soon")
    wiki += gen_tail()

    with open("routes/" + codename + ".html", "w") as wiki_out:
        wiki_out.write(wiki)


def gen_book_table():
    table = f'<div class="content" id="content">'
    #for each book, add gen p with a href
    table_content = {"paper": [], "dissertation":[], "book": []}
    with open("include/main_table_data.csv", "r") as table_data:
        for line in [l.split("\n")[0] for l in table_data.readlines()]:
            name, link, text_type, codename = line.split(",")
            print(name, text_type)
            table_content[text_type].append((name, link, codename))
            generate_wiki_page(codename)
            #TODO: make conditional generation and uncoment
            #generate_readable(codename, link)
    
    table += "<h4>Papers</h4>"
    for paper_data in table_content["paper"]:
        table += gen_download_p(paper_data[0], paper_data[1], paper_data[2])
    table += "<h4>Dissertations</h4>"
    for dissertation_data in table_content["dissertation"]:
        table += gen_download_p(dissertation_data[0], dissertation_data[1], dissertation_data[2])
    table += "<h4>Books</h4>"
    for book_data in table_content["book"]:
        table += gen_download_p(book_data[0], book_data[1], book_data[2])
    table += "</div>"
    return table
            

    table += f'</div>'

def gen_index():
    index = ""
    index += gen_head("Association Citation", wtype="main")
    index += gen_banner()
    index += gen_book_table()
    index += gen_tail()

    with open("index.html", "w") as index_out:
        index_out.write(index)

gen_index()
