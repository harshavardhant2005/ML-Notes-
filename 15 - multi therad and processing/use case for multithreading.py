
from bs4 import BeautifulSoup
import threading
import requests as rq
urls = ["https://en.wikipedia.org/wiki/Main_Page","https://en.wikipedia.org/wiki/Talk:Main_Page"]

def fetch_contents(url):
    response = rq.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f"fetch :{len(soup.text)} for url is {url}")
threads =[]
for url in urls:
    t1= threading.Thread(target=fetch_contents,args=(url,))
    threads.append(t1)
    t1.start()

for thread in threads:
    thread.join()
print("web pages are scrapped !")