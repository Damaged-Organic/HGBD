# hgbd_project/hgbd/website/forms.py
import datetime

from django import forms
from django.utils.translation import ugettext_lazy as _

from .services.mailer import MailerMixin


class CooperationForm(MailerMixin, forms.Form):
    DATETIME_FORMAT = '%d-%m-%Y %H:%M'

    name = forms.CharField(min_length=2, max_length=250)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        min_length=5, max_length=1000, widget=forms.Textarea
    )
    honeypot = forms.CharField(
        required=False, widget=forms.TextInput(attrs={'style': 'display:none'})
    )

    def __init__(self, *args, **kwargs):
        self._request = kwargs.pop('request', None)
        super(CooperationForm, self).__init__(*args, **kwargs)

        # Name
        self.fields['name'].label = _('Імʼя')
        self.fields['name'].widget.attrs = {
            'placeholder': _('Введіть імʼя'),
            'data-rule-required': 'true',
            'data-msg-required': _('Будь ласка, введіть імʼя'),
            'data-rule-minlength': 2,
            'data-msg-minlength': _('Імʼя занадто коротке'),
            'data-rule-maxlength': 250,
            'data-msg-maxlength': _('Імʼя занадто довге'),
        }
        self.fields['name'].error_messages = {
            'required': _('Будь ласка, введіть імʼя'),
            'min_length': _('Імʼя занадто коротке'),
            'max_length': _('Імʼя занадто довге'),
        }

        # E-mail
        self.fields['email'].label = _('E-mail')
        self.fields['email'].widget.attrs = {
            'placeholder': _('Вкажіть e-mail'),
            'data-rule-required': 'true',
            'data-msg-required': _('Будь ласка, вкажіть e-mail'),
            'data-rule-email': 'true',
            'data-msg-email': _('Це не схоже на валідний e-mail'),
            'data-rule-maxlength': 254,
            'data-msg-maxlength': _('Вказаний e-mail занадто довгий'),
        }
        self.fields['email'].error_messages = {
            'required': _('Будь ласка, вкажіть e-mail'),
            'invalid': _('Це не схоже на валідний e-mail'),
            'max_length': _('Вказаний e-mail занадто довгий'),
        }

        # Message
        self.fields['message'].label = _('Повідомлення')
        self.fields['message'].widget.attrs = {
            'placeholder': _('Залиште повідомлення'),
            'data-rule-required': 'true',
            'data-msg-required': _('Будь ласка, залиште повідомлення'),
            'data-rule-minlength': 5,
            'data-msg-minlength': _('Повідомлення занадто коротке'),
            'data-rule-maxlength': 1000,
            'data-msg-maxlength': _('Повідомлення занадто довге'),
        }
        self.fields['message'].error_messages = {
            'required': _('Будь ласка, залиште повідомлення'),
            'min_length': _('Повідомлення занадто коротке'),
            'max_length': _('Повідомлення занадто довге'),
        }

    def send_email(self):
        '''
        Do not send an email if spam bot is detected, but pretend that
        everything went fine for obfuscation reasons - let them spam
        '''
        if self.cleaned_data['honeypot']:
            return False

        sent_at = datetime.datetime.now()

        subject = (
            'Повідомлення з сайту HG Business Development, ' +
            sent_at.strftime(self.DATETIME_FORMAT)
        )
        template = 'website/emails/cooperation.html'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
            'sent_at': sent_at,
        }

        super(CooperationForm, self).send_email(subject, template, context)
