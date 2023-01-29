# Unlimited Carwashes
Targets ospt.me a url shortner used by loads of carwash companys.

it works by using the string pip module to make a random 5 character string with random letters and combining it with the ospt.me url, from there it makes a request to the curl and uses BeautifulSoup to see if its a valid link by checking for "<body>Invalid Key</body>". Then it loops logging every link that does not contain "<body>Invalid Key</body>" to found.txt. This can be threaded for larger scale harvesting.

![image](https://user-images.githubusercontent.com/66269103/215306409-9b7b93da-202d-4f50-9594-dd1253bf5d74.png)

![image](https://user-images.githubusercontent.com/66269103/215306439-dbc18ff5-9d6e-4b20-b1f4-0d15e116505d.png)

