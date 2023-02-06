import threading
import random
import requests
import sys
import os
import string
from bs4 import BeautifulSoup
from unshortenit import UnshortenIt
unshortener = UnshortenIt()

t = 0
threadcount = 0
letters = string.ascii_letters
threads = int(input("> input Thread Count\n> "))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
  valid = 0
  invalid = 0
  expired = 0
  while True:
    url = (f"https://ospt.me/{''.join(random.choice(letters) for i in range(5))}")
    x = requests.get(url)
    soup = BeautifulSoup(x.content, 'html.parser')
    text = str(soup.body)
    if "<body>Invalid Key</body>" in text:
        clear()
        invalid = invalid + 1
    elif "<h1>Error: coupon not found.</h1>" in text:
        clear()
        invalid = invalid + 1
    elif "<h1>Coupon: Not Shareable</h1>" in text:
        clear()
        invalid = invalid + 1
    elif '</div><div style="text-align:center;color:red;font-size:16px;">Sorry, this coupon has expired.</div>' in text:
        clear()
        expired = expired + 1
    elif '<div class="style_it"> <i class="fa fa-exclamation-triangle fa-danger fa-10x" style="color:#990000;"></i>This Coupon Is No Longer Valid </div>' in text:
        clear()
        expired = expired + 1
    else:
        clear()
        session = requests.Session()  # so connections are recycled
        resp = session.head(url, allow_redirects=True)
        uri = unshortener.unshorten(url)
        y = requests.get(uri)
        coupon = BeautifulSoup(y.content, 'html.parser')

        for title in coupon.find_all('title'):
            brand = (title.get_text())
            f = open("found.txt", "a")
            f.write(f"{brand} > {url} > {uri}\n")
            f.close()
        valid = valid + 1
        pass

    print(f"> {url} > valid : {valid} > Expired {expired} > invalid : {invalid}")

for i in range(threads):
    threading.Thread(target=main).start()
    threadcount = threadcount+1
    print(f"> Thread loaded | {threadcount}/{threads}")
                
print(f"> {threads} Threads Loaded")
