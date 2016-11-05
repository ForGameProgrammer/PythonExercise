import urllib.request

def download_file(url, file_name):
    urllib.request.urlretrieve(url, file_name)

download_file("https://s-media-cache-ak0.pinimg.com/originals/2b/2d/05/2b2d05bd3a23cef4befcf4452339ccc3.jpg","The Flash.jpg")
