from email import message_from_bytes
from email.encoders import encode_base64
from email.policy import default
from os import walk, makedirs
from os.path import join
from sys import path
def list_files_recursively(directory):
    file_list = []
    for root, dirs, files in walk(directory):
        for file in files:
            file_list.append([join(root, file),file])
    return file_list

file_list = list_files_recursively(join(path[0], 'input'))
print(file_list)

for file in file_list:
    print("----------------------------------------")
    print(file[0])    
    dir = join(path[0], 'output')
    print(dir)
    makedirs(dir, exist_ok=True)
    file_out = join(dir,file[1])
    print(file_out)
    # Read the MHTML file
    with open(file[0], 'rb') as file:
        mhtml_content = file.read()

    # Parse the MHTML content
    msg = message_from_bytes(mhtml_content)

    # Convert encoding to base64
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part['Content-Transfer-Encoding'] == 'binary':
            part.set_payload(part.get_payload(decode=True))
            encode_base64(part)
            part.replace_header('Content-Transfer-Encoding', 'base64')
    
    # Save the converted MHTML file
    with open(file_out, 'wb') as file:
        file.write(msg.as_bytes(policy=default))

