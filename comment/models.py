from django.db import models
from django.contrib.auth.models import User
from post.models import Post
from django.utils import timezone

class Comment(models.Model):
    of_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=255)
    date_commented = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"A comment for post \"{self.of_post.title}\", by \"{self.author}\""
