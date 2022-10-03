from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    img_path = models.CharField(max_length=200)
    github_link = models.CharField(max_length=200)
    replit_link = models.CharField(
        max_length=200, default='https://replit.com/@BenSpeakman1')
    website_link = models.CharField(max_length=200, null=True, blank=True)
    language = models.CharField(max_length=200, null=True, blank=True)
    language_icon = models.CharField(max_length=200, null=True, blank=True)
    publish_date = models.DateTimeField('date published')

    def __str__(self):
        return self.project_name
