from django.db import models

class IpAddress(models.Model):
    pub_date = models.DateTimeField('date published')
    ip_address = models.GenericIPAddressField()
    port = models.IntegerField()
    def __str__(self):
        return "{}:{}".format(self.ip_address,self.port)