from django.db import models
from users.models import Users

class Lists(models.Model):
    id_list = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    id_user = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='lists', blank=False, null=False
    )

    class Meta:
        managed = True
        db_table = 'lists'
        
