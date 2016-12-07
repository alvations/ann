from bs4 import BeautifulSoup

with open('NIPS 2016 Annual Meeting.html', 'r') as fin:
    soup = BeautifulSoup(fin.read())
    cards = soup.find_all('div', {'class':'maincard'})
    idx = [int(card['id'].split('_')[-1]) for card in cards]


#print(idx)
print (len(idx))
print(min(idx), max(idx))
