import re
import sys

def clean_text(text):
    #"remove punctuation form a text"
    #"'Error in quotation marks: the same quotation mark used to open must also be used to close. 

    punct = "+.*/?,;'\#"
    #When an error occurs in usage ', we must employ a different set of quotation marks "".
    for p in punct:
        #(:) must be placed at for 
        text = text.replace(p,"")
        # here forget to close " for space 
    return text 

def tokenize(text):
    """Convert text into tokens"""
    #" ''Error in quotation marks we can use """ its more pratical when we leave a line 
    return text.split( )

def tokenize2(text):
    """Convert text into tokens,return a list of tokens(words)"""
    #Error in quotation marks:must use the same for open and close
    spaces = r"\s+"
    #Forgetting quotation marks around the regular expression 
    words = re.split(spaces,text)# forget to import re 
    return words
    # declaration words not word and return must be upon def 

def word_freq(words):
    """Counts
    words and return a
    dictionary of words
    with
    their occurrence"""
    #The text is written normally, without quotation marks.
    index={}
    for w in words:
        if w in index:
            #Forgetting to plac: at the end of the condition
            index[w] += 1
        else:
            #Forgetting to plac: at the end of the condition else 
            index[w] = 1
    return index #انشاء قاموس فارغ 

def most_common_word(words_freq_table):
    #Missing  (:) at the end of the line
    """Counts words and return a dictionary of words with their"""
    #Error in quotation marks:must use the same for open and close 

    frequent =""
    #'frequent' has no assigned value
    frequency = 0
    for word in words_freq_table:
        #Missing : at the end of for 
        if words_freq_table[word] > frequency:
            frequent = word
            frequency = words_freq_table[word]
    return frequent

def read_file(filename):
    #Missing : at the end of function 
    'Read a text from file'
    #error quotation mark without closing 

    text = ""
    #the quotation use to open must use for close 
    try:# missing : at the end 
        fl = open(filename)
        text = fl.read()
        fl.close()  # When open a file using open(), you close it after finished by fl.close() 
        #to avoid consuming system resources and memory
    except:
        print("Can't open file", filename)
        #Error in quotation marks and 
        sys.exit()# forget to import sys 
    return text
