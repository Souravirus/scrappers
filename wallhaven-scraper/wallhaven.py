import urllib.request
import os
from bs4 import BeautifulSoup

#ask user how many wallpapers to download
limit = int(input('Number of wallpapers to download: '))



#allowed aspect ratios: 4x3, 5x4, 16x9, 16x10, 21x9, 32x9, 48x9, 9x16, 10x16
ratios = ["16x9", "16x10"]

count = 1
if not os.path.exists("wallpapers"):
    os.makedirs("wallpapers")

#ask user to include general/anime/people categories, 0 = disabled, 1 = enabled
general = 1 if input('Include "General" category (y/n): ') == 'y' else 0
anime = 1 if input('Include "Anime" category (y/n): ') == 'y' else 0
people = 1 if input('Include "People" category (y/n): ') == 'y' else 0

#ask for purity of wallpapers
purity = 100 if input('Include NSFW filtering (y/n): ') == 'y' else 110

while count <= limit:
    
    url = "https://alpha.wallhaven.cc/search?categories={}{}{}&purity={}&ratios={}&sorting=random&order=desc".format(general, anime, people, purity, "%2C".join(ratios))

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