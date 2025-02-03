import os

from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Attachment, Comment, Task
import sys

import convertdate
import pytz
import datetime

with open("api.token", "r") as key_in:
	api = TodoistAPI(str(key_in.readlines()[0].split('\n')[0]))

def comments_from_task_id(t_id):
	try:
		comments = api.get_comments(task_id=t_id)
		return [c for c in comments]
	except Exception as error:
		print(error)

def rss_item(nadi_stamp, mdlink, post_category):
  return f''' 
  <item>
    <title>{nadi_stamp}</title>
    <link>{mdlink}</link>
    <description>{post_category}</description>
  </item>

'''

def process_posts():
	pseudo_post_id = "8049968003"
	pseudo_posts = comments_from_task_id(pseudo_post_id)

	with open("./data/seen_posts.txt", "r") as postids_in:
		postid_lines = [l.split('\n')[0] for l in postids_in.readlines()]

	seen_postids = set()
	for postid in postid_lines:
		seen_postids.add(postid)
	xml_payload = ""
	new_posts = set()
	post_info = {}
	mdlinks = []
	for pseudo_post in pseudo_posts:
		if pseudo_post.id not in seen_postids:
			new_posts.add(pseudo_post.id)
			date_info_e, time_info_e = pseudo_post.posted_at.split("T")
			gyear, gmonth, gday = date_info_e.split("-")
			lhour, lmin, lsec = time_info_e.split(".")[0].split(":")
			minutes_total = int(lhour)*60 + int(lmin)
			nadis = round(minutes_total / 24, 2)
			byear, bmonth, bday = convertdate.bahai.from_gregorian(int(gyear), int(gmonth), int(gday))
			nadistamp = str(nadis).replace(".","n") + "x" + str(bday) + str(bmonth) + str(byear) 
			marked_payload = ""
			marked_payload += f'''# {nadis} Nadis {bday} {bmonth} {byear}\n\n'''
			marked_payload += f'''{pseudo_post.content}\n'''
			markedout_path = "/posts/" + nadistamp + ".md"
			with open("." + markedout_path, "w") as marked_out:
				marked_out.write(marked_payload)
			post_category = pseudo_post.content.split("]")[0].split('[')[-1]
            siteurl = "https://kaclark.github.io/association_citation"
			xml_payload += rss_item(nadistamp, siteurl + markedout_path, post_category)

			mdlinks.append(siteurl + markedout_path)
			#posts_info[pseudo_post.posted_at] = pseudo_post.content
	#take snapshot in case something odd happens 
	os.system("cp ./data/posts.xml ./data/posts.xml.snapshot")
	os.system("cp ./data/seen_posts.txt ./data/seen_posts.txt.snapshot")
	os.system("cp ./index.html ./data/index.html.snapshot")

	with open("./data/posts.xml", "r") as xml_in:
		xml_lines = [l.split('\n')[0] for l in xml_in.readlines()]
	
	#define with imaginary values until promoted	
	payload_prefix = "-1"
	payload_suffix = "-1"
	payload_construct = ""

	#search for end of feed
	for l_ind, line in enumerate(xml_lines):
		if "</channel>" in line:
			payload_prefix = xml_lines[:l_ind]
			payload_suffix = xml_lines[l_ind:]

	payload_construct += '\n'.join(payload_prefix)
	payload_construct += xml_payload
	payload_construct += "\n".join(payload_suffix)

	with open("./data/posts.xml", "w") as xml_out:
		xml_out.write(payload_construct + "\n")

	with open("./data/seen_posts.txt", "a") as posts_record:
		posts_record.write("\n".join(list(new_posts)) + "\n")

	with open("index.html", "r") as html_in:
		html_lines = [l.split('\n')[0] for l in html_in.readlines()]
	mdblock_prefix = "-1"
	mdblock_suffix = "-1"
	for hl_ind, html_line in enumerate(html_lines):
		if "<!--INJECT-->" in html_line:
			mdblock_prefix = html_lines[:hl_ind+1]
			mdblock_suffix = html_lines[hl_ind+1:]

	mdlinks.reverse()
	mdblock_payload = "\n\n" + "\n\n".join([f'''<md-block src="{mdlink}"></md-block>''' for mdlink in mdlinks])

	index_construct = ""
	index_construct += '\n'.join(mdblock_prefix)
	index_construct += mdblock_payload + "\n"
	index_construct += "\n".join(mdblock_suffix)

	with open("index.html", "w") as html_out:
		html_out.write(index_construct + "\n")

def construct_css(config):

    # Accessing the data
    css_filepath = config['css_config']['filepath']

    body_font = config['css_config']['body_style']['font-family']

    p_align = config['css_config']['p_style']['p_align']
    p_fontsize = config['css_config']['p_style']['p_fontsize']
    p_margin_left = config['css_config']['p_style']['margin-left']
    p_margin_right = config['css_config']['p_style']['margin-right']

    h1_align = config['css_config']['h1_style']['text-align']

    div_width = config['css_config']['div_style']['width']
    div_padding = config['css_config']['div_style']['padding']
    div_margin = config['css_config']['div_style']['margin']

    navbar_color = config['css_config']['navbar_style']['background_color']
    navbar_height = config['css_config']['navbar_style']['height']


    bannerimg_display = config['css_config']['bannerimg_style']['display']
    bannerimg_margin_left = config['css_config']['bannerimg_style']['margin-left']
    bannerimg_margin_right = config['css_config']['bannerimg_style']['margin-right']
    bannerimg_width = config['css_config']['bannerimg_style']['width']
    bannerimg_height = config['css_config']['bannerimg_style']['height']

    def style_body(body_font):
        return f'''
body {{
    font-family: {body_font}
}}
                '''

    def style_p(palign, pfontsize, p_margin_left, p_margin_right):
        return f'''
p {{
    text-align: {palign};
    font-size: {pfontsize};
    margin-left: {p_margin_left};
    margin-right: {p_margin_right};
}}

                '''
    def style_h1(text_align):
        return f'''
h1 {{
    text-align: {text_align}
}}
                '''

    def style_div(div_width, div_padding, div_margin):
        return f'''
div {{
    width: {div_width};
    padding: {div_padding};
    margin: {div_margin};

}}

            '''

    def style_navbar(bcolor, bheight):
        return f'''
ul {{
    list-style-type: none;
    margin: 0;
    padding: 0;
    background-color: {bcolor};
    height: {bheight};
}}

li {{
    display: inline;
    height: 100%;
    margin: auto;
}}

li + li {{
    margin : 1em;
}}

div.navbardiv {{
    margin: auto;
}}

            '''

    def style_bannerimg(bannerimg_display, bannerimg_margin_left, bannerimg_margin_right, bannerimg_width, bannerimg_height):
        return f'''
.bannerimg {{
    display: {bannerimg_display};
    margin-left: {bannerimg_margin_left};
    margin-right: {bannerimg_margin_right};
    width: {bannerimg_width};
    height: {bannerimg_height};

}}

                '''
    
    #Construct CSS Payload
    css_payload = ""
    css_payload += style_body(body_font)
    css_payload += style_p(p_align, p_fontsize, p_margin_left, p_margin_right)
    css_payload += style_h1(h1_align)
    css_payload += style_div(div_width, div_padding, div_margin)
    css_payload += style_navbar(navbar_color, navbar_height)
    css_payload += style_bannerimg(bannerimg_display, bannerimg_margin_left, bannerimg_margin_right, bannerimg_width, bannerimg_height)
    
    #Deliver Payload to Filesystem
    with open(css_filepath, "w") as css_out:
        css_out.write(css_payload)

process_posts()

