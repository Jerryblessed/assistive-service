# Generated by Django 4.2 on 2023-06-12 07:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0009_auto_20210613_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default='tag website', help_text='Enter Your Address', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='banner_image',
            field=models.ImageField(default='slider-1.jpg', upload_to='banner'),
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='I love reading', help_text='Short Bio (eg. I love cats and games)', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='tag city', help_text='Enter Your City', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(default='tag', help_text='Enter Your Country', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='profile',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook_url',
            field=models.CharField(blank=True, default='#', help_text="Enter # if you don't have an account", max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='github_url',
            field=models.CharField(blank=True, default='#', help_text="Enter # if you don't have an account", max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile-pic-default.jpg', upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_url',
            field=models.CharField(blank=True, default='#', help_text="Enter # if you don't have an account", max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='job_title',
            field=models.CharField(default='tag', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_url',
            field=models.CharField(blank=True, default='#', help_text="Enter # if you don't have an account", max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='zip_code',
            field=models.CharField(default='tag', help_text='Enter Your Zip Code', max_length=100),
        ),
    ]
