from bs4 import BeautifulSoup

def read_html(filename):
    file_content = open(filename, mode='r')
    return file_content.read()