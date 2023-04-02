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

print("In method #3 we will guess from a list of common passwords.")
input("enter to continue")
Input_Password = input("type a one word 'password': ") 
stored_password = MD5me(Input_Password)

#------Method Three------#
def search_method_3(file_name):
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

    while still_searching:
        ourguess_pass = words[word1count]
        
        if stored_password == MD5me(ourguess_pass):
            print ("Success! The password is " + ourguess_pass)
            still_searching = False   # We can stop now - we found it!
            result = True
        
        tests = tests + 1
        # First letter capitalized
        if still_searching:
            ourguess_pass = Cap(ourguess_pass)
           
            if stored_password == MD5me(ourguess_pass):
                print ("Success! The password is " + ourguess_pass)
                still_searching = False   # We can stop now - we found it!
                result = True
    
            tests = tests + 1

        word1count = word1count + 1
        if (word1count >=  number_of_words):
            still_searching = False

    if still_searching == False and totalguesses == 870:
        print("Darn the passwaord isn't in our list of words.")

    seconds = time.time()-starttime
    report_search_time(tests, seconds)
    return result

search_method_3("passwords.txt")