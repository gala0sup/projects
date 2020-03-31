import requests 
from bs4 import BeautifulSoup

class Downloader(object):
    
    def __init__(self,manga_link=None):


        self.manga_link = manga_link
        self.page = None
        self.prased_html = None
        self.name = None
        self.chapter_list = {}
        self.total_chapters = None
        self.last_chapter = None
        self.download_dir = None

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
        choice = input('choose option \n1. download all \n2.download from list')
        if self.download_dir != None:
            if choice==1:
                for chapter_number,chapter_link in reversed(self.chapter_list.items()):
    
                    print("downloading {}".format(chapter_number))

                    self._get_webpage(self.chapter_list[chapter_number])
                    self._make_soup()

                    chapter_reader = (self.prased_html.find(class_='container-chapter-reader')).findAll('img')

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
                        del image_data 
        else:
            print('\n Download dir not set \nPlease enter download dir :- ')
            self._set_download_dir(input())


    def _get_image_links(self):
        pass
    def _download_image(self):
        pass
    def _save_image(self):
        pass
    def _set_download_dir(self, directory):
        self.download_dir = directory