# Generated by Django 4.2.3 on 2023-08-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_pv_post_uv'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_html',
            field=models.TextField(blank=True, editable=False, verbose_name='正文html'),
        ),
    ]
