
from requests import get

def download(url, file_name): # From http://stackoverflow.com/a/34964610/610569
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)


for i in range(9999):
    url = 'https://nips.cc/Conferences/2016/Schedule?showEvent=' + str(i)
    download(url, 'data/'+str(i)+'.html')
