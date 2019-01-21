import requests
import shutil

url = "insert url here"

local_filename = url.split('/')[-1]
r = requests.get(url, stream=True)
with open(local_filename, 'wb') as f:
    shutil.copyfileobj(r.raw, f)