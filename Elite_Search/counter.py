<<<<<<< HEAD
from global_variables import *
freq_hash={}
def counter(word_array):
    for each_word in word_array:
        freq_hash[each_word] = ""
    for each_word in freq_hash:
        freq_hash[each_word] = word_array.count(each_word)
=======
from global_variables import *
freq_hash={}
def counter(word_array):
    for each_word in word_array:
        freq_hash[each_word] = ""
    for each_word in freq_hash:
        freq_hash[each_word] = word_array.count(each_word)
>>>>>>> be72d95c64dfbe6173a00e5666955c37e30b2028
        print each_word+":"+str(freq_hash[each_word])