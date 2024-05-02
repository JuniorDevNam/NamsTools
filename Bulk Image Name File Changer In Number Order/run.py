import os
import sys

input_file = os.path.join(sys.path[0],"input_file_names.txt")
imagespath = os.path.join(sys.path[0],"Images")

print('''The Android File Manager ordered the number file name as strings, \n
so if you rename the file in normal order like this: \n
"0.jpg, 1.jpg, 2.jpg,...,99.jpg",\n
it will order the files in the File Explorer like this: \n
"0.jpg, 1.jpg, 10.jpg, 11.jpg,...,2.jpg , 20.jpg, 21.jpg,..." \n
To fix that stupid sorting, we have to add zeros (0) \n
in front of the numbers 1 to 9\n
''')

fukingdumbandroidreadnumberfilenameodering = str(input('''Support Android Ordering List Images? \n
Yes / No: '''))

with open(input_file, 'r', encoding="utf-8") as i:
    names = i.readlines()

def main(imagespath, names):
    for count, name in enumerate(names):
        oldName = os.path.join(imagespath, name.strip())
        if os.path.exists(oldName):
            new = str(count)
            if fukingdumbandroidreadnumberfilenameodering == 'Yes':
                if 1 <= len(names) <= 999:
                    new_filename = new.zfill(3)
                elif 1000 <= len(names) <= 9999:
                    new_filename = new.zfill(4)
            else:
                new_filename = new
            newName = os.path.join(imagespath, new_filename)
            os.rename(oldName, newName)

main(imagespath, names)
