def gen_head(title, wiki=False): 
    if not wiki:
        return f'''<html><head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>{title}</title>
        <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="include/main.css"/>
        </head>
        <body>
        '''
    else:
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
	<h2>Stage 1: Digital Library<h2>
    </div>
    '''

def gen_p(text):
    return f'<div class="content" id="content"><p id="entry">{text}</p></div>'

def gen_tail():
    return f'''</div>
    </body>
    </html>
    '''

def gen_download_p(displayname, link, codename):
    nlink = "routes/" + codename + ".html"
    return f'<a href={link} download={displayname}><p class="maintable">{displayname}</p></a><a href={nlink}><p>📄</p></a><br>'

def generate_wiki_page(codename):
    wiki = ""
    wiki += gen_head(codename)
    #for each note entry, add a p
    #TODO: lookup codename + ".note"; if fail, gen new
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
    index += gen_head("Association Citation")
    index += gen_banner()
    index += gen_book_table()
    index += gen_tail()

    with open("index.html", "w") as index_out:
        index_out.write(index)

gen_index()
