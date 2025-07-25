# Generated by Django 5.2.3 on 2025-06-29 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_rename_published_at_artwork_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='likes_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='artwork',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='artwork',
            name='tags',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='published_date',
            field=models.DateTimeField(),
        ),
    ]
