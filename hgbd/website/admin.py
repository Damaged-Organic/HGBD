# hgbd_project/hgbd/website/admin.py
from django import forms
from django.db import models
from django.contrib import admin
from django.utils.html import escape
from django.conf import settings

import nested_admin
from transmeta import canonical_fieldname

from hgbd.admin import (
    admin_site, DefaultOrderingModelAdmin,
    ForbidAddMixin, ForbidDeleteMixin, ContentBlockMixin
)

from .models import (
    IntroContent, AboutContent, BenefitsContent,
    ServicesContent, TeamContent, GetInTouchContent,
    Number, Benefit, Contact,
    Employee,
    Service, ServiceList, ServiceListItem
)


# Content

@admin.register(IntroContent, site=admin_site)
class IntroContentAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    list_display = ('headline_in_uk', 'headline_out_uk', )

    fieldsets = (
        ('Локалізована інформація', {
            'fields': ('headline_in_uk', 'headline_out_uk', )
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={
            'style': 'width:50%; max-width:50%;'
        })},
    }


@admin.register(AboutContent, site=admin_site)
class AboutContentAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    list_display = ('label_uk', 'title_uk', )

    fieldsets = (
        ('Локалізована інформація', {
            'fields': ('label_uk', 'title_uk', 'text_uk', )
        }),
    )

    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={
            'style': 'resize:none', 'cols': '80', 'rows': '10'
        })}
    }


@admin.register(BenefitsContent, site=admin_site)
class BenefitsContentAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    list_display = ('title_uk', )

    fieldsets = (
        ('Локалізована інформація', {
            'fields': ('title_uk', )
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={
            'style': 'width:50%; max-width:50%;'
        })},
    }


@admin.register(ServicesContent, site=admin_site)
class ServicesContentAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    list_display = ('label_uk', 'title_uk', )

    fieldsets = (
        ('Локалізована інформація', {
            'fields': ('label_uk', 'title_uk', 'text_uk', )
        }),
    )

    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={
            'style': 'resize:none', 'cols': '80', 'rows': '10'
        })}
    }


@admin.register(TeamContent, site=admin_site)
class TeamContentAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    list_display = ('label_uk', 'title_uk', )

    fieldsets = (
        ('Локалізована інформація', {
            'fields': ('label_uk', 'title_uk', 'text_uk', )
        }),
    )

    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={
            'style': 'resize:none', 'cols': '80', 'rows': '10'
        })}
    }


@admin.register(GetInTouchContent, site=admin_site)
class GetInTouchContentAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    list_display = ('title_uk', )

    fieldsets = (
        ('Локалізована інформація', {
            'fields': ('title_uk', 'text_uk', 'link_title_uk', )
        }),
    )

    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={
            'style': 'resize:none', 'cols': '80', 'rows': '10'
        })}
    }


# Common

@admin.register(Number, site=admin_site)
class NumberAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    list_display = ('quantity', 'description_uk', )

    fieldsets = (
        (None, {
            'fields': ('quantity', )
        }),
        ('Локалізована інформація', {
            'fields': ('description_uk', )
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={
            'style': 'width:50%; max-width:50%;'
        })},
    }


@admin.register(Benefit, site=admin_site)
class BenefitAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    readonly_fields = ('id', )
    list_display = ('id', 'text_uk', )
    list_display_links = ('text_uk', )

    fieldsets = (
        ('Локалізована інформація', {
            'fields': ('text_uk', )
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={
            'style': 'width:50%; max-width:50%;'
        })},
    }


