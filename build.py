#!/usr/bin/env python

# shape of html

title_tag = "TITLE-STRING"
menu_tag = "MENU-HTML"
content_tag = "CONTENT-HTML"
filename_tag = "FILENAME-DOT-HTML"

format = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>TITLE-STRING</title>
<link rel="stylesheet" href="main.css">
</head>
<body>
<header>
<img src="top.png" alt="CADE-26">
</header>
<nav>
MENU-HTML
</nav>
<article><div class="content">
CONTENT-HTML
</div></article>
<footer style="text-align:center;">
<div style="width: 100%; text-align:left; padding-left: 15px; padding-top: 10px; padding-bottom: 10px;">CADE-26 is grateful for sponsorship from:</div>
<a href="https://www.microsoft.com/en-us/research/"><img src="msr.png" style="width: 200px; padding-left:30px;" alt="Microsoft Research"/></a>
<a href="http://international.goteborg.se/"><img src="gbg.png" style="width: 200px; padding-left:30px;" alt="Gothenburg City"/></a>
<a href="http://www.chalmers.se/en/areas-of-advance/ict/Pages/default.aspx"><img src="aoa.png" style="width: 280px; padding-left:30px;" alt="Information and Communication Technologies Chalmers Area of Advance"/></a><br>
</footer>
</body>
</html>"""

validate_link = """ - <a style="color:grey;" href="https://validator.w3.org/nu/?doc=http%3A%2F%2Fwww.cse.chalmers.se%2F~myreen%2Fcade-26%2FFILENAME-DOT-HTML">FILENAME-DOT-HTML</a>"""

# a list, where each item is: filename, title, in_menu, is_local page

pages = [("index","Home",True,True),
         ("workshops","Workshops &amp; Tutorials",True,True),
         ("http://www.cs.miami.edu/~tptp/CASC/26/","CASC",True,False),
         ("org","Organization",True,True),
         ("venue","Venue &amp; Hotels",True,True),
         ("bledsoe","Woody Bledsoe Student Travel Awards at CADE 2017",False,True)]

# generate html

def get_menu(filename):
  str = '<ul>\n'
  for (filename,title,in_menu,is_local) in pages:
    if in_menu:
      if is_local:
        str += '<li><a href="'+filename+'.html">'+title+'</a></li>\n'
      else:
        str += '<li><a href="'+filename+'" target="_blank">'+title+'</a></li>\n'
  str += '</ul>\n'
  return str

validate_html = ""

for (filename,title,in_menu,is_local) in pages:
  if (is_local):
    with open(filename+'.txt', 'r') as content_file:
      content = content_file.read()
    html = format.replace(title_tag,"CADE-26: " + title)
    html = html.replace(menu_tag,get_menu(filename))
    html = html.replace(content_tag,content)
    html = html.replace(filename_tag,filename+'.html')
    with open(filename+'.html', 'w') as html_file:
      html_file.write(html)
    validate_html += validate_link.replace(filename_tag,filename+'.html') + '\n'

validate_html = """<html><head><link rel="stylesheet" href="style2.css"></head><body><pre><b>Validate:</b>""" + '\n' + validate_html + "</pre></body></html>"

with open('validate.html', 'w') as html_file:
  html_file.write(validate_html)
