import json

def construct_css(config_path):

    with open(config_path, 'r') as file:
    	config = json.load(file)

    # Accessing the data
    css_filepath = config['css_config']['filepath']

    body_font = config['css_config']['body_style']['font-family']
    body_wwrap = config['css_config']['body_style']['word-wrap']

    p_align = config['css_config']['p_style']['p_align']
    p_fontsize = config['css_config']['p_style']['p_fontsize']
    p_margin_left = config['css_config']['p_style']['margin-left']
    p_margin_right = config['css_config']['p_style']['margin-right']

    h1_align = config['css_config']['h1_style']['text-align']
    h1_fontsize = config['css_config']['h1_style']['fontsize']

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

    def add_font():
         return f'''

@font-face {{
  font-family: "CascadiaCode";
  src: url("../fonts/CascadiaCode-Regular.woff2") format('woff2');
}}

@font-face {{
  font-family: "CascadiaCode";
  src: url("../fonts/CascadiaCode-SemiBold.woff2") format('woff2');
  font-weight: bold;
}}

@font-face {{
  font-family: "CascadiaCode";
  src: url("../fonts/CascadiaCode-SemiBoldItalic.woff2") format('woff2');
  font-weight: bold;
  font-style: italic;
}}

@font-face {{
  font-family: "CascadiaCode";
  src: url("../fonts/CascadiaCodeItalic.woff2") format('woff2');
  font-style: italic;
}}


'''


    def style_body(body_font, body_wwrap):
        return f'''
body {{
    font-family: {body_font};
    word-wrap:{body_wwrap};
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
    def style_h1(text_align, fontsize):
        return f'''
h1 {{
    text-align: {text_align};
    font-size: {fontsize};
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
    css_payload += add_font()
    css_payload += style_body(body_font, body_wwrap)
    css_payload += style_p(p_align, p_fontsize, p_margin_left, p_margin_right)
    css_payload += style_h1(h1_align, h1_fontsize)
    css_payload += style_div(div_width, div_padding, div_margin)
    css_payload += style_navbar(navbar_color, navbar_height)
    css_payload += style_bannerimg(bannerimg_display, bannerimg_margin_left, bannerimg_margin_right, bannerimg_width, bannerimg_height)
    
    #Deliver Payload to Filesystem
    with open(css_filepath, "w") as css_out:
        css_out.write(css_payload)

construct_css("config.json")

