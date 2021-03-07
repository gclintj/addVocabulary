import csv
import unicodedata

#use a file
path = '/home/lintj/file.csv'
with open(path, mode='w+', newline = '') as oldcsv:
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

#save file
with open(path, 'w', newline = '') as newcsv:
    write = csv.writer(newcsv)
    write.writerow(new_list)

#to be tested: Chinese comma
