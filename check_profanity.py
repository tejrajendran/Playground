import urllib

def read_text(file_path):
    quotes = open(file_path)
    contents_of_file = quotes.read()
    quotes.close()
    return contents_of_file

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()

    if "true" in output:
        print "PROFANITY ALERT!!"
    else :
        print "no curse words found"

    connection.close()

text = read_text("/Users/212571508/Documents/workspace/full_stack_web_developer/Playground/movie_quotes.txt")
check_profanity(text)