from pdf2image import convert_from_path
from PIL import Image
from pytube import YouTube

def pdf_to_jpg():
    images = convert_from_path('Resume.pdf',500,poppler_path='C:\\Program Files\\poppler-23.07.0\\Library\\bin')

    for i in range(len(images)):
        images[i].save('page'+ str(i) +'.jpg', 'JPEG')

def jpg_to_png():
    image = Image.open('page0.jpg')
    image.save('output.png')

def png_to_jpg():
    image = Image.open('output.png')
    image.convert('RGB').save('output.jpg')

def youtube_downloader(video_url):
    YouTube(video_url).streams.get_highest_resolution().download()
