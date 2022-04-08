from django.db import models

#==================================================
# TOPページのコンテンツ
class Home_contents(models.Model):
    title = models.CharField(max_length = 100)  # タイトル
    desc = models.CharField(max_length = 200)   # 概要
    page = models.CharField(max_length = 100)   # ページ (URL)
    icon = models.CharField(max_length = 200)   # HTMLのアイコン
    auth = models.BooleanField(default = False) # 権限

    def __str__(self):
        return self.title

#==================================================
# プログラミング教材関連
class Programming_contents(models.Model):
    num = models.IntegerField(default = 0)      # 番号
    title = models.CharField(max_length = 100)  # タイトル
    url = models.URLField(blank = True)         # URL

    def __str__(self):
        return str(self.num) + '_' + self.title

#==================================================
# Newsページの内容
class News_list(models.Model):
    date = models.DateField()                   # 日時
    desc = models.CharField(max_length = 200)   # 文章

    def __str__(self):
        return str(self.date) + self.desc
