import csv

#use a file
with open('file.csv', newline = '') as oldcsv:
    oldlist = list(csv.reader(oldcsv))

#get new words
#TODO
Enter word(s) to be added, seperated by comma:

#split
add_list = [w.strip() for w in word_string.split(',') if w.strip()]

#combine and remove duplicate

list = set(old + list)

#sort

#save file
