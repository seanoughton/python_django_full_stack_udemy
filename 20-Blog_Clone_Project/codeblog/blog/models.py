from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(model.Models):
    author = models.ForeignKey('auth.user')
    text = models.TextField()
    title = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.new())
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__():
        return self.title


class Comment(model.Models):
    post = models.ForeignKey('blog.Post',related_name="comments")
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.new())
    approved_comment = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__():
        return self.text
