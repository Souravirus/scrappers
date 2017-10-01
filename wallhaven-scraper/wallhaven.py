import urllib.request
import os
from bs4 import BeautifulSoup

#how many wallpapers to download
limit = 15

#include general/anime/people categories, 0 = disabled, 1 = enabled
general = 1
anime = 1
people = 0

#allowed aspect ratios: 4x3, 5x4, 16x9, 16x10, 21x9, 32x9, 48x9, 9x16, 10x16
ratios = ["16x9", "16x10"]

count = 1
if not os.path.exists("wallpapers"):
    os.makedirs("wallpapers")

while count < limit:
    
    url = "https://alpha.wallhaven.cc/search?categories={}{}{}&purity=100&ratios={}&sorting=random&order=desc".format(general, anime, people, "%2C".join(ratios))

    req = urllib.request.Request(url)
    req.add_header('User-agent', 'Mozilla/')

    soup = BeautifulSoup(urllib.request.urlopen(req).read(), 'html.parser')
    walls = []
    for previewlink in soup.find_all('a', class_="preview"):
        walls.append(previewlink['href'])

    for wall in walls:
        req = urllib.request.Request(wall)
        req.add_header('User-agent', 'Mozilla/')
        soup = BeautifulSoup(urllib.request.urlopen(req).read(), 'html.parser')
        paper = soup.find(id="wallpaper")['src']
        print("Downloaded {}/{}".format(count,limit))
        
        f = open('wallpapers/'+paper.replace('//wallpapers.wallhaven.cc/wallpapers/full/', ''), 'wb')
        req = urllib.request.Request('https:'+paper)
        req.add_header('User-agent', 'Mozilla/')
        f.write(urllib.request.urlopen(req).read())
        f.close()
        count += 1
        if count > limit:
            break
print("done")