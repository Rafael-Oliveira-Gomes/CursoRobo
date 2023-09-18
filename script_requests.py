import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.gabrielcasemiro.com.br")


if page.status_code == 200:
    print(page.text)

else:
    print("HTTP error ", page.status_code)
    
soup = BeautifulSoup(page.text)

#o codigo para, para poder verificar os dados html
import pdb; pdb.set_trace()




