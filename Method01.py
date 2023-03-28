import time 

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
input("enter to continue")
Input_Password = input("type a 'password' consisting of only numbers: ") # **get rid of spaces or letters**
num_digits = len(Input_Password)

#------Method One------#
def search_method_1(num_digits):
    global totalguesses
    result = False
    a=0
    starttime = time.time()
    tests = 0
    still_searching = True

    while still_searching and a<(10**num_digits):
        ourguess = leading_zeroes(a,num_digits)
        
        tests = tests + 1
        if Input_Password == ourguess:
            print ("Success! The password is " + ourguess)
            still_searching = False  
            result = True
   
        a=a+1

    seconds = time.time()-starttime
    report_search_time(tests, seconds)
    return result

search_method_1(num_digits)
