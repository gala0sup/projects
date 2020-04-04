from .Base import Base 

class Manganelo(Base):
    def __init__(self):
        super().__init__()
        
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