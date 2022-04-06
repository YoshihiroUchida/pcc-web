from django.db import models

class Prog_contents(models.Model):
    title = models.CharField(max_length = 100)  # タイトル
    web_site = models.URLField(blank = True)    # URL