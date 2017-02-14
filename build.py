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
<a href="http://www.chalmers.se/en/areas-of-advance/ict/Pages/default.aspx"><img src="aoa.png" style="width: 280px; padding-left:30px;" alt="Information and Communication Technologies Chalmers Area of Advance"/></a><br><br>
<a style="color:grey;" href="https://validator.w3.org/nu/?doc=http%3A%2F%2Fwww.cse.chalmers.se%2F~myreen%2Fcade-26%2FFILENAME-DOT-HTML">validate</a>
</footer>
</body>
</html>"""

# a list, where each item is: filename, title, is-item-on-main-nav

pages = [("index","Home",True),
         ("workshops","Workshops &amp; Tutorials",True),
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
  html = html.replace(filename_tag,filename+'.html')
  with open(filename+'.html', 'w') as html_file:
     html_file.write(html)
