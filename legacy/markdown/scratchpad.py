

#Ps-Dionysius has this pattern of random newline characters. I have been collapsing everything into one line and then separating the line at the period since that will still be rendered as a flowing paragraph in Markdown. Since this pattern seems pretty set, I'm going to automate this read-write operation
def strip_newlines(fd):
    with open(fd, "r") as f_in:
        data = f_in.read()
    no_newlines = "".join(data.split("\n"))
    no_tab = "".join(no_newlines.split("\t"))
    return no_tab

def newline_each_sentence(txt_blob):
    lined_out = txt_blob.replace(".", ".\n")
    return lined_out

def write_file(data, fd):
    with open(fd, "w") as f_out:
        f_out.write(data)

def parse_dionysius():
    divine_names_data = strip_newlines("episcripture/ps-dionysius/divine_names.md")
    cleaner_data = newline_each_sentence(divine_names_data)
    write_file(cleaner_data, "episcripture/ps-dionysius/divine_names_clean.md")

'''
LATEX SCRATCHPAD
    f(x)= 
    \begin{cases}
        \frac{x^2-x}{x},& \text{if } x\geq 1\\
                    0,              & \text{otherwise}
        \end{cases}

f(x)= \begin{cases} \frac{x^2-x}{x},& \text{if } x\geq 1\\0,& \text{otherwise} \end{cases}


\left\{
\begin{array}{ll}
      1 & h(x^{(i)}) \neq y^{(i)} \\
                    0 & otherwise \\
              \end{array} 
      \right.


\[ \left\{\begin{array}{ll}1 & h(x^{(i)}) \neq y^{(i)} \\0 & otherwise \\ \end{array} \right. \]
'''
