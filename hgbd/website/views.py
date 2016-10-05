# hgbd_project/hgbd/website/views.py
import time
import json

from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext as _
from django.http import HttpResponse
from django.shortcuts import render

from .forms import CooperationForm
from .services.form_helpers import get_form_errors


def index(request):
    return render(request, 'website/index.html')


def service(request, id, slug=None):
    return render(request, 'website/service.html')


def cooperation(request):
    form = CooperationForm(request=request)

    return render(request, 'website/cooperation.html', {
        'form': form
    })


def cooperation_send(request):
    if request.method == 'POST':
        form = CooperationForm(request.POST, request=request)

        if form.is_valid():
            message = _('Дякуємо за повідомлення!')
            response = {
                'data': {'message': message},
                'code': 200,
            }

            form.send_email()
        else:
            errors = get_form_errors(form, form.errors.items())

            message = _('При обробці форми виникли помилки')
            response = {
                'data': {'errors': errors, 'message': message},
                'code': 400,
            }
    else:
        raise PermissionDenied

    '''
    Artificial delay from considerations of performance and UX
    '''
    time.sleep(1)

    return HttpResponse(
        json.dumps(response['data']), status=response['code']
    )


def handler400(request):
    return render(request, 'website/errors/400.html', {}, status=400)


def handler403(request):
    return render(request, 'website/errors/403.html', {}, status=403)


def handler404(request):
    return render(request, 'website/errors/404.html', {}, status=404)


def handler500(request):
    return render(request, 'website/errors/500.html', {}, status=500)
