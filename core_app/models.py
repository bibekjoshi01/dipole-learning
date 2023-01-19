from django.db import models
from ckeditor.fields import RichTextField
from api.validators import validate_subject_icon
from django.core.validators import FileExtensionValidator

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Subject(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='unit', null=True)
    title = models.CharField(
        max_length=255,
        unique=True,
        help_text="Main Documentation Topic"
    )
    icon = models.ImageField(
        upload_to='subject/icons',
        blank=True,
        null=True,
        validators=[validate_subject_icon, FileExtensionValidator(['png', 'svg', 'jpg', 'jpeg'])]
    )
    description = RichTextField()

    def __str__(self):
        return self.title


class Unit(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='unit', null=True)
    title = models.CharField(max_length=255)
    description = RichTextField()
    
    def __str__(self):
        return self.title


class Chapter(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='chapter', null=True)
    title = models.CharField(max_length=255)
    description = RichTextField()
    
    def __str__(self):
        return self.title


class Heading(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='heading', null=True)
    title = models.CharField(max_length=255)
    description = RichTextField()
    
    def __str__(self):
        return self.title


class Sub_Heading(models.Model):
    heading = models.ForeignKey(Heading, on_delete=models.CASCADE, related_name='heading', null=True)
    title = models.CharField(max_length=255)
    description = RichTextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Sub Heading'
        verbose_name_plural = 'Sub Headings'


