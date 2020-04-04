import base64
import os
import pathlib
import re
import shutil
import string

import requests
from bs4 import BeautifulSoup


class Downloader(object):
    
    def __init__(self,manga_link=None):


        self.manga_link = manga_link
        self.page = 'a'
        self.prased_html = None
        self.name = None
        self.chapter_list = {}
        self.total_chapters = None
        self.chapter_names = {}
        self.last_chapter = None
        
        self.download_dir = None
        self.image_links= []

    def get_info(self,manga_link):

        self.manga_link = manga_link
        self._get_webpage(self.manga_link)
        self._make_soup()
        self.get_name()
        self.get_chapter_list()

    def _make_soup(self):

        self.prased_html =BeautifulSoup(self.page.text,'lxml')

    def _get_webpage(self,page_link,_stream=False,_raw=False):

        if _raw:
            self.page = requests.get(page_link,stream=_stream).raw
        else:
            self.page = requests.get(page_link,stream=_stream)

    def status_code(self):
        return self.page.status_code

    def get_name(self):
         self.name =  str(((self.prased_html.find(class_='story-info-right')).find('h1')).text).replace(' ','_')

    def get_chapter_list(self):

        chapter_list_html = self.prased_html.find(class_='panel-story-chapter-list')
        chapter_list = chapter_list_html.findAll(class_='chapter-name text-nowrap')

        for chapter_link in chapter_list:
            link = str(chapter_link.get('href'))
            chapter_name = str(chapter_link.get('title'))
            chapter_number = link.split('/')[-1]
            self.chapter_list.update({str(chapter_number) : str(link)})
            self.chapter_names.update({str(chapter_number) : str(chapter_name)})

        self.total_chapters = len(self.chapter_list.keys())
        self.last_chapter = list(self.chapter_list.keys())[0]


        del chapter_list_html
        del chapter_list

    def info(self):
        return {
            'name':self.name,
            'chapters':self. total_chapters,
            'last':self.last_chapter
        }
        
    def download(self,link=None):
        choice = input('choose option \n1. download all \n2.download from list \n')
        if self.download_dir != None:
            if choice==1:
                for chapter_number in reversed(self.chapter_list.keys()):
    
                    print("downloading {}".format(chapter_number))

                    self._get_webpage(self.chapter_list[chapter_number])
                    self._make_soup()
                    self._get_image_links()

                    for link in self.image_links:
                        self._download_image(link,chapter_number)

            else:
                while True:

                    while True:

                        print('choose from chapter list\n')
                        print('chapter number : chapter name')
                        for i in self.chapter_names.keys():
                            print(i,' : ', self.chapter_names[i])

                        chapter_number = input('\n chapter number :- ') 
                        
                        if chapter_number  in self.chapter_list.keys():

                            
                            print("downloading {} : {}".format(chapter_number,self.chapter_names[chapter_number]))

                            self._get_webpage(self.chapter_list[chapter_number])
                            self._make_soup()
                            self._get_image_links()

                            for link in self.image_links:
                                self._download_image(link,chapter_number)

                        else:
                            print('chapter not in list try again ... \n')
                            os.system('cls')
                                
                    print('\n\n\n Download more ? [y/n] :- ')
                    choice = input()

                    if choice == 'y':
                        os.system('cls')
                    else:
                        break



                
        else:
            print('\n Download dir not set \nPlease enter download dir :- ')
            self.set_download_dir(input())


    def _get_image_links(self):

        chapter_reader = (self.prased_html.find(class_='container-chapter-reader')).findAll('img')

        for image_link in chapter_reader:
            link = str(image_link.get('src'))
            self.image_links.append(link)

    def _download_image(self,link,chapter_number):

        self._get_webpage(link,_stream=True,_raw=True)
        image_data = self.page

        filename = str(link.split('/')[-1])
        print('\t'+filename)

        
        final_dir_path = self.download_dir / self.name / self._slugify(str(self.chapter_names[str(chapter_number)]))
        pathlib.Path(final_dir_path).mkdir(parents=True,exist_ok=True)
        final_path = final_dir_path / filename

        self._save_image(image_data,final_path)

        del image_data 

    def _save_image(self,image_data,image_file_name):

        image_file = open(image_file_name ,'wb')
        shutil.copyfileobj(image_data,image_file)
        image_file.close
        
    def set_download_dir(self, directory):

        self.download_dir = pathlib.Path(directory)
    
    def _slugify(self,value):
        """
        Normalizes string, converts to lowercase, removes non-alpha characters,
        and converts spaces to hyphens.
        """
        pure = ''
        for i in value.strip().replace(' ','_'):
            if i in string.punctuation.replace('_','').replace('(','').replace(')','').replace('.',''):
                pure += '_'
            else:
                pure += i
        return pure
