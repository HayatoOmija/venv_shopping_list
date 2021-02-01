from django.db import models

# Create your models here.
from accounts.models import CustomUser


class ShoppingList(models.Model):
    """買い物リスト"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    product = models.CharField(verbose_name='買うもの', max_length=40)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'ShoppingList'

    def __str__(self):
        return self.product
