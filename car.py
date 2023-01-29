import threading
import random
import requests
import sys
import string
from bs4 import BeautifulSoup

t = 0
threadcount = 0
letters = string.ascii_letters
threads = int(input("> input Thread Count\n> "))

def main():
  while True:
    url = (f"https://ospt.me/{''.join(random.choice(letters) for i in range(5))}")
    x = requests.get(url)
    soup = BeautifulSoup(x.content, 'html.parser')
    text = str(soup.body)
    if text == "<body>Invalid Key</body>":
        pass
    else:
        print(f"> Found : {url}")
        f = open("found.txt", "a")
        f.write(f"{url}\n")
        f.close()
    

for i in range(threads):
    threading.Thread(target=main).start()
    threadcount = threadcount+1
    print(f"> Thread loaded | {threadcount}/{threads}")
                
print(f"> {threads} Threads Loaded")
