import shutil
import requests

url = input("Please enter an image URL (String): ")

file_name = input("Save image as (String): ")

res = requests.get(url, stream= True)

if res.status_code == 200:
    with open(file_name, "wb") as f:
        shutil.copyfileobj(res.raw, f)
    print("Image successfully Downloaded: ", file_name)
else:
    print("Image Couldn't be downloaded")