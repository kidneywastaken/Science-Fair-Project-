import sys, time, hashlib
from array import *

# total number of guesses we had to make to find it
totalguesses = 0

def leading_zeroes(n, zeroes):
    t=("0"*zeroes)+str(n)
    t=t[-zeroes:]
    return t

# This displays the results of a search including tests per second when possible
def report_search_time(tests, seconds):
    if (seconds > 0.000001):
        print ("The search took "+make_human_readable(seconds)+" seconds for "+make_human_readable(tests)+" tests or "+make_human_readable(tests/seconds)+" tests per second.")
    else:
        print ("The search took "+make_human_readable(seconds)+" seconds for "+make_human_readable(tests)+" tests.")
    return

# This function takes in numbers, rounds them to the nearest integer and puts
# commas in to make it more easily read by humans
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
        
## A little helper program to remove any weird formatting in the file
def cleanup (s):
    s = s.strip()
    return s

## A little helper program that capitalizes the first letter of a word
def Cap (s):
    s = s.upper()[0]+s[1:]
    return s


print("In method #4 we will guess from a list of common passwords but will guess two words in the same password with a symbol between them.")
input("enter to continue")
Input_Password = input("type a two word 'password'with a symbol between them") # **get rid of spaces or letters**

# *** METHOD 4 ***     
def search_method_4(file_name):
    global totalguesses
    result = False
    
    # Start by reading the list of words into a Python list
    f = open(file_name)
    words = f.readlines()
    f.close
    # We need to know how many there are
    number_of_words = len(words)
    
    ## Depending on the file system, there may be extra characters before
    ## or after the words. 
    for i in range(0, number_of_words):
        words[i] = cleanup(words[i])

    # Let's try each one as the password and see what happens
    starttime = time.time()
    tests = 0
    still_searching = True
    word1count = 0           # Which word we'll try next
    punc_count = 0
    word2count = 0

    punctuation="~!@#$%^&*()_-+={}[]:<>,./X"  # X is a special case where we omit
                                              # the punctuation to run the words together

    number_of_puncs = len(punctuation)
    print()
    print("Using method 4 with "+str(number_of_puncs)+" punctuation characters and "+str(number_of_words)+" words...")

    while still_searching:
        if ("X" == punctuation[punc_count]):
            # If we're at the end of the string and found the 'X', leave it out
            ourguess_pass = words[word1count] + words[word2count]
        else:
            ourguess_pass = words[word1count] + punctuation[punc_count] + words[word2count]
        # uncomment the next line to print the current guess
        print("Guessing: "+ourguess_pass)
        # Try it the way they are in the word list
        if Input_Password == ourguess_pass:
            print ("Success! The password is " + ourguess_pass)
            still_searching = False   # we can stop now - we found it!
            result = True
        #else:
            #print ("Darn. " + ourguess_pass + " is NOT the password.")
        tests = tests + 1
        totalguesses = totalguesses + 1
        # Now let's try it with the first letter of the first word capitalized
        if still_searching:
            ourguess_pass = Cap(words[word1count]) + punctuation[punc_count] + words[word2count]
            # uncomment the next line to print the current guess
            # print("Guessing: "+ourguess_pass)
            if Input_Password == ourguess_pass:
                print ("Success! The password is " + ourguess_pass)
                still_searching = False   # we can stop now - we found it!
                result = True
            #else:
                #print ("Darn. " + ourguess_pass + " is NOT the password.")
            tests = tests + 1
            totalguesses = totalguesses + 1
        # Now let's try it with the first letter of the second word capitalized
        if still_searching:
            ourguess_pass = words[word1count] + punctuation[punc_count] + Cap(words[word2count])
            # uncomment the next line to print the current guess
            # print("Guessing: "+ourguess_pass)
            if Input_Password == ourguess_pass:
                print ("Success! The password is " + ourguess_pass)
                still_searching = False   # we can stop now - we found it!
                result = True
            #else:
                #print ("Darn. " + ourguess_pass + " is NOT the password.")
            tests = tests + 1
            totalguesses = totalguesses + 1
        # Now let's try it with the both words capitalized
        if still_searching:
            ourguess_pass = Cap(words[word1count]) + punctuation[punc_count] + Cap(words[word2count])
            # uncomment the next line to print the current guess
            # print("Guessing: "+ourguess_pass)
            if Input_Password == ourguess_pass:
                print ("Success! The password is " + ourguess_pass)
                still_searching = False   # we can stop now - we found it!
                result = True
            #else:
                #print ("Darn. " + ourguess_pass + " is NOT the password.")
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