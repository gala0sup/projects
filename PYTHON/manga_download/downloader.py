from scripts.downloader_class import Downloader

test_down = Downloader()

test_down.get_info('https://manganelo.com/manga/we922424')

test_down.set_download_dir('D:\\torrent\\manga')

test_down.download()


