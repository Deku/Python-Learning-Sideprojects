from utils import get_webpage, log_error
from pdfdoc import create_pdf
from bs4 import BeautifulSoup
from subprocess import Popen

raw_html = get_webpage('http://poems.com/today.php')
html = BeautifulSoup(raw_html, 'html.parser')
title = html.select('#poem_container #page_title')[0].text
content = html.select('#poem_container #poem p')

try:
    create_pdf(title, content)
    Popen(['poem.pdf'], shell=True)
except PermissionError as ex:
    log_error('Error while generating the PDF document: {0}'.format(str(ex)))