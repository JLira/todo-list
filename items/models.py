from django.db import models
from lists.models import Lists


class Items(models.Model):
    id_item = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    id_list = models.ForeignKey(
        Lists, related_name='items', on_delete=models.CASCADE, blank=False, null=False
    )
    