@admin.register(Contact, site=admin_site)
class ContactAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    list_display = ('email', 'phone', 'address_legal_uk', 'address_post_uk', )

    fieldsets = (
        (None, {
            'fields': ('email', 'phone', )
        }),
        ('Локалізована інформація', {
            'fields': ('address_legal_uk', 'address_post_uk', ),
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(ContactAdmin, self).formfield_for_dbfield(
            db_field, **kwargs
        )
        db_fieldname = canonical_fieldname(db_field)

        if db_fieldname in ['address_legal', 'address_post']:
            field.widget = forms.TextInput(attrs={
                'style': 'width:50%; max-width:50%;'
            })

        return field


# Employee

@admin.register(Employee, site=admin_site)
class EmployeeAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    readonly_fields = ('id', 'photo_thumb', )
    list_display = ('id', 'position', 'full_name', )
    list_display_links = ('full_name', )

    fieldsets = (
        (None, {
            'fields': ('photo_thumb', 'photo', )
        }),
        ('Локалізована інформація', {
            'fields': ('position_uk', 'name_uk', 'surname_uk', ),
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(EmployeeAdmin, self).formfield_for_dbfield(
            db_field, **kwargs
        )
        db_fieldname = canonical_fieldname(db_field)

        if db_fieldname == 'photo':
            field.help_text = escape(
                """
                Рекомендований розмір фотографії - 600x600 пікселів
                """
            )

        return field


# Service

class ServiceListItemInline(nested_admin.NestedStackedInline):
    model = ServiceListItem
    # TODO: should find the way to bypass transmeta & nested_admin error
    # when translated field present in nested admin view. Leaving default
    # field value for now
    fields = ('text', )
    extra = 0

    formfield_overrides = {
        models.CharField: {'widget': forms.Textarea(attrs={
            'style': 'resize:none; width:100%; max-width:100%;', 'rows': 3
        })},
    }

    '''
    Custom template to display enumerated tabular inline
    '''
    template = "admin/inlines/tabular.html"


class ServiceListInline(
    ForbidAddMixin, ForbidDeleteMixin, nested_admin.NestedTabularInline
):
    model = ServiceList
    fields = ('label_uk', 'title_uk', )
    max_num = 5
    extra = 0

    inlines = [
        ServiceListItemInline,
    ]

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(ServiceListInline, self).formfield_for_dbfield(
            db_field, **kwargs
        )
        db_fieldname = canonical_fieldname(db_field)

        if db_fieldname == 'title':
            field.widget = forms.Textarea(attrs={
                'style': 'resize:none', 'cols': '80', 'rows': '1'
            })

        return field


@admin.register(Service, site=admin_site)
class ServiceAdmin(
    ForbidAddMixin, ForbidDeleteMixin, nested_admin.NestedModelAdmin
):
    readonly_fields = (
        'id',
        'image_main_preview', 'image_main_thumb_preview', 'image_list_preview',
    )
    list_display = ('id', 'title_uk', 'headline_uk', )
    list_display_links = ('title_uk', )
    ordering = ('id', )

    fieldsets = (
        (None, {
            'fields': (
                'image_main', 'image_main_thumb', 'image_list',
                'image_main_preview',
                'image_main_thumb_preview',
                'image_list_preview',
            ),
        }),
        ('Локалізована інформація', {
            'fields': (
                'title_uk', 'description_uk', 'headline_uk',
                'about_label_uk', 'about_description_uk',
                'hint_title_uk', 'hint_description_uk',
            ),
        }),
    )

    inlines = [
        ServiceListInline,
    ]

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(ServiceAdmin, self).formfield_for_dbfield(
            db_field, **kwargs
        )
        db_fieldname = canonical_fieldname(db_field)

        if db_fieldname in ['title', 'headline']:
            field.widget = forms.TextInput(attrs={
                'style': 'width:50%; max-width:50%;'
            })

        if db_fieldname == 'headline':
            field.help_text = escape(
                """
                Можливе використання тегу '<span>' для
                надання тексту кольорового акценту
                """
            )

        if db_fieldname == 'description':
            field.widget = forms.Textarea(attrs={
                'style': 'resize:none', 'cols': '100', 'rows': '2'
            })

        if db_fieldname == 'hint_description':
            field.widget = forms.Textarea(attrs={
                'style': 'resize:none', 'cols': '100', 'rows': '5'
            })

        if db_fieldname == 'about_description':
            field.widget = forms.Textarea(attrs={
                'style': 'resize:none', 'cols': '100', 'rows': '10'
            })

        return field

    def change_view(self, request, object_id, form_url='', extra_context=None):
        '''
        This `change_view()` override is made to disable rendering of inline
        table headers if object hasn't got any relation to corresponding model
        instances (i.e. `service.servicelist_set.count() <= 0`)
        '''
        service = Service.objects.get(pk=object_id)

        if service.servicelist_set.count() == 0:
            self.inlines = []
        else:
            self.inlines = [ServiceListInline, ]

        return super(ServiceAdmin, self).change_view(
            request, object_id, form_url, extra_context=extra_context
        )
