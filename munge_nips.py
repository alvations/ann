import pickle
from collections import namedtuple

from bs4 import BeautifulSoup

Event = namedtuple('Event', 'id, card, abstract, authors, title, datetime, type')

events ={}
for i in range(9999):
    with open('data/'+str(i)+'.html') as fin:
        soup = BeautifulSoup(fin.read())
        maincard = soup.find_all('div', {'class':'maincard'})
        if not maincard:
            continue
        assert len(maincard) == 1
        maincard = maincard[0]

        abstract = soup.find_all('div', {'class':'abstractContainer'})[0].text

        idx = maincard['id'].split('_')[-1]

        authors = soup.find('div', {'class':'maincardFooter'}).text
        datetime = soup.find('div', {'class':'maincardHeader'}).text
        title = soup.find('div', {'class':'maincardBody'}).text
        type = soup.find('div', {'class':'maincardType'}).text

        events[int(idx)] = Event(id=idx, card=maincard, abstract=abstract, type=type, 
                                 authors=authors, title=title, datetime=datetime)

with open('nips2016.pk', 'wb') as fout:
    pickle.dump(events, fout)

print (len(events)) # Hint: Use Python3 not 2. https://pythonclock.org
