from django.db import models
from django.utils import timezone
from datetime import datetime


class Food(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    qantity = models.IntegerField()
    open = models.BooleanField(default=False)
    open_date = models.DateField(
            blank=True, null=True)
    open_expire = models.DateField(
            blank=True, null=True)
    expire = models.DateField(
            blank=True, null=True)
    created_date = models.DateField(
            default=timezone.now)
    published_date = models.DateField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def days_to_exp_from_now(self):
        d2 = str(self.expire)
        d1 = datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f")
        d2 = datetime.strptime(d2, "%Y-%m-%d")
        return (d2 - d1).days

    def days_to_exp(self):
        d1 = datetime.strptime(str(self.created_date), "%Y-%m-%d")
        d2 = datetime.strptime(str(self.expire), "%Y-%m-%d")
        return (d2 - d1).days

    def percent_to_exp(self):
        if self.days_to_exp_from_now() > 0:
            result = 100/(self.days_to_exp()/self.days_to_exp_from_now())
            result = str(round(100 - result, 1)).replace(",",".")
        else:
            result = 100
        return result

    def type_of_result(self):
        if self.days_to_exp_from_now() <= 0 or self.percent_to_exp() >= 80 :
            type = "bg-danger"
        elif self.percent_to_exp() > 0 and self.percent_to_exp() < 50:
            type = "bg-success"
        elif self.percent_to_exp() >= "50" and self.percent_to_exp() < 80:
            type = "bg-warning"
        return type

    def __str__(self):
        return self.title
