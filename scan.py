import sys
import urllib.parse
import urllib.request
from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen

domain = sys.argv[1]

if domain[0:7] != "http://" and domain[0:8] != "https://":
    domain = "http://" + domain
    if domain[len(domain) - 1] == '/':
        domain = domain[0:len(domain) - 1]

def check(address):
    '''
    Return Code List
    0 Success
    -1 HTTPError
    -2 URLError
    '''

    req = urllib.request.Request(address)

    try:
        response = urlopen(req)
    except HTTPError as e:  #The Server Can't Answer This Request.
        return -1 
    except URLError as e:   #Can't Reach To The Server
        return -2    
    else:
        return 0    #Successfully Access

def main():
    print('Start scanning ' + domain + '...')
    print("")

    fo = open("dict.txt", 'r')
    words = fo.readlines()
    
    total = 0

    for line in words:
        line = line[0:len(line) - 1]
        result = check(domain + line)
        if result == 0:
            print(domain + line)
            total = total + 1
        elif result == -2:
            print("Fatal Error : Can't Reach to the Server.")
            return
    
    print("")
    print("Scan ended. " + str(total) + " directories found in total.")


main()
