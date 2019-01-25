from utils import get_page, log_title, log_paragraph
from bs4 import BeautifulSoup

raw_html = get_page('http://poems.com/today.php')
html = BeautifulSoup(raw_html, 'html.parser')
title = html.select('#poem_container #page_title')[0]
content = html.select('#poem_container #poem p')

log_title(title.text)

for p in content:
    log_paragraph(p.text)
