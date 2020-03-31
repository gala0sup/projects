import pathlib
import shutil

import requests as rq
from bs4 import BeautifulSoup as bs

from scripts.downloader_class import Downloader

test_down = Downloader()

test_down.get_info('https://manganelo.com/manga/huku267071576897767')

info = test_down.info(True,True)

print(info)




""" download_folder = pathlib.Path("D:\\torent\\manga")

page = rq.get('https://manganelo.com/manga/huku267071576897767')

soup = bs(page.text,'lxml')

managa_name = str(((soup.find(class_='story-info-right')).find('h1')).text).replace(' ','_')

chapter_list_html = soup.find(class_='panel-story-chapter-list')

chapter_list = chapter_list_html.findAll(class_='chapter-name text-nowrap')


chapter_links = {}

for chapter_link in chapter_list:
    link = str(chapter_link.get('href'))
    chapter_number = link.split('/')[-1]
    chapter_links.update({str(chapter_number):str(link)})

del soup


for chapter_number,chapter_link in reversed(chapter_links.items()):
    choice = input(str('download '+chapter_number+' [y/n] :- '))
    if choice in ['y','Y']:
        pass
    else:
        break
    print("downloading {}".format(chapter_number))
    chapter_page = rq.get(str(chapter_links[chapter_number]))

    chapter_soup = bs(chapter_page.text,'lxml')

    chapter_reader = (chapter_soup.find(class_='container-chapter-reader')).findAll('img')

    image_links = []


    for image_link in chapter_reader:
        link = str(image_link.get('src'))
        image_links.append(link)


    for link in image_links:
        image_data = rq.get(link,stream=True).raw
        filename = str(link.split('/')[-1])
        print('\t'+filename)
        final_dir_path = download_folder / managa_name / chapter_number
        pathlib.Path(final_dir_path).mkdir(parents=True,exist_ok=True)
        final_path = final_dir_path / filename
        image_file = open(final_path ,'wb')
        shutil.copyfileobj(image_data,image_file)
        image_file.close
        del image_data """



'''
for i,j in chapter_links.items():
    print(i+' : '+j)
'''
