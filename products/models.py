from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    price = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    cover = models.ImageField(verbose_name=_('cover image'), upload_to='products/covers')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', _('1 - Very Bad')),
        ('2', _('2 - Bad')),
        ('3', _('3 - Normal')),
        ('4', _('4 - Good')),
        ('5', _('5 - Perfect')),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(verbose_name=_('Comment:'))
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name=_('Stars:'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    # Manager
    objects = ActiveCommentsManager()
    all_comments = models.Manager()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product_id])
