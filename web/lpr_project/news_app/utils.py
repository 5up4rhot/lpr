# FilePATH generator import files
from django.utils import timezone
import uuid
import os

# Slug generator import files
from slugify import slugify


# Slug generator
def get_unique_slug(instance):
    """
    Takes a model instance, sluggable field name (such as 'title') of that
    model as string, slug field name (such as 'slug') of the model as string;
    returns a unique slug as string.
    """
    slug = slugify(instance.title)
    extension = 1
    ModelClass = instance.__class__

    while ModelClass.objects.filter(slug=slug).exists():
        slug = '{}-{}'.format(slug, extension)
        extension += 1

    return slug


# FilePATH generator
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4(), ext)
    return os.path.join('news/images/{}/{}/{}'.format(timezone.now().strftime('%Y'), timezone.now().strftime('%m'), timezone.now().strftime('%d')), filename)


# FileNAME generator for CKEDITOR
def get_filename(filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4(), ext)
    return filename
