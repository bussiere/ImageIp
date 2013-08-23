from django.db import models
class Log(models.Model):
    Ip = models.TextField(max_length=18, null=True, blank=True)
    Referer = models.TextField(max_length=2048, null=True, blank=True)
    UserAgent = models.TextField(max_length=2048, null=True, blank=True)
    Date =  models.DateTimeField(auto_now_add=True,editable=True)
    Date.editable=True
    def __unicode__(self):
        return str(self.Ip + "" + str(self.Date))
# Create your models here.
