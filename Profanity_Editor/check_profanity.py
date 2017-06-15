import urllib.request

def read_text():
    quotes = open("/Users/PriteshJ/Documents/Udacity/ProgrammingFoundationsWithPython/Profanity_Editor/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    # need to filter out bad whitespace or it returns "HTTP Error 400: Bad Request"
    contents_of_file = ''.join(contents_of_file.split())
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    # Using b"boolean_value" since in Python 3, file is read in bytes by default
    if b"true" in output:
        print("Profanity Alert!!")
    elif b"false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")
    
read_text()
