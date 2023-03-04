import requests
import string
import random
from bs4 import BeautifulSoup
import shutil

def random_string(length):
   chars = string.ascii_lowercase
   chars += string.digits
   return ''.join(random.choice(chars) for i in range(length))

downloads = 0
print("Scraping....")
while True:
    id = random_string(random.choice([6,7]))
    print("Trying "+id+"....")
    URL = "https://prnt.sc/"+id
    request = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(request.text, 'html.parser')

    images = soup.find_all('img')

    src = images[0].get('src')
    image_url = requests.compat.urljoin(URL, src)

    if str(image_url) not in ["https://st.prntscr.com/2022/05/15/0209/img/0_173a7b_211be8ff.png",
                              "https://st.prntscr.com/2022/05/15/0209/img/footer-logo.png"]:

            if "https://i.imgur.com/" not in str(image_url):

                response = requests.get(image_url, stream = True, headers={'User-Agent': 'Chrome'})
                if response.status_code == 200:
                    print("Success! downloading " + id + "....")
                    with open('imgs/'+id+'.png', 'wb') as f:
                        shutil.copyfileobj(response.raw, f)

                    downloads += 1
                    if downloads == 300:
                        break
print("Done")