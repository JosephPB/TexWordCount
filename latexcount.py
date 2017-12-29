"""
Programme takes .tex file name command line input and produces a wordcount.txt file
containing the word count of file ignoring certain words specified in programme
"""

import sys

filename = str(sys.argv[1])

wordCount = 0

#list of beginnings to ignore in a word count
toCheck = ["\\begin", "\\end", "\\documentclass", "\\usepackage", "\\title", "\\date", "\\chapter", "\\section", "\\subsection", "\\cite"]

#read .tex file and update wordCount
with open(filename, "r") as texFile:
    for line in texFile:
        words = []
        words.append(line.split())
        print words
        for word in words[0]:
            is_in = False
            counter = 0
            while is_in == False and counter < len(toCheck):
                if word[0:len(toCheck[counter])] == toCheck[counter]:
                    is_in = True
                counter += 1
            if is_in == False:
                wordCount += 1

print wordCount
                
#output wordcount.txt file
with open("wordcount.txt", "w") as outputFile:
    outputFile.write("wordcount: {}".format(wordCount))
        
        
