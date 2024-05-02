import sys

url = sys.argv[1]
save_dir = sys.argv[2]
custom_name = sys.argv[3]
name = sys.argv[4]

if save_dir == "Google Drive":
    sdir = f"/content/drive/MyDrive/{name}"

#normal download
if custom_name == False:
    !youtube-dl "$url"
    if save_dir == "Google Drive":
        !youtube-dl "$sdir" "$url"
else:
    