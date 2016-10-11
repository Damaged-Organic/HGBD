# hgbd_project/hgbd/hgbd/admin.py
from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin


# Common admin mixins

class ForbidDeleteMixin():
    def get_actions(self, request):
        actions = super(ForbidDeleteMixin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False


class ForbidAddMixin():
    def has_add_permission(self, request):
        return False


class ContentBlockMixin(ForbidDeleteMixin, ForbidAddMixin):
    exclude = ('name',)


# Admin site

class DefaultOrderingModelAdmin(admin.ModelAdmin):
    ordering = ('id',)


class HgbdAdminSite(admin.AdminSite):
    site_title = 'HG Business Development'
    site_header = 'HG Business Development'
    index_title = 'HG Business Development - Керування контентом'

admin_site = HgbdAdminSite(name='deus_ex_machina')


@admin.register(Group, site=admin_site)
class GroupAdmin(GroupAdmin):
    pass


@admin.register(User, site=admin_site)
class UserAdmin(UserAdmin):
    pass
