import sys

filename = str(sys.argv[1])

wordCount = 0

toCheck = ["\\chapter", "\\begin", "\\end", "\\section", "\\cite"]

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
        
        
