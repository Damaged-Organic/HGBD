# hgbd_project/hgbd/website/views.py
from django.shortcuts import render


def index(request):
    return render(request, 'website/index.html')


def service(request, id, slug=None):
    return render(request, 'website/service.html')


def cooperation(request):
    return render(request, 'website/cooperation.html')


def handler400(request):
    return render(request, 'website/errors/400.html', {}, status=400)


def handler403(request):
    return render(request, 'website/errors/403.html', {}, status=403)


def handler404(request):
    return render(request, 'website/errors/404.html', {}, status=404)


def handler500(request):
    return render(request, 'website/errors/500.html', {}, status=500)
