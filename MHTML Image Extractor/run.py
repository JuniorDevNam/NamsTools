from os.path import join
from os import makedirs
from sys import path
from MHTMLExtractor import MHTMLExtractor

file = input("Enter MHTML File (File Must Be The Same Directory; Enter Name File With .mhtml Extension File Only): ")
file_path = join(path[0], file)
out_dir = file[:]
if ".mhtml" in file:
    out_dir = out_dir.replace(".mhtml", "")
out_dir = out_dir.replace(" ", "_")
print(file)
dir = join(path[0], out_dir)
makedirs(dir, exist_ok=True)
print(out_dir)

MHTMLExtractor(mhtml_path=file_path, output_dir=dir).extract()