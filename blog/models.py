from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
import uuid
from django.core.validators import EmailValidator
from ckeditor.fields import RichTextField


User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=100, default='Uncategorized')

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Post(models.Model):
    uuid = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(blank=True, null=True, max_length=500)
    title = models.CharField(max_length=500)
    featured_image = models.ImageField(upload_to='blog/featured_img', blank=True, null=True)
    body = RichTextField()
    excerpt = models.CharField(max_length=500, blank=True, null=True, help_text="Optional")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    read_time = models.DecimalField(decimal_places=0, max_digits=3)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_publised = models.BooleanField(default=True)
    stick_at_top = models.BooleanField(default=False, verbose_name="Stick to the Top of the Blog")
    allow_comments = models.BooleanField(default=True, help_text="Whether to allow the comments in post or not")

    def clean(self):
        self.slug = slugify(self.title)
        if Post.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            self.slug = f'{self.slug[:450]}-{str(self.uuid)[:8]}'
        super(Post, self).clean()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_at']
    
    def upvote(self):
        self.votes += 1
        self.save()
    
    def downvote(self):
        self.votes -= 1
        self.save()


# categories hirerachy ------------> to be applied


class Comment(models.Model):
    STATUS = (
        ('moderation', 'moderation'),
        ('approved', 'approved'),
        ('rejected', 'rejected'),
    )
    uuid = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name="replies")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100, blank=False, null=False)  
    email = models.EmailField(validators=[EmailValidator()])
    body = models.CharField(max_length=500, blank=False, null=False)
    status = models.CharField(max_length=100, choices=STATUS, blank=True, default='moderation')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

    class Meta:
        ordering = ['-created_at']
    
