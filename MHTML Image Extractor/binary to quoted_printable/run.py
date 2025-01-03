from email import message_from_bytes
import quopri
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

    # Convert encoding to quoted-printable
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part['Content-Transfer-Encoding'] == 'binary':
            binary_data = part.get_payload(decode=True)
            quoted_printable_data = quopri.encodestring(binary_data)
            part.set_payload(quoted_printable_data.decode('ascii'))
            part.replace_header('Content-Transfer-Encoding', 'quoted-printable')

    # Save the converted MHTML file
    with open(file_out, 'wb') as file:
        file.write(msg.as_bytes(policy=default))