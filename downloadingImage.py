import requests, shutil

url = input("Please enter an image url (string):")

file_name = input("save image as a (string)")

res = requests.get(url, stream=True)

if res.status_code == 200:
    with open(file_name, 'wb') as f:
        shutil.copyfileobj(res.raw, f)
    print("Image successfully Downloaded: ", file_name)
else:
    print("Image couldn't be downloaded ")