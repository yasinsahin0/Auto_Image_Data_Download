import requests

from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=yazbel&tbm=isch"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

for i, j in enumerate(soup.find_all("img")):
    try:
        data = requests.get(j.get("src"), stream=True)
        if b"PNG" in data.content:
            filename = f"img{i}.png"
        elif b"JFIF" in data.content:
            filename = f"img{i}.jpg"
        else:
            filename = f"img{i}"
        with open("data/"+filename, "wb") as f:
            for chunk in data.iter_content(chunk_size=4096):
                f.write(chunk)
    except ValueError as err:
        pass