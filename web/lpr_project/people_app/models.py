from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from cities_light.models import Country, Region, City
from slugify import slugify


def profile_photo_directory_path(instance, filename):
    return 'people/photos/{}.{}'.format(instance.slug, filename.split(".")[-1])


class Profile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(verbose_name='Фотография',
                              upload_to=profile_photo_directory_path, blank=True, null=True)
    bio = RichTextField(verbose_name='Биография', blank=True, null=True)
    county = models.ForeignKey(Country, verbose_name='Страна',
                               on_delete=models.CASCADE, blank=True, null=True)
    region = models.ForeignKey(Region, verbose_name='Регион',
                               on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(City, verbose_name='Город',
                             on_delete=models.CASCADE, blank=True, null=True)
    birth_date = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    first_name = models.CharField(verbose_name='Имя', max_length=50, blank=True)
    second_name = models.CharField(verbose_name='Фамилия', max_length=70, blank=True)
    patronymic = models.CharField(verbose_name='Отчество', max_length=70, null=True, blank=True)
    slug = models.SlugField(verbose_name='Slug ФИО', max_length=190, null=True, blank=True)
    position = models.CharField(verbose_name='Должность', max_length=100, null=True, blank=True)
    brief_info = models.TextField(verbose_name='Краткие данные',
                                  max_length=500, blank=True, null=True)
    public_phone_number = models.CharField(
        verbose_name='Публичный номер телефона', max_length=12, blank=True, null=True)
    public_email = models.EmailField(verbose_name='Публичный email',
                                     max_length=100, blank=True, null=True)
    public_telegram = models.URLField(verbose_name='Публичный telegram', blank=True, null=True)
    public_vk = models.URLField(verbose_name='Публичная страница Вконтакте', blank=True, null=True)
    public_fb = models.URLField(verbose_name='Публичная страница Facebook', blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.second_name)

    def get_absolute_url(self):
        return reverse('people_app:profile_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.second_name)+"_"+slugify(self.first_name) + \
            "_"+slugify(self.patronymic)
        return super(Profile, self).save(*args, **kwargs)


class Structure(models.Model):
    slug = models.SlugField(max_length=190, blank=True, null=True)
    name = models.CharField(verbose_name='Название', max_length=250)
    description = models.TextField(verbose_name='Описание')
    email = models.EmailField(max_length=100, blank=True, null=True)
    personnel = models.ManyToManyField('Profile', verbose_name='Сотрудники', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('people_app:structure_detail', args=[str(self.slug)])
