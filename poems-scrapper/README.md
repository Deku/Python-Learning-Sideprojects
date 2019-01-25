# Daily Poems Scrapper

## What is this?

This is a web scrapper that feeds on <http://poems.com/today.php> to get a poem (different everyday), and exports it to PDF.

## How to run

1. Execute `bootstrap.sh` to create the virtualenv folder and install dependencies
2. Execute `app.py` to get your poem

## What did I learn in this project?

- How to use virtual environments with `venv`
- How to use `requests` to get raw HTML from web pages
- How to use `BeautifulSoup` to wrangle data from HTML
- How to print in colors to the console
- How to generate a PDF document using `ReportLab`
- Open a file from Python using `subprocess.Popen()`

## References

- <https://realpython.com/python-web-scraping-practical-introduction/>
- <https://realpython.com/python-virtual-environments-a-primer/>
- <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>
- <http://docs.python-requests.org/en/master/>
- <https://medium.com/@vonkunesnewton/generating-pdfs-with-reportlab-ced3b04aedef>
