from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):

    options = (
        ("draft", "Draft"),
        ("published", "Published")
    )

    title = models.CharField(max_length=251)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=options, default="draft")

    # List the post in Decending order because of '-' in created_at
    class Meta:
        ordering = ("-created_at",)

    # This method will provide a readable title while looking at database
    # from admin
    def __str__(self):
        return self.title
