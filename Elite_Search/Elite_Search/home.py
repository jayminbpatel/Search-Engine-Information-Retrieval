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
updated_hashMap = {}
mainDirectory = 'F:\\CS454-Python\\en';  # root path
test_path="F:\CS454-Python\en\\articles\(\\1\\5"
hash_filename_link = {}
search_results = []

def make_hash_link():
    for root, dirs, files in os.walk(mainDirectory):
        for each_filename in files:
            filename = str(each_filename)
            file_path = os.path.realpath(os.path.join(root, filename))
            hash_filename = get_hash(file_path,filename )
            hash_filename_link[hash_filename] = file_path
            print "Linking : "+filename
#    with open('file_links.json', mode='w+') as f:
#        json.dump(hash_filename_link, f)
    print "Hash Linking done"

#Step 1
def test_crawl():
#jsoning file hashes
#end jsonging file hashes
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
def index_content():
    file_array = os.listdir("storage")
    file_counter = 0
    for each_file in file_array:
        file_counter+=1
        print "Processing "+str(file_counter)+" : "+ each_file
        index_file_content("storage/"+each_file)

#for each_word in word_hash_map:
#    print each_word+":"+str(word_hash_map[each_word])

#Write JSON
def json_it():
    with open('store.json', mode='w+') as f:
        json.dump(word_hash_map, f)
def read_json():
    with open("store.json") as json_file:
        json_data = json.load(json_file)
        for each_line in json_data:
            print each_line+" : "+str(json_data[each_line])
            for each_value in json_data[each_line]:
                print each_value
def update_json():
    with open('store.json') as json_file:
        json_data = json.load(json_file)
        for each_word in json_data:
            new_hashMap={}
            for each_value in json_data[each_word]:
                print "Processing : "+each_value
                splitted_value = each_value.split(':')
                new_hashMap[splitted_value[1]] = splitted_value[0]
            updated_hashMap[each_word] = new_hashMap
        with open('updated.json', mode='w+') as f:
            json.dump(updated_hashMap, f)
word_count_final = 0
def print_updated_json(searchQuery):
    global word_count_final
    with open('updated.json') as json_file:
        json_data = json.load(json_file)
        for each_word in json_data:
            word_count_final += 1
#            print word_count_final
#            if searchQuery == each_word:
#                print each_word+":"+str(json_data[each_word])
#                break
            if searchQuery in each_word:
                print each_word

                for each_url in json_data[each_word]:
#                    print each_url
                    split_value = each_url.split("/")
#                    print split_value[1]
                    final_split_value = split_value[1].split('.')
                    x =  final_split_value[0]
#                    result_list.append(hash_filename_link[x])
                    print hash_filename_link[x]
                    search_results.append(hash_filename_link[x])
    return search_results

def rank():
    file_content = open('store.json', mode='r')
    json_text =  file_content.read()
    for each_line in json_text:
        print each_line

#make_hash_link()
#crawl()
#index_content()
#json_it()
#read_json()
#update_json()
#print_updated_json(searchQuery)
#rank()
