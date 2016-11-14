#import statements
import os
from hash_file import *
from bs4 import BeautifulSoup

#variables
mainDirectory = 'C:\\Users\\Jaymin\\Downloads\\en';  # root path
filename_hash_list = {}#stores all hash values of file paths
word_hash = {}#stores all words and their urls
#searchQuery = "Willem"
file_count = 0
#methods
def hash_link():
    global file_count
    for root, dirs, files in os.walk(mainDirectory):
        for each_filename in files:
            filename = str(each_filename)
            file_path = os.path.realpath(os.path.join(root, filename))
            hash_value = hash_filepath(file_path)
            filename_hash_list[hash_value] = file_path
            file_count+=1
            print hash_value +":"+file_path

def read_file():
    file_counter = 0
    global file_count
    for each_hash in filename_hash_list:
        file_counter+=1
        print "Processing "+str(file_counter)+" : "+str(file_count)
        file_path = filename_hash_list[each_hash]
        file_content = open(file_path, mode='r')
        soup = BeautifulSoup(file_content, 'html.parser')#feed to Beautifulsoup
        text_content_from_file = soup.get_text()
        split_text =  text_content_from_file.split()
        for each_word in split_text:
            each_word_freq = split_text.count(each_word)
#            print str(each_word_freq)+":"+each_word

            if each_word in word_hash:
                counter_hash = word_hash[each_word]
                if not each_hash in counter_hash:
                    counter_hash[each_hash] = each_word_freq
            else:
                word_hash[each_word] = {}
                counter_hash = word_hash[each_word]
                counter_hash[each_hash] = each_word_freq

#hash_link()
#read_file()
def main(search_query):
    hash_link()
    read_file()
    return_result_list = []
    for each_word in word_hash:
        print "Checking : "+each_word
        if search_query in each_word:
            result_list = word_hash[each_word]
            for each_result in result_list:
                return_result_list.append(filename_hash_list[each_result])
    return return_result_list

