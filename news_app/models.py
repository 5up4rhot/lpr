from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# used to generate slug based on title
from django.db.models.signals import pre_save
from .utils import get_unique_slug
# import filePATH generator
from .utils import get_file_path


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset()\
                          .filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(verbose_name='Загаловок', max_length=250)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    image = models.ImageField(verbose_name='Картинка',
                              upload_to=get_file_path, blank=True, null=True)
    slug = models.SlugField(verbose_name='Slug', max_length=250,
                            unique_for_date='publishtime', blank=True)
    author = models.ForeignKey(User, verbose_name='Автор',
                               related_name='blog_posts', on_delete=models.DO_NOTHING)
    body = RichTextUploadingField(verbose_name='Содержание')
    publishtime = models.DateTimeField(verbose_name='Дата публикации', blank=True, null=True)
    createtime = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updatetime = models.DateTimeField(verbose_name='Дата обновления', blank=True, null=True)
    status = models.CharField(verbose_name='Статус', max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    updated = models.BooleanField(verbose_name='Обновлено', default=False)
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.publishtime and self.status == 'published':
            self.publishtime = timezone.now()
        elif self.status == 'published' and self.publishtime:
            self.updatetime = timezone.now()
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-createtime',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_app:post_detail',
                       args=[self.publishtime.year,
                             self.publishtime.month,
                             self.publishtime.day,
                             self.slug])


# slug-generator
def auto_slug_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = get_unique_slug(instance)


pre_save.connect(auto_slug_receiver, sender=Post)
