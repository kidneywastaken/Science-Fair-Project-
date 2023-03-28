import time, hashlib

def MD5me(s):
    result = s.encode("utf-8")
    result = hashlib.md5(result).hexdigest()
    return result

def leading_zeroes(n, zeroes):
    t=("0"*zeroes)+str(n)
    t=t[-zeroes:]
    return t

def report_search_time(tests, seconds):
    if (seconds > 0.000001):
        print ("The search took "+make_human_readable(seconds)+" seconds for "+make_human_readable(tests)+" tests or "+make_human_readable(tests/seconds)+" tests per second.")
    else:
        print ("The search took "+make_human_readable(seconds)+" seconds for "+make_human_readable(tests)+" tests.")
    return

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

print("In method #1 the password will only consist of numbers.")
input("Enter to continue")
Input_Password = input("Type a 'password' consisting of only numbers: ")
no_space_password = Input_Password.replace(" ", '')
num_digits = len(no_space_password)
stored_password = MD5me(no_space_password)

#------Method One------#
def search_method_1(num_digits):
    result = False
    a=0
    starttime = time.time()
    tests = 0
    still_searching = True

    while still_searching and a<(10**num_digits):
        ourguess = leading_zeroes(a,num_digits)
        
        tests = tests + 1
        if stored_password == MD5me(ourguess):
            print ("Success! The password is " + ourguess)
            still_searching = False  
            result = True
   
        a=a+1

    seconds = time.time()-starttime
    report_search_time(tests, seconds)
    return result

search_method_1(num_digits)
