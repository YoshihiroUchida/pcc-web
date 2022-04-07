from django.db import models

class Prog_contents(models.Model):
    num = models.IntegerField(default = 0)      # 番号
    title = models.CharField(max_length = 100)  # タイトル
    web_site = models.URLField(blank = True)    # URL

    # レコードの表示部分
    def __str__(self):
        return str(self.num) + '_' + self.title