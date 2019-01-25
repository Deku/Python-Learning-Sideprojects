from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

class bcolors:
    HEADER = '\033[95m'
    PRIMARY = '\033[94m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_page(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as ex:
        log_error('Error during request to {0}: {1}'.format(url, str(ex)))
        return None

def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)

def log_error(msg):
    print(bcolors.ERROR + msg + bcolors.RESET)

def log_title(title):
    print(bcolors.HEADER + bcolors.SUCCESS + title + bcolors.RESET + '\r\n')

def log_paragraph(text):
    print(text.replace(u'\xa0', '') + '\r\n')
