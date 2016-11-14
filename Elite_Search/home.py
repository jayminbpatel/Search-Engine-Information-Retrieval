import os
import time

import json
import hashlib
from read_file import *
from write_html import *
from hash_file import *
from index_file_content import *
from global_variables import *

mainList = []  # add all nodes to this list
wordHashMap={}

#Step 1+

mainDirectory = 'C:\\Users\\Jaymin\\Downloads\\en';  # root path
test_path="C:\\Users\\Jaymin\Downloads\\en\\articles\(\\1\\5"

def test_crawl():
    for root, dirs, files in os.walk(test_path):
        for each_filename in files:
            filename = str(each_filename)
            file_path = os.path.realpath(os.path.join(root, filename))
#read file
            file_content = read_html(file_path)
#get hashCode
            hash_filename = get_hash(file_path,filename )
#write file
            write_html(file_content, hash_filename)
            print "Processing : "+ filename
#process file
    file_array = os.listdir("storage")
    for each_file in file_array:
        print each_file
        index_file_content("storage/"+each_file)
def crawl():
    for root, dirs, files in os.walk(mainDirectory):
        for each_filename in files:
            print "Crawling : "+each_filename
            filename = str(each_filename)
            file_path = os.path.realpath(os.path.join(root, filename))

#read file
            file_content = read_html(file_path)
#get hashCode
            hash_filename = get_hash(file_path,filename)
#write file
            write_html(file_content, hash_filename)
#process file
#process file
    file_array = os.listdir("storage")
    for each_file in file_array:
        print each_file
        index_file_content("storage/"+each_file)

crawl()
for each_word in word_hash_map:
    print each_word+":"+str(word_hash_map[each_word])