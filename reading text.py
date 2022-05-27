# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open (filename, 'r') as c: #with open is means the opened file will be closed automatically
        text= c.read()
        return text

import re # had to import regex to use later below

output= read_file_content('story.txt')
print(output)


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
counts=dict()
# textwopunctuation= re.sub(r'[^\w\s]','',output) used this as first solution
text = re.sub(r'[^\w\s]','',output).split()  # this was used as second solution after further research

print(text)

for word in text:
    if word in counts.keys():
        counts[word] +=1
    else:
            counts[word] =1
print(counts)

