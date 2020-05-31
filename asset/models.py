from django.db import models


class Asset(models.Model):
    host_name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    host_group = models.CharField(max_length=20, blank=True, null=True)
    internal_ip = models.GenericIPAddressField(protocol='ipv4', max_length=20, blank=False, null=False, unique=True)
    external_ip = models.GenericIPAddressField(protocol='ipv4', max_length=20, unique=True, blank=True, null=True)
    host_cpu = models.SmallIntegerField(blank=False, null=False)
    host_memory = models.SmallIntegerField(blank=False, null=False)

    def __str__(self):
        return self.host_name
