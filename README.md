# UnlimitedCarwashes
Targets ospt.me a url shortner used by loads of carwash companys.

it works by using the string pip module to make a random 5 character string with random letters and combining it with the ospt.me url, from there it makes a request to the curl and uses BeautifulSoup to see if its a valid link by checking for "<body>Invalid Key</body>". Then it loops logging every link that does not contain "<body>Invalid Key</body>" to found.txt. This can be threaded for larger scale harvesting.
