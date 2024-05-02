import requests
import os
import sys

# URL of the stream list file (.m3u8 or .m3u)
stream_list_url = sys.argv[1]
site = sys.argv[2]

params = stream_list_url.split("/")
# Read the stream list file
response = requests.get(stream_list_url)
stream_list_content = response.text

# Find the URLs of the .ts segments
ts_urls = [line.strip() for line in stream_list_content.splitlines() if line.endswith(".ts")]
print(ts_urls[-1])

# Create a directory to save the .ts files
output_dir = "ts_files"
os.makedirs(output_dir, exist_ok=True)

# Download each .ts segment
for i, ts_url in enumerate(ts_urls):
    ts_filename = f"{output_dir}/segment_{i}.ts"
    if site == "": downurl = ts_url
    if site == "thempho":
      downurl = "https://static.thempho.com/video/stream/" + params[5] + "/" + params[6] + "/" + params[7] + "/" + ts_url
    response = requests.get(downurl)
    with open(ts_filename, "wb") as f:
        f.write(response.content)
    print(f"Downloaded {ts_filename}")

print("All .ts segments downloaded successfully.")