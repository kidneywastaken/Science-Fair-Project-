import sys, time, hashlib
from array import *

# # total number of guesses we had to make to find it
totalguesses = 0

# ## Convert a string into MD5 hash
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

Input_Password = input("type any passsword your heart desires(8 max charaters): ")
Input_Password = MD5me(Input_Password)


#------Method One------#
def search_method_1(num_digits, Input_Password):
    global totalguesses
    result = False
    a=0
    starttime = time.time()
    tests = 0
    still_searching = True

    while still_searching and a<(10**num_digits):
        ourguess = leading_zeroes(a,num_digits)
    
        tests = tests + 1
        totalguesses = totalguesses + 1
        if Input_Password == MD5me(ourguess):
            print ("Success! The password is " + ourguess)
            still_searching = False  
            result = True
   
        a=a+1

    seconds = time.time()-starttime
    report_search_time(tests, seconds)
    return result


#------Method Two------#
def search_method_2(num_pass_wheels, Input_Password):
    global totalguesses
    result = False
    starttime = time.time()
    tests = 0
    still_searching = True
    
    wheel = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    # Only allow up to 8 characters 
    if (num_pass_wheels > 8):
        print("Unable to handle the request. No more than 8 characters for a password")
        still_searching = False
    
    # Set all of the wheels to the first position
    pass_wheel_array=array('i',[1,0,0,0,0,0,0,0,0])
        
    while still_searching:
        ourguess_pass = ""
        for i in range(0,num_pass_wheels):  # once for each wheel
            if pass_wheel_array[i] > 0:
                ourguess_pass = wheel[pass_wheel_array[i]] + ourguess_pass
        if Input_Password == MD5me(ourguess_pass):
            print ("Success! Password is " + ourguess_pass)
            still_searching = False   # we can stop now - we found it!
            result = True
      
        tests += 1
        totalguesses = totalguesses + 1
        # Spin the rightmost wheel and if it changes, spin the next one over and so on
        carry = 1
        for i in range(0,num_pass_wheels): # Once for each wheel
            pass_wheel_array[i] = pass_wheel_array[i] + carry
            carry = 0
            if pass_wheel_array[i] > 62:
                pass_wheel_array[i] = 1
                carry = 1
                if i == (num_pass_wheels-1):
                    still_searching = False

    seconds = time.time()-starttime
    report_search_time(tests, seconds)
    return result


#------Method Three------#
def search_method_3(file_name):
    result = False
    global totalguesses

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
        
        if Input_Password == MD5me(ourguess_pass):
            print ("Success! The password is " + ourguess_pass)
            still_searching = False   # We can stop now - we found it!
            result = True
        
        tests = tests + 1
        totalguesses = totalguesses + 1
        # First letter capitalized
        if still_searching:
            ourguess_pass = Cap(ourguess_pass)
           
            if Input_Password == MD5me(ourguess_pass):
                print ("Success! The password is " + ourguess_pass)
                still_searching = False   # We can stop now - we found it!
                result = True
    
            tests = tests + 1

        word1count = word1count + 1
        if (word1count >=  number_of_words):
            still_searching = False

    seconds = time.time()-starttime
    report_search_time(tests, seconds)
    return result


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
       
        if Input_Password == MD5me(ourguess_pass):
            print ("Success! The password is " + ourguess_pass)
            still_searching = False   # We can stop now - we found it!
            result = True
       
        tests = tests + 1
        totalguesses = totalguesses + 1
        # First letter capitalized
        if still_searching:
            ourguess_pass = Cap(words[word1count]) + punctuation[punc_count] + words[word2count]
          
            if Input_Password == MD5me(ourguess_pass):
                print ("Success! The password is " + ourguess_pass)
                still_searching = False   # We can stop now - we found it!
                result = True
     
            tests = tests + 1
            totalguesses = totalguesses + 1
        # First letter of the second word capitalized
        if still_searching:
            ourguess_pass = words[word1count] + punctuation[punc_count] + Cap(words[word2count])
            
            if Input_Password == MD5me(ourguess_pass):
                print ("Success! The password is " + ourguess_pass)
                still_searching = False   # We can stop now - we found it!
                result = True
           
            tests = tests + 1
            totalguesses = totalguesses + 1
        # Both words capitalized
        if still_searching:
            ourguess_pass = Cap(words[word1count]) + punctuation[punc_count] + Cap(words[word2count])
     
            if Input_Password == MD5me(ourguess_pass):
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


def main(Input_Password):
    Totalstarttime = time.time()
    tests = 0 
    found_password = False
    if not found_password: 
        found_password = search_method_3("passwords.txt")

    if not found_password:
        print("Method 3 did not work!")
        found_password = search_method_4("passwords.txt")

    if not found_password:
        print("Method 4 did not work!")
        found_password = search_method_1(1, Input_Password)
    
    if not found_password:
        found_password = search_method_1(2, Input_Password)

    if not found_password:
        found_password = search_method_1(3, Input_Password)

    if not found_password:
        found_password = search_method_1(4, Input_Password)

    if not found_password:
        found_password = search_method_1(5, Input_Password)

    if not found_password:
        found_password = search_method_1(6, Input_Password)

    if not found_password:
        found_password = search_method_1(7, Input_Password)

    if not found_password:
        found_password = search_method_1(8, Input_Password)

    if not found_password:
        print("Method 1 did not work!")
        found_password = search_method_2(4, Input_Password)

    if not found_password:
        found_password = search_method_2(5, Input_Password)

    if not found_password:
        found_password = search_method_2(6, Input_Password)

    if not found_password:
        found_password = search_method_2(7, Input_Password)

    if not found_password:
        found_password = search_method_2(8, Input_Password)

    seconds = time.time() - Totalstarttime

    if (seconds < 0.00001):
        print ("The total search for all methods took "+make_human_readable(seconds)+" seconds and "+make_human_readable(totalguesses)+" guesses.")
        print ("(on some machines, Python doesn't know how long things actually took)")
    else:
        print ("The total search for all methods took "+make_human_readable(seconds)+" seconds and "+make_human_readable(totalguesses)+" guesses.("+make_human_readable(totalguesses/seconds)+" guesses per second)")

main(Input_Password)