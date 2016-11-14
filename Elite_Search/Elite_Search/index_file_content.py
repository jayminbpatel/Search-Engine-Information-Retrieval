from bs4 import BeautifulSoup
from global_variables import *
from counter import *
def index_file_content(filename):
    file_content = open(filename, mode='r')#parse file
    soup = BeautifulSoup(file_content, 'html.parser')#feed to Beautifulsoup
    all_text = soup.get_text()#get all text content
    text_array = soup.get_text().split()#slit using spaces and store it in a variable
#    for each_word in text_array:
#        each_word_freq = counter(each_word, text_array)
#        if each_word in word_hash_map:
#            list = word_hash_map[each_word]
#            if not filename in list:
#                list.append(each_word_freq+":"+filename)
#        else:
#            word_hash_map[each_word] = []
#            list = word_hash_map[each_word]
#            list.append(each_word_freq+":"+filename)
#    for each_word in wordHashMap:
#        print str(wordHashMap[each_word])+":"+each_word
    for each_word in text_array:
        each_word_freq = counter(each_word, text_array)
        if each_word in word_hash_map:
            list = word_hash_map[each_word]
            if not filename in list:
                list.append(each_word_freq+":"+filename)
        else:
            word_hash_map[each_word] = []
            list = word_hash_map[each_word]
            list.append(each_word_freq+":"+filename)
#    for each_word in wordHashMap:
#        print str(wordHashMap[each_word])+":"+each_word