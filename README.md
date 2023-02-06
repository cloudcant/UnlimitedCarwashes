# Unlimited Carwashes
Targets ospt.me a url shortner used by loads of carwash companys.

> it works by using the string pip module to make a random 5 character string with random letters and combining it with the ospt.me url, from there it makes a request to the url and uses BeautifulSoup to see if its a valid link by checking for "<body>Invalid Key</body>". When it finds a valid link it unshortens it and grabs the details and logs everythig to found.txt (check it out in this repo) . This process is then threaded for larger scale harvesting.

> There is a bug with "This coupon is no longer valid" and ill fix it if anyone asks

## Usage

> [Screen recording 2023-02-05 10.13.49 PM.webm](https://user-images.githubusercontent.com/66269103/216882297-3dd54946-2607-4455-a732-7e996d117715.webm)

## Output

> ![image](https://user-images.githubusercontent.com/66269103/216882514-33ac71ee-5fc9-45d8-a487-debb2f3dca57.png)

