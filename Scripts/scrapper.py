import requests
import shutil

url = "https://storage.googleapis.com/openimages/2018_04/test/test-images-with-rotation.csv"

local_filename = url.split('/')[-1]
r = requests.get(url, stream=True)
with open(local_filename, 'wb') as f:
    shutil.copyfileobj(r.raw, f)