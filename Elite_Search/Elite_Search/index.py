from bs4 import BeautifulSoup
from counter import *
path="F:\CS454-Python\en\\articles\(\\1\\5\(15810)_1994_JR1_9064.html"

mainList=[]
class mainNode:
    word=""
    subList=[]
x = open(path, mode='r')

soup = BeautifulSoup(x, 'html.parser')

body = soup.get_text().split()
counter_hash = {}

counter(body)
