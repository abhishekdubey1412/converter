from django.shortcuts import render
from converter import mod

def Home(request):
    data = {
        'title':"Responsive Navigation Bar"
    }
    return render(request, "index.html",data)

def PDFJPG(request):
    data = {
        'title':"PDF TO JPG"
    }
    return render(request, "pdf_to_jpg.html",data)

def JPGPNG(request):
    data = {
        'title':"JPG TO PNG"
    }
    return render(request, "jpg-to-png.html",data)

def YOUTUBE(request):
    link = ''
    try:
        link = request.POST['yt_link']
    except:
        pass
    data = {
        'title':"Youtube Downloader"
    }
    
    if link != '':
        mod.youtube_downloader(link)
    else:
        pass
    return render(request, "yt_down.html",data)

def NotFound(request):
    return render(request, '404.html')