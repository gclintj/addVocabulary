import csv
import unicodedata

#use a file
filepath = '/home/lintj/file.csv'

open(filepath, mode='a', newline = '') 
with open(filepath, newline = '') as oldcsv:
    oldlist = list(csv.reader(oldcsv))
    if oldlist:
        oldlist = oldlist[0]

#get new words
words = input("Enter word(s) to be added, seperated by comma:\n")
words = unicodedata.normalize('NFKC',words)

#split
add_list = [w.strip() for w in words.split(',') if w.strip()]

print(oldlist)
print(add_list)

#combine and remove duplicate
new_list = list(set(oldlist + add_list))

#sort
new_list.sort()

print(new_list)
print(len(new_list),"words in total.")

#save file
with open(filepath, 'w', newline = '') as newcsv:
    write = csv.writer(newcsv)
    write.writerow(new_list)

#to be tested: Chinese comma
