import requests 
from bs4 import BeautifulSoup

class Downloader(object):
    
    def __init__(self,manga_link=None):


        self.manga_link = manga_link
        self.page = None
        self.prased_html = None
        self.name = None
        self.chapter_list = {}
        self.last_chapter = None

    def get_info(self,manga_link):

        self.manga_link = manga_link
        self._get_webpage(self.manga_link)
        self._make_soup()
        self.get_name()
        self.get_chapter_list()

    def _make_soup(self):

        self.prased_html =BeautifulSoup(self.page.text,'lxml')

    def _get_webpage(self,page_link):

        self.page = requests.get(page_link)

    def status_code(self):
        return self.page.status_code

    def get_name(self):
         self.name =  str(((self.prased_html.find(class_='story-info-right')).find('h1')).text).replace(' ','_')

    def get_chapter_list(self):

        chapter_list_html = self.prased_html.find(class_='panel-story-chapter-list')
        chapter_list = chapter_list_html.findAll(class_='chapter-name text-nowrap')

        for chapter_link in chapter_list:
            link = str(chapter_link.get('href'))
            chapter_number = link.split('/')[-1]
            self.chapter_list.update({str(chapter_number):str(link)})

        self.last_chapter = list(self.chapter_list.keys())[-1]

        del chapter_list_html
        del chapter_list

    def info(self,name=False,chapters=False,last=False):

        if name:
            if chapters:
                if last:
                    return { 
                    'name':str(self.name),
                    'chapters' : str(self.chapter_list.keys()),
                    'last': str(self.last_chapter)
                    }
                else:
                    return {
                        'name': str(self.name),
                        'chapters':str(self.chapter_list.keys())
                    }
            else:
                if last:
                    return { 
                    'name':str(self.name),
                    'last': str(self.last_chapter)
                    }
                else:
                    return str(self.name)
        else:
            if chapters:
                if last:
                    return { 
                    'chapters' : str(self.chapter_list.keys()),
                    'last': str(self.last_chapter)
                    }
                else:
                    return  str(self.chapter_list.keys())
            else:
                if last:
                    return str(self.last_chapter)
                else:
                    raise ValueError('atleast one of the three argument must be True','name','chapters','last')
        

