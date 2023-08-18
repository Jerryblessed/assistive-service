# Generated by Django 4.2 on 2023-05-28 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_chair_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, default='category-default.jpg', upload_to='category_images'),
        ),
        migrations.AlterField(
            model_name='chair',
            name='image_credit',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
