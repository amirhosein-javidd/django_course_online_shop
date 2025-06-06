# Generated by Django 5.1.7 on 2025-04-14 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_comment_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cover',
            field=models.ImageField(blank=True, upload_to='products/covers', verbose_name='cover image'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='stars',
            field=models.CharField(choices=[('1', '1 - Very Bad'), ('2', '2 - Bad'), ('3', '3 - Normal'), ('4', '4 - Good'), ('5', '5 - Perfect')], max_length=10, verbose_name='Stars:'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='Comment:'),
        ),
    ]
