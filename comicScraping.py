import bs4, requests, os

url = 'https://xkcd.com'               # starting url
os.makedirs('xkcd', exist_ok=True)    # store comics in ./xkcd
while not url.endswith('#'):
    print("Downloading page %s..." % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    comicElem = soup.select('#comic img')

    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        print('Downloading image %s...' % (comicUrl))
        res.raise_for_status()

        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    prevLink = soup.select('a[rel = "prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')
print('Done')