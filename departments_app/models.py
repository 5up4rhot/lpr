from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from people_app.models import Profile
from cities_light.models import Country, Region, City
from uuslug import slugify


def department_logo_directory_path(instance, filename):
    return 'department/logos/{}.{}'.format(instance.region, filename.split(".")[-1])


class Department(models.Model):
    county = models.ForeignKey(Country, verbose_name='Страна', on_delete=models.CASCADE)
    region = models.ForeignKey(Region, verbose_name='Регион', on_delete=models.CASCADE)
    city = models.ForeignKey(City, verbose_name='Город',
                             on_delete=models.CASCADE, blank=True, null=True)
    info = RichTextField(verbose_name='Информация', blank=True, null=True)
    logo = models.ImageField(verbose_name='Логотип',
                             upload_to=department_logo_directory_path, blank=True, null=True)
    contacts = models.ManyToManyField(Profile, verbose_name='Контакты', blank=True)
    website = models.URLField(verbose_name='Собственный сайт', blank=True, null=True)
    telegram_channel = models.URLField(verbose_name='Канал в telegram', blank=True, null=True)
    telegram_chat = models.URLField(verbose_name='Чат в telegram', blank=True, null=True)
    vk_group = models.URLField(verbose_name='Группа Вконтакте', blank=True, null=True)
    fb_group = models.URLField(verbose_name='Группа Facebook', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('people_app:department_detail', args=[self.region])

    def __str__(self):
        if self.city:
            return self.city
        else:
            return self.region
