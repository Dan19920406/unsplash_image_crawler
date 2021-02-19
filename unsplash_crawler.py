import requests
import json
import time
import os

def unsplash_crawler(path:str,queries:str,pages:int):
    for page in range(1,pages+1):
        query = queries.replace(' ','').replace(',','%2C%20')
        r = requests.get(f'https://unsplash.com/napi/search/photos?query={query}&per_page=20&page={page}&xp=feedback-loop-v2%3Acontrol')
        print(f'Page : {page}')
        tmp = json.loads(r.text)
        for l in tmp['results']:
            if str(l['alt_description']).upper() == 'NONE':
                alt = l['id']
            else:
                alt = l['alt_description']
            url = l['links']['download']
            print(f'{alt} : {url}')
            with open(f'{p}/{alt}.jpg', 'wb') as f:
                f.write(requests.get(url).content)
        time.sleep(1)
        
q = input('What are you searching for? \n(Please use comma split the queries, ex : car,wheels,bumper) : ')
t = input('Enter scroll times : \n(20 images/per scroll) : ')
os.mkdir(f'image-{q}')
p = os.path.join(os.getcwd(),f'image-{q}')
unsplash_crawler(p,q,int(t))
print('Process finish...')
