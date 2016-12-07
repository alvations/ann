from collections import namedtuple
from bs4 import BeautifulSoup

Event = namedtuple('Event', 'id, card, abstract, authors, title, datetime')

events ={}

for i in range(3000, 3040):
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
        events[int(idx)] = Event(id=idx, card=maincard, abstract=abstract, 
                                 authors=authors, title=title, datetime=datetime)

print (events[3039])
print (len(events))
