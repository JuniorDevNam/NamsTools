from os import system
file = input("Enter MHTML File: ")
out_dir = file[:]
if ".mhtml" in file:
    out_dir.replace(".mhtml","")
out_dir.replace(" ","_")
print(file)
print(out_dir)
system
