from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Principle(models.Model):

    content = models.CharField(
        max_length=500, help_text="Enter content for this Principle")


class Opinion(models.Model):

    subject = models.CharField(
        max_length=100, verbose_name='Предмет обсуждения', help_text="Enter subject of Opinion")
    content = RichTextField(verbose_name='Точка зрения', help_text="Enter content for Opinion")


class Reform(models.Model):

    header_choices = (
        ('law', 'Констутиционно-правовые реформы'),
        ('justice', 'Судебно-правоохранительная реформа'),
        ('social', 'Социальные рефомы'),
        ('economic', 'Экономические реформы'),
        ('military', 'Военно-промышленная реформа'),
        ('fp', 'Внешнеполитическая реформа'),
    )
    header = models.CharField(
        max_length=10, verbose_name='Область применения', choices=header_choices)
    subheader = models.CharField(max_length=100, verbose_name='Тезис',
                                 help_text="Enter subheader of Reform")
    content = RichTextField(verbose_name='Позиция', help_text="Enter content for Reform")


class QA(models.Model):
    subject_choices = (
        ('1_lib', 'Либертарианство'),
        ('2_soc', 'Социальная поддержка'),
        ('3_weapon', 'Оружие'),
        ('4_copyright', 'Копирайт'),
        ('5_terms', 'Терминология'),
    )

    subject = models.CharField(
        max_length=30, verbose_name='Предмет обсуждения', choices=subject_choices)
    question = models.TextField(verbose_name='Вопрос', help_text="Enter question text")
    answer = models.TextField(verbose_name='Ответ', help_text="Enter answer text")
