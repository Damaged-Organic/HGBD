# hgbd_project/hgbd/website/views.py
import time
import json

from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.shortcuts import (
    render, get_object_or_404, get_list_or_404
)

from .services.form_helpers import get_form_errors
from .models import (
    IntroContent, AboutContent, BenefitsContent,
    ServicesContent, TeamContent, GetInTouchContent,
    Number, Benefit, Contact,
    Employee, Service
)
from .forms import CooperationForm


def index(request):
    ''' Index '''
    content = {
        block.get_template_block_name(): block for block in [
            IntroContent.objects.first(),
            AboutContent.objects.first(),
            BenefitsContent.objects.first(),
            ServicesContent.objects.first(),
            TeamContent.objects.first(),
            GetInTouchContent.objects.first(),
        ]
    }

    numbers = get_list_or_404(Number)
    benefits = get_list_or_404(Benefit)
    employees = get_list_or_404(Employee)
    services = get_list_or_404(Service)
    contacts = get_object_or_404(Contact)

    return render(request, 'website/index.html', {
        'content': content,
        'numbers': numbers,
        'benefits': benefits,
        'contacts': contacts,
        'employees': employees,
        'services': services,
        'contacts': contacts
    })


def service(request, pk, slug=None):
    ''' Service '''
    content = {
        block.get_template_block_name(): block for block in [
            GetInTouchContent.objects.first(),
        ]
    }

    service = get_object_or_404(
        Service.objects.prefetch_related(
            'servicelist_set__servicelistitem_set'
        ),
        pk=pk
    )

    contacts = get_object_or_404(Contact)

    return render(request, 'website/service.html', {
        'content': content,
        'service': service,
        'contacts': contacts,
    })


def cooperation(request):
    ''' Cooperation '''
    content = {
        block.get_template_block_name(): block for block in [
            GetInTouchContent.objects.first(),
        ]
    }

    contacts = get_object_or_404(Contact)

    form = CooperationForm(request=request)

    return render(request, 'website/cooperation.html', {
        'content': content,
        'contacts': contacts,
        'form': form,
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
