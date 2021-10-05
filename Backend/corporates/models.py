from django.db import models
from django.conf import settings

# Create your models here.

class Corporate(models.Model):
    name = models.CharField(max_length=20)
    E_rating = models.FloatField()
    S_rating = models.FloatField()
    G_rating = models.FloatField()
    ESG_rating = models.FloatField()
    scrap_cnt = models.IntegerField()
    scrap_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='scrap_corporates')
    today_cnt = models.IntegerField()
    first = models.IntegerField()
    second = models.IntegerField()
    third = models.IntegerField()

class Environment(models.Model):
    corporate = models.ForeignKey(Corporate, on_delete=models.CASCADE)
    co2 = models.FloatField(blank=True, null=True)
    energy = models.FloatField(blank=True, null=True)
    total = models.FloatField()
    news_pos_cnt = models.IntegerField()
    news_neg_cnt = models.IntegerField()

class Social(models.Model):
    corporate = models.ForeignKey(Corporate, on_delete=models.CASCADE)
    average_term = models.FloatField(blank=True, null=True)
    term_ratio = models.FloatField(blank=True, null=True)
    woman_ratio = models.FloatField(blank=True, null=True)
    total = models.FloatField()
    news_pos_cnt = models.IntegerField()
    news_neg_cnt = models.IntegerField()
    
class Governance(models.Model):
    corporate = models.ForeignKey(Corporate, on_delete=models.CASCADE)
    board_ratio = models.FloatField(blank=True, null=True)
    board_independency = models.BooleanField(blank=True, null=True)
    salary_gap = models.FloatField(blank=True, null=True)
    dividen_ratio = models.FloatField(blank=True, null=True)
    largest_shareholder = models.FloatField(blank=True, null=True)
    total = models.FloatField()
    news_pos_cnt = models.IntegerField()
    news_neg_cnt = models.IntegerField()
    
class News(models.Model):
    corporate = models.ForeignKey(Corporate, on_delete=models.CASCADE)
    url = models.CharField(max_length=300)
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.CharField(max_length=50)
    category = models.CharField(max_length=10)
    evaluation = models.IntegerField(default=0)