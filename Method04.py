# Code has been modified and adapted from Science Buddies; https://www.sciencebuddies.org/science-fair-projects/project-ideas/CompSci_p046/computer-science/password-security-how-easily-can-your-password-be-hacked#procedure

import time, hashlib
from array import *

totalguesses = 0

## Convert a string into MD5 hash
def MD5me(s):
    result = s.encode("utf-8")
    result = hashlib.md5(result).hexdigest()
    return result

## Adds zeros to all the guesses so that we get all possible combinations 
def leading_zeroes(n, zeroes):
    t=("0"*zeroes)+str(n)
    t=t[-zeroes:]
    return t

## Displays the results of a search 
def report_search_time(tests, seconds):
    if (seconds > 0.000001):
        print ("The search took "+make_human_readable(seconds)+" seconds for "+make_human_readable(tests)+" tests or "+make_human_readable(tests/seconds)+" tests per second.")
    else:
        print ("The search took "+make_human_readable(seconds)+" seconds for "+make_human_readable(tests)+" tests.")
    return

## Rounds numbers to the nearest integer and puts Adds commas to make it easier read
def make_human_readable(n):
    if n>=1:
        result = ""
        temp=str(int(n+0.5))
        while temp != "":
            result = temp[-3:] + result
            temp = temp[:-3]
            if temp != "":
                result = "," + result
    else:
        temp = int(n*100)
        temp = temp /100
        result = str(temp)
    return result
        
## Remove any weird formatting in the file
def cleanup (s):
    s = s.strip()
    return s

## Capitalizes the first letter of a word
def Cap (s):
    s = s.upper()[0]+s[1:]
    return s

print("In method #4 we will guess from a list of common passwords but will guess two words in the same password with a symbol between them.")
input("enter to continue")
Input_Password = input("type a two word 'password'with a symbol between them: ")
no_space_password = Input_Password.replace(" ", '')
stored_password = MD5me(no_space_password)

#------Method Four------#     
def search_method_4(file_name):
    global totalguesses
    result = False
    
    # Start by reading the list of words into a Python list
    f = open(file_name)
    words = f.readlines()
    f.close
    # How many words are there
    number_of_words = len(words)
    
    ## Cleans up the formatting so that it only looks at the words
    for i in range(0, number_of_words):
        words[i] = cleanup(words[i])

    starttime = time.time()
    tests = 0
    still_searching = True
    word1count = 0         
    punc_count = 0
    word2count = 0

    punctuation="~!@#$%^&*()_-+={}[]:<>,./X"  # X is a special case where we omit
                                              # the punctuation to run the words together

    number_of_puncs = len(punctuation)

    while still_searching:
        if ("X" == punctuation[punc_count]):
            # If we're at the end of the string and found the 'X', leave it out
            ourguess_pass = words[word1count] + words[word2count]
        else:
            ourguess_pass = words[word1count] + punctuation[punc_count] + words[word2count]
       
        if stored_password == MD5me(ourguess_pass):
            print ("Success! The password is " + ourguess_pass)
            still_searching = False   # We can stop now - we found it!
            result = True
       
        tests = tests + 1
        totalguesses = totalguesses + 1
        # First letter capitalized
        if still_searching:
            ourguess_pass = Cap(words[word1count]) + punctuation[punc_count] + words[word2count]
          
            if stored_password == MD5me(ourguess_pass):
                print ("Success! The password is " + ourguess_pass)
                still_searching = False   # We can stop now - we found it!
                result = True
     
            tests = tests + 1
            totalguesses = totalguesses + 1
        # First letter of the second word capitalized
        if still_searching:
            ourguess_pass = words[word1count] + punctuation[punc_count] + Cap(words[word2count])
            
            if stored_password == MD5me(ourguess_pass):
                print ("Success! The password is " + ourguess_pass)
                still_searching = False   # We can stop now - we found it!
                result = True
           
            tests = tests + 1
            totalguesses = totalguesses + 1
        # Both words capitalized
        if still_searching:
            ourguess_pass = Cap(words[word1count]) + punctuation[punc_count] + Cap(words[word2count])
     
            if stored_password == MD5me(ourguess_pass):
                print ("Success! The password is " + ourguess_pass)
                still_searching = False   # We can stop now - we found it!
                result = True
    
            tests = tests + 1
            totalguesses = totalguesses + 1

        word1count = word1count + 1
        if (word1count >=  number_of_words):
            word1count = 0
            punc_count = punc_count + 1
            if (punc_count >= number_of_puncs):
                punc_count = 0
                word2count = word2count + 1
                if (word2count >= number_of_words):
                    still_searching = False

    seconds = time.time()-starttime
    report_search_time(tests, seconds)
    return result

search_method_4("passwords.txt")