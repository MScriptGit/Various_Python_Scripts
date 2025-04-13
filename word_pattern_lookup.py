#imports list of Dutch words and search for patterns in words of specific length

#import regex
import re

#import nl woorden
f = open("nlTaalPack/OpenTaal-210G-basis-gekeurd.txt", "r")

#convert data to a string
toStr = f.read()

#set length var
length = int(0)

#user input
pattern = input("Geef zoekpatroon in. Gebruik . voor onbekende letters: ")

#get length of user input
length = len(pattern)

#get words of desired length
lenFiltered = [word for word in toStr.split() if len(word) == length]

#add filtered words to a list
filteredStr = " , ".join(str(element) for element in lenFiltered)

#remove commas
enhancedStr = filteredStr.replace(" , ", "\n")

#regex pattern search in filtered word list
x = re.findall(pattern, enhancedStr)

#remove double list items (which seem to show up for some reason)
noDoubles = list(set(x))

#sort alphabetically
noDoubles.sort()

#print result
print(noDoubles)