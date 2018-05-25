from django.db import models
from django.utils import timezone


class Food(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    qantity = models.IntegerField()
    open = models.BooleanField(default=False)
    open_date = models.DateTimeField(
            blank=True, null=True)
    open_expire = models.DateTimeField(
            blank=True, null=True)
    expire = models.DateTimeField(
            blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
