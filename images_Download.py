import os

import requests
from bs4 import BeautifulSoup


class ImageDownload:
    def __init__(self):
        self.data_file_path = "html_content/"
        self.save_file_path = "data/"

    def HtmlDataFileList(self):
        file_name_list = os.listdir(self.data_file_path)
        for i in file_name_list:
            if i[-4:] != "html":
                file_name_list.remove(i)
        return file_name_list

    def FileFolderName(self,file_name_list):
        for name in file_name_list:
            folder_name = name[:-5]
            self.Download(folder_name,name)

    def Download(self,folder_name,html_file_name):
        os.mkdir("data/"+folder_name)
        with open("html_content/"+html_file_name) as fp:
            soup = BeautifulSoup(fp, 'html.parser')

        for i, j in enumerate(soup.find_all("img")):
            try:
                data = requests.get(j.get("src"), stream=True)
                if b"PNG" in data.content:
                    filename = f"img{i}.png"
                elif b"JFIF" in data.content:
                    filename = f"img{i}.jpg"
                else:
                    filename = f"img{i}"
                with open("data/" + folder_name + "/" + filename, "wb") as f:
                    for chunk in data.iter_content(chunk_size=4096):
                        f.write(chunk)
            except ValueError as err:
                print("Value Error : ",err)

if __name__ == "__main__":
    ID = ImageDownload()
    file_name_list = ID.HtmlDataFileList()
    ID.FileFolderName(file_name_list)