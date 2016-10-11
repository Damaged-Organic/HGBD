import re

from django.db import models
from django.utils.safestring import mark_safe
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

from transmeta import TransMeta
from transliterate import translit

"""
Hack to order models in Django Admin. Whitespaces assigned in nested Meta
classes are concatenated with verbose_name_plural to force ordering by
whitespaces number
"""
models.options.DEFAULT_NAMES += ('order_prefix',)


def get_table_name(*args):
    """ Getting the correct and clean table name """
    app_label = 'website'
    return '_'.join((app_label, ) + args)


# Content

class ContentBlock(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name or self.__name__

    def get_template_block_name(self):
        return self.name.replace(' ', '_').lower()


class IntroContent(ContentBlock, metaclass=TransMeta):
    headline_in = models.CharField('Слоган (вступ)', max_length=50)
    headline_out = models.CharField('Слоган (висновок)', max_length=50)

    class Meta:
        db_table = get_table_name('content', 'intro')

        order_prefix = ' ' * 11

        verbose_name = 'Блок "Вступ"'
        verbose_name_plural = order_prefix + verbose_name

        translate = ('headline_in', 'headline_out', )


class AboutContent(ContentBlock, metaclass=TransMeta):
    label = models.CharField('Ярлик', max_length=20)
    title = models.CharField('Заголовок', max_length=50)
    text = models.TextField('Текст', max_length=500)

    class Meta:
        db_table = get_table_name('content', 'about')

        order_prefix = ' ' * 10

        verbose_name = 'Блок "Компанія"'
        verbose_name_plural = order_prefix + verbose_name

        translate = ('label', 'title', 'text', )


class BenefitsContent(ContentBlock, metaclass=TransMeta):
    title = models.CharField('Заголовок', max_length=50)

    class Meta:
        db_table = get_table_name('content', 'benefits')

        order_prefix = ' ' * 9

        verbose_name = 'Блок "Переваги"'
        verbose_name_plural = order_prefix + verbose_name

        translate = ('title', )


class ServicesContent(ContentBlock, metaclass=TransMeta):
    label = models.CharField('Ярлик', max_length=20)
    title = models.CharField('Заголовок', max_length=50)
    text = models.TextField('Текст', max_length=500)

    class Meta:
        db_table = get_table_name('content', 'services')

        order_prefix = ' ' * 8

        verbose_name = 'Блок "Сервіси"'
        verbose_name_plural = order_prefix + verbose_name

        translate = ('label', 'title', 'text', )


class TeamContent(ContentBlock, metaclass=TransMeta):
    label = models.CharField('Ярлик', max_length=20)
    title = models.CharField('Заголовок', max_length=50)
    text = models.TextField('Текст', max_length=500)

    class Meta:
        db_table = get_table_name('content', 'team')

        order_prefix = ' ' * 7

        verbose_name = 'Блок "Команда"'
        verbose_name_plural = order_prefix + verbose_name

        translate = ('label', 'title', 'text', )


class GetInTouchContent(ContentBlock, metaclass=TransMeta):
    title = models.CharField('Заголовок', max_length=50)
    text = models.TextField('Текст', max_length=500)
    link_title = models.CharField('Заголовок посилання', max_length=20)

    class Meta:
        db_table = get_table_name('content', 'get_in_touch')

        order_prefix = ' ' * 6

        verbose_name = 'Блок "Звʼязок"'
        verbose_name_plural = order_prefix + verbose_name

        translate = ('title', 'text', 'link_title', )


# Common

class Number(models.Model, metaclass=TransMeta):
    quantity = models.IntegerField('Значення', default=1, validators=[
        MinValueValidator(1),
        MaxValueValidator(99)
    ])
    description = models.CharField('Опис', max_length=50)

    class Meta:
        db_table = get_table_name('numbers')

        order_prefix = ' ' * 5

        verbose_name = 'Цифра'
        verbose_name_plural = order_prefix + 'Цифри'

        translate = ('description', )

    def __str__(self):
        return self.description or self.__name__


class Benefit(models.Model, metaclass=TransMeta):
    text = models.CharField('Опис переваги', max_length=200)

    class Meta:
        db_table = get_table_name('benefits')

        order_prefix = ' ' * 4

        verbose_name = 'Перевага'
        verbose_name_plural = order_prefix + 'Переваги'

        translate = ('text', )

    def __str__(self):
        return self.text or self.__name__


class Contact(models.Model, metaclass=TransMeta):
    email = models.CharField('E-mail', max_length=254)
    phone = models.CharField('Телефон', max_length=19)
    address_legal = models.CharField('Юридична адреса', max_length=300)
    address_post = models.CharField('Адреса для листування', max_length=300)

    class Meta:
        db_table = get_table_name('contacts')

        order_prefix = ' ' * 3

        verbose_name = 'Контакт'
        verbose_name_plural = order_prefix + 'Контакти'

        translate = ('address_legal', 'address_post', )

    def __str__(self):
        return self._meta.verbose_name or self.__name__

    @property
    def get_phone_code(self):
        return re.search(r'\((.*)\)', self.phone).group(1)

    @property
    def get_phone_number(self):
        return re.search(r'(\d{3}-\d{2}-\d{2})', self.phone).group(1)


# Employee

class Employee(models.Model, metaclass=TransMeta):
    PHOTO_PATH = 'employee/photos/'

    position = models.CharField('Посада', max_length=100)
    name = models.CharField('Імʼя', max_length=200)
    surname = models.CharField('Прізвище', max_length=200)

    photo = models.ImageField('Фотографія', upload_to=PHOTO_PATH)

    class Meta:
        db_table = get_table_name('employees')

        order_prefix = ' ' * 2

        verbose_name = 'Співробітник'
        verbose_name_plural = order_prefix + 'Співробітники'

        translate = ('position', 'name', 'surname', )

    def __str__(self):
        return self.position or self.__name__

    @property
    def full_name(self):
        return "%s %s" % (self.name, self.surname)

    def photo_thumb(self):
        return '<img src=\"%s\" width=\"400\">' % (self.photo.url)
    photo_thumb.allow_tags = True
    photo_thumb.short_description = 'Превʼю фотографії'


# Service

class Service(models.Model, metaclass=TransMeta):
    IMAGE_PATH_MAIN = 'service/images/main/'
    IMAGE_PATH_MAIN_THUMB = 'service/images/main/thumb/'
    IMAGE_PATH_LIST = 'service/images/list/'

    # TODO: slug doesn't support i18n for now
    slug = models.SlugField(editable=False)

    title = models.CharField('Заголовок', max_length=100)
    description = models.CharField('Короткий опис', max_length=500, null=True)
    headline = models.CharField('Слоган', max_length=200)

    about_label = models.CharField('Ярлик', max_length=20)
    about_description = models.TextField('Детальний опис', max_length=1500)

    hint_title = models.CharField('Заголовок визначення', max_length=100)
    hint_description = models.CharField('Текст визначення', max_length=500)

    image_main = models.ImageField(
        'Головне зображення',
        upload_to=IMAGE_PATH_MAIN,
        null=True,
        blank=True
    )
    image_main_thumb = models.ImageField(
        'Мініатюра головного зображення',
        upload_to=IMAGE_PATH_MAIN_THUMB,
        null=True
    )
    image_list = models.ImageField(
        'Зображення до списку',
        upload_to=IMAGE_PATH_LIST,
        null=True,
        blank=True
    )

    class Meta:
        db_table = get_table_name('services')

        order_prefix = ' ' * 1

        verbose_name = 'Сервіс'
        verbose_name_plural = order_prefix + 'Сервіси'

        translate = (
            'title', 'description', 'headline',
            'about_label', 'about_description',
            'hint_title', 'hint_description',
        )

    def __str__(self):
        return self.title or self.__name__

    def save(self, *args, **kwargs):
        if self.title:
            # TODO: 'uk' parameter should be changed in case of extra locale
            transliterated = translit(self.title, 'uk', reversed=True)
            self.slug = slugify(transliterated).replace('-', '_')

        super(Service, self).save(*args, **kwargs)

    def get_service_lists(self):
        return self.servicelist_set.all()

    def image_main_preview(self):
        return '<img src="%s" width="400">' % (self.image_main.url)
    image_main_preview.allow_tags = True
    image_main_preview.short_description = 'Превʼю головного зображення'

    def image_main_thumb_preview(self):
        return '<img src="%s" width="400">' % (self.image_main_thumb.url)
    image_main_thumb_preview.allow_tags = True
    image_main_thumb_preview.short_description = (
        'Превʼю мініатюри головного зображення'
    )

    def image_list_preview(self):
        return '<img src="%s" width="400">' % (self.image_list.url)
    image_list_preview.allow_tags = True
    image_list_preview.short_description = 'Превʼю зображення до списку'


class ServiceList(models.Model, metaclass=TransMeta):
    label = models.CharField('Ярлик', max_length=50)
    title = models.CharField('Заголовок', max_length=100)

    service = models.ForeignKey(
        Service, null=True, blank=True, on_delete=models.SET_NULL
    )

    class Meta:
        db_table = get_table_name('services', 'lists')

        verbose_name = 'Список характеристик сервісу'
        verbose_name_plural = 'Списки характеристик сервісу'

        translate = ('label', 'title', )

    def __str__(self):
        return self.label or self.__name__

    def get_service_list_items(self):
        return self.servicelistitem_set.all()


# TODO: should find the way to bypass transmeta & nested_admin error
# when translated field present in nested admin view. For now required
# 'metaclass=TransMeta' is omitted in class declaration, as well as
# 'translate' property in Meta class
class ServiceListItem(models.Model):
    text = models.CharField('Опис пункту', max_length=500)

    service_list = models.ForeignKey(
        ServiceList, null=True, blank=True, on_delete=models.SET_NULL
    )

    class Meta:
        db_table = get_table_name('services', 'lists', 'items')

        verbose_name = 'Пункт списку характеристик сервісу'
        verbose_name_plural = 'Пункти списку характеристик сервісу'

    def __str__(self):
        return self.text or self.__name__
