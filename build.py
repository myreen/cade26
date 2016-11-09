#!/usr/bin/env python

# shape of html

title_tag = "TITLE-STRING"
menu_tag = "MENU-HTML"
content_tag = "CONTENT-HTML"

format = """<!DOCTYPE html>
<html>
<head>
<title>TITLE-STRING</title>
<link rel="stylesheet" href="main.css">
</head>
<body>
<header>
<img src="top.png">
</header>
<nav>
MENU-HTML
</nav>
<article><div class="content">
CONTENT-HTML
</div></article>
<footer>
</footer>
</body>
</html>"""

# a list, where each item is: filename, title, is-item-on-main-nav

pages = [("start","Home",True),
         ("org","Organization",True),
         ("venue","Venue &amp; Hotels",True)]

# generate html

def get_menu(filename):
  str = '<ul>\n'
  for (filename,title,in_menu) in pages:
      if in_menu:
          str += '<li><a href="'+filename+'.html">'+title+'</a></li>\n'
  str += '</ul>\n'
  return str

for (filename,title,in_menu) in pages:
  with open(filename+'.txt', 'r') as content_file:
     content = content_file.read()
  html = format.replace(title_tag,"CADE-26: " + title)
  html = html.replace(menu_tag,get_menu(filename))
  html = html.replace(content_tag,content)
  with open(filename+'.html', 'w') as html_file:
     html_file.write(html)
