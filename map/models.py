from django.db import models

# Create your models here.
class Stat(models.Model):
    time = models.BigIntegerField(null=False, verbose_name=u"时间戳")
    longitude = models.FloatField(null=False, verbose_name=u"经度")
    latitude = models.FloatField(null=False, verbose_name=u"纬度")

    class Meta:
        verbose_name = u"统计信息表"
        verbose_name_plural = verbose_name
        db_table = "stat"