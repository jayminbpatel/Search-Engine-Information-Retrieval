from bs4 import BeautifulSoup
from counter import *
path="F:\CS454-Python\en\\articles\(\\1\\5\(15810)_1994_JR1_9064.html"

mainList=[]
class mainNode:
    word=""
    subList=[]
x = open(path, mode='r')
#print x.read() Why does this happen?
#file = str(x.read())
#wordList = file.split()
#print "DOC" in wordList
#print wordList
#for each_word in wordList:
#    m = mainNode()
#    m.word = each_word
#    m.subList.append(path)
#    mainList.append(m)
#for each_node in mainList:
#    print each_node.subList
soup = BeautifulSoup(x, 'html.parser')
#print(soup.prettify())
#print(soup.get_text())
body = soup.get_text().split()
counter_hash = {}
#def counter(word_array):
#    for each_word in word_array:
#        freq = word_array.count(each_word)
#        counter_hash[each_word] = freq
counter(body)
#for each_key in counter_hash:
#    print counter_hash[each_key]+" : "+each_key
#for w in sorted(counter_hash, key=counter_hash.get, reverse=True):
#  print w, counter_hash[w]