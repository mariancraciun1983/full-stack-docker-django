from django.db import models


class UserEmailTemplate(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    title = models.CharField(max_length=128, blank=False, null=False)
    body = models.TextField(max_length=10000, blank=False, null=False)
    body_html = models.TextField(max_length=10000, blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("id",)
        db_table = "app_UserEmailTemplate"
