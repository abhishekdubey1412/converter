from django.http import HttpResponse
from django.shortcuts import render

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
    data = {
        'title':"Youtube Downloader"
    }
    return render(request, "yt_down.html",data)

def NotFound(request):
    return render(request, '404_templet.html')