import requests
from bs4 import BeautifulSoup

class Base(object):
    def __init__(self):


        

        self.page = None # requests response
        self.prased_html = None # BeautifulSoup soup

        self.manga_link = None # link of the webpage 
        self.name = None # Managa name
        self.author = None # Name of the Author
        self.status = None # Ongoing or completed
        self.updated = None # last date manga was updated is a string 
        self.view  = None # Number of Views
        self.rating = None #  number out of five 


        self.total_chapters = None # Number of chapters
        self.chapter_list = {}  # {'chapter number':'chapter link'}
        self.chapter_names = {} # {'chapter number':'chapter name'}
        self.last_chapter = None # last_chapter


        self.number_of_pages = None # Number of Pages in a chapter 
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
         pass

    def get_chapter_list(self):
        pass

    def info(self):
        return {
            'name':self.name,
            'chapters':self. total_chapters,
            'last':self.last_chapter
        }
