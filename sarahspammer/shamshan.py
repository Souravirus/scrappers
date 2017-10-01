import requests
import bs4
import os

url = str(input('Enter the url: '))

s = requests.Session()
resp = s.get(url)
outTxt = str(resp.text)
soup = bs4.BeautifulSoup(outTxt, 'lxml')

userId = soup.find('input')['value']
requestToken = None
# print(userId)

for kapa in range(100):
    with open('temp.txt', 'w+') as fle:
        fle.write(outTxt)
        fle.seek(0)
        for line in fle:
            if 'RequestVerificationToken' in line:
                line = line.split('value=\"')[1].split('\"')[0]
                requestToken = line
                # print(line)
        fle.close()
        os.remove('temp.txt')

    print('Fetching data done')

    text = 'Shamshan ka vaasi pukare tumko'

    s.post(url + 'Messages/SendMessage', data={'__RequestVerificationToken': requestToken, 'userId': userId, 'text': text})
    s.get(url)


s.close()
